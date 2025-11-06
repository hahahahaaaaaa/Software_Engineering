import mysql.connector
from mysql.connector import Error
from typing import Dict, List, Optional, Tuple

class DBConnector:
    """Komodo Hub数据库连接工具类"""
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self) -> bool:
        """建立数据库连接"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4'
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)  # 返回字典格式结果
                return True
        except Error as e:
            print(f"数据库连接失败：{e}")
        return False

    def close(self) -> None:
        """关闭数据库连接"""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
        print("数据库连接已关闭")

    def execute_query(self, query: str, params: Tuple = ()) -> Optional[List[Dict]]:
        """执行查询类SQL（SELECT），返回结果列表"""
        if not self.connect():
            return None
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except Error as e:
            print(f"查询失败：{e}，SQL: {query}，参数: {params}")
            return None
        finally:
            self.close()

    def execute_update(self, query: str, params: Tuple = ()) -> Optional[int]:
        """执行更新类SQL（INSERT/UPDATE/DELETE），返回受影响行数"""
        if not self.connect():
            return None
        try:
            self.cursor.execute(query, params)
            self.connection.commit()  # 提交事务
            return self.cursor.rowcount  # 返回受影响行数
        except Error as e:
            self.connection.rollback()  # 事务回滚
            print(f"更新失败：{e}，SQL: {query}，参数: {params}")
            return None
        finally:
            self.close()

class RoleCRUD:
    """角色表CRUD操作类"""
    def __init__(self, db_connector: DBConnector):
        self.db = db_connector

    def create_role(self, role_name: str, role_desc: str) -> Optional[int]:
        """
        创建新角色（文档中仅需初始化8种角色，此方法用于扩展）
        :param role_name: 角色名称（如“社区管理员”）
        :param role_desc: 角色描述（对应文档中角色职责）
        :return: 新增角色ID，失败返回None
        """
        query = """
            INSERT INTO roles (role_name, role_desc, create_time)
            VALUES (%s, %s, CURRENT_TIMESTAMP)
        """
        params = (role_name, role_desc)
        row_count = self.db.execute_update(query, params)
        if row_count and row_count > 0:
            # 获取新增角色ID
            query = "SELECT LAST_INSERT_ID() AS role_id"
            result = self.db.execute_query(query)
            return result[0]['role_id'] if result else None
        return None

    def get_role_by_id(self, role_id: int) -> Optional[Dict]:
        """根据角色ID查询角色信息"""
        query = "SELECT * FROM roles WHERE role_id = %s"
        result = self.db.execute_query(query, (role_id,))
        return result[0] if result else None

    def get_all_roles(self) -> Optional[List[Dict]]:
        """查询所有角色（文档中8种核心角色）"""
        query = "SELECT * FROM roles ORDER BY role_id ASC"
        return self.db.execute_query(query)

    def update_role_desc(self, role_id: int, new_desc: str) -> bool:
        """更新角色描述（如调整职责说明）"""
        query = "UPDATE roles SET role_desc = %s WHERE role_id = %s"
        row_count = self.db.execute_update(query, (new_desc, role_id))
        return row_count and row_count > 0

    def delete_role(self, role_id: int) -> bool:
        """删除角色（需确保无关联用户，文档中8种角色不建议删除）"""
        # 先检查是否有关联用户
        check_query = "SELECT COUNT(*) AS user_count FROM users WHERE role_id = %s"
        check_result = self.db.execute_query(check_query, (role_id,))
        if check_result and check_result[0]['user_count'] > 0:
            print(f"删除失败：角色ID {role_id} 仍有关联用户（{check_result[0]['user_count']}个）")
            return False
        # 执行删除
        delete_query = "DELETE FROM roles WHERE role_id = %s"
        row_count = self.db.execute_update(delete_query, (role_id,))
        return row_count and row_count > 0

class UserCRUD:
    """用户表CRUD操作类（关联角色）"""
    def __init__(self, db_connector: DBConnector):
        self.db = db_connector

    def create_user(
        self, role_id: int, username: str, password: str,
        nickname: str, avatar_url: Optional[str] = None,
        is_privacy_protected: int = 0
    ) -> Optional[int]:
        """
        创建用户（支持所有角色：注册普通用户、学生、教师等）
        :param is_privacy_protected: 隐私保护标识（1=是，如学生；0=否，如社区成员）
        :return: 新增用户ID
        """
        # 密码加密存储（使用SHA256，匹配前文MySQL初始化逻辑）
        query = """
            INSERT INTO users (role_id, username, password_hash, nickname, avatar_url, is_privacy_protected, status, create_time)
            VALUES (%s, %s, SHA2(%s, 256), %s, %s, %s, 1, CURRENT_TIMESTAMP)
        """
        params = (role_id, username, password, nickname, avatar_url, is_privacy_protected)
        row_count = self.db.execute_update(query, params)
        if row_count and row_count > 0:
            query = "SELECT LAST_INSERT_ID() AS user_id"
            result = self.db.execute_query(query)
            return result[0]['user_id'] if result else None
        return None

    def get_user_by_id(self, user_id: int) -> Optional[Dict]:
        """根据用户ID查询用户（含角色名称）"""
        query = """
            SELECT u.*, r.role_name 
            FROM users u
            LEFT JOIN roles r ON u.role_id = r.role_id
            WHERE u.user_id = %s
        """
        result = self.db.execute_query(query, (user_id,))
        return result[0] if result else None

    def get_users_by_role(self, role_id: int) -> Optional[List[Dict]]:
        """查询指定角色的所有用户（如查询所有学生）"""
        query = """
            SELECT u.*, r.role_name 
            FROM users u
            LEFT JOIN roles r ON u.role_id = r.role_id
            WHERE u.role_id = %s AND u.status = 1
        """
        return self.db.execute_query(query, (role_id,))

    def update_user_privacy(self, user_id: int, is_privacy_protected: int) -> bool:
        """更新用户隐私保护状态（如学生需强制开启）"""
        query = "UPDATE users SET is_privacy_protected = %s WHERE user_id = %s"
        row_count = self.db.execute_update(query, (is_privacy_protected, user_id))
        return row_count and row_count > 0

    def disable_user(self, user_id: int) -> bool:
        """禁用用户（软删除，保留数据）"""
        query = "UPDATE users SET status = 0 WHERE user_id = %s"
        row_count = self.db.execute_update(query, (user_id,))
        return row_count and row_count > 0

class CommunityCRUD:
    """社区表与社区成员关联表CRUD操作类"""
    def __init__(self, db_connector: DBConnector):
        self.db = db_connector

    def create_community(
        self, community_name: str, province_count: int,
        office_count: int, member_count: int, create_year: int
    ) -> Optional[int]:
        """创建社区（如文档中的#SaveOurAnimals）"""
        query = """
            INSERT INTO communities (community_name, province_count, office_count, member_count, create_year, status)
            VALUES (%s, %s, %s, %s, %s, 1)
        """
        params = (community_name, province_count, office_count, member_count, create_year)
        row_count = self.db.execute_update(query, params)
        if row_count and row_count > 0:
            query = "SELECT LAST_INSERT_ID() AS community_id"
            result = self.db.execute_query(query)
            return result[0]['community_id'] if result else None
        return None

    def add_community_member(self, user_id: int, community_id: int, is_admin: int = 0) -> bool:
        """
        添加社区成员（区分普通成员与管理员）
        :param is_admin: 1=社区管理员，0=普通成员
        """
        # 检查用户角色是否为“社区成员”或“社区管理员”
        role_check = """
            SELECT r.role_name FROM users u
            LEFT JOIN roles r ON u.role_id = r.role_id
            WHERE u.user_id = %s AND r.role_name IN ('社区成员', '社区管理员')
        """
        check_result = self.db.execute_query(role_check, (user_id,))
        if not check_result:
            print(f"添加失败：用户ID {user_id} 非社区相关角色")
            return False
        # 检查是否已关联该社区
        exist_check = "SELECT * FROM community_members WHERE user_id = %s AND community_id = %s"
        exist_result = self.db.execute_query(exist_check, (user_id, community_id))
        if exist_result:
            print(f"添加失败：用户ID {user_id} 已加入社区ID {community_id}")
            return False
        # 执行添加
        query = """
            INSERT INTO community_members (user_id, community_id, is_admin, join_time)
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
        """
        row_count = self.db.execute_update(query, (user_id, community_id, is_admin))
        return row_count and row_count > 0

    def get_community_members(self, community_id: int) -> Optional[List[Dict]]:
        """查询社区所有成员（含用户信息与角色）"""
        query = """
            SELECT cm.*, u.username, u.nickname, u.avatar_url, r.role_name
            FROM community_members cm
            LEFT JOIN users u ON cm.user_id = u.user_id
            LEFT JOIN roles r ON u.role_id = r.role_id
            WHERE cm.community_id = %s
        """
        return self.db.execute_query(query, (community_id,))

    def remove_community_member(self, user_id: int, community_id: int) -> bool:
        """移除社区成员"""
        query = "DELETE FROM community_members WHERE user_id = %s AND community_id = %s"
        row_count = self.db.execute_update(query, (user_id, community_id))
        return row_count and row_count > 0

class CommunityCRUD:
    """社区表与社区成员关联表CRUD操作类"""
    def __init__(self, db_connector: DBConnector):
        self.db = db_connector

    def create_community(
        self, community_name: str, province_count: int,
        office_count: int, member_count: int, create_year: int
    ) -> Optional[int]:
        """创建社区（如文档中的#SaveOurAnimals）"""
        query = """
            INSERT INTO communities (community_name, province_count, office_count, member_count, create_year, status)
            VALUES (%s, %s, %s, %s, %s, 1)
        """
        params = (community_name, province_count, office_count, member_count, create_year)
        row_count = self.db.execute_update(query, params)
        if row_count and row_count > 0:
            query = "SELECT LAST_INSERT_ID() AS community_id"
            result = self.db.execute_query(query)
            return result[0]['community_id'] if result else None
        return None

    def add_community_member(self, user_id: int, community_id: int, is_admin: int = 0) -> bool:
        """
        添加社区成员（区分普通成员与管理员）
        :param is_admin: 1=社区管理员，0=普通成员
        """
        # 检查用户角色是否为“社区成员”或“社区管理员”
        role_check = """
            SELECT r.role_name FROM users u
            LEFT JOIN roles r ON u.role_id = r.role_id
            WHERE u.user_id = %s AND r.role_name IN ('社区成员', '社区管理员')
        """
        check_result = self.db.execute_query(role_check, (user_id,))
        if not check_result:
            print(f"添加失败：用户ID {user_id} 非社区相关角色")
            return False
        # 检查是否已关联该社区
        exist_check = "SELECT * FROM community_members WHERE user_id = %s AND community_id = %s"
        exist_result = self.db.execute_query(exist_check, (user_id, community_id))
        if exist_result:
            print(f"添加失败：用户ID {user_id} 已加入社区ID {community_id}")
            return False
        # 执行添加
        query = """
            INSERT INTO community_members (user_id, community_id, is_admin, join_time)
            VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
        """
        row_count = self.db.execute_update(query, (user_id, community_id, is_admin))
        return row_count and row_count > 0

    def get_community_members(self, community_id: int) -> Optional[List[Dict]]:
        """查询社区所有成员（含用户信息与角色）"""
        query = """
            SELECT cm.*, u.username, u.nickname, u.avatar_url, r.role_name
            FROM community_members cm
            LEFT JOIN users u ON cm.user_id = u.user_id
            LEFT JOIN roles r ON u.role_id = r.role_id
            WHERE cm.community_id = %s
        """
        return self.db.execute_query(query, (community_id,))

    def remove_community_member(self, user_id: int, community_id: int) -> bool:
        """移除社区成员"""
        query = "DELETE FROM community_members WHERE user_id = %s AND community_id = %s"
        row_count = self.db.execute_update(query, (user_id, community_id))
        return row_count and row_count > 0

import random
import string

class SchoolCRUD:
    """学校表与学校成员关联表CRUD操作类"""
    def __init__(self, db_connector: DBConnector):
        self.db = db_connector

    def create_school(
        self, school_name: str, location: str,
        is_subscribed: int = 0, subscription_start: Optional[str] = None,
        subscription_end: Optional[str] = None
    ) -> Optional[int]:
        """创建学校（如文档中的乌戎拉亚小学）"""
        query = """
            INSERT INTO schools (school_name, location, is_subscribed, subscription_start, subscription_end)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (school_name, location, is_subscribed, subscription_start, subscription_end)
        row_count = self.db.execute_update(query, params)
        if row_count and row_count > 0:
            query = "SELECT LAST_INSERT_ID() AS school_id"
            result = self.db.execute_query(query)
            return result[0]['school_id'] if result else None
        return None

    def generate_access_code(self, school_id: int) -> str:
        """生成学生专属访问码（格式：学校缩写_年份_随机6位，如UK_2024_ABC123）"""
        # 获取学校缩写（取学校名称前2个字母大写）
        school = self.get_school_by_id(school_id)
        if not school:
            school_abbr = "SCH"
        else:
            school_abbr = school['school_name'][:2].upper()
        # 生成随机6位字符（字母+数字）
        random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return f"{school_abbr}_2024_{random_str}"

    def add_school_member(
        self, user_id: int, school_id: int, class_info: Optional[str] = None,
        is_teacher: int = 0, is_school_admin: int = 0
    ) -> bool:
        """
        添加学校成员（区分学生、教师、学校管理员）
        :param is_teacher: 1=教师，0=学生；is_school_admin=1=学校管理员（优先级更高）
        """
        # 检查用户角色
        role_check = """
            SELECT r.role_name FROM users u
            LEFT JOIN roles r ON u.role_id = r.role_id
            WHERE u.user_id = %s AND r.role_name IN ('学生', '学校教师', '学校管理员')
        """
        check_result = self.db.execute_query(role_check, (user_id,))
        if not check_result:
            print(f"添加失败：用户ID {user_id} 非学校相关角色")
            return False
        # 生成学生专属访问码（仅学生需要）
        access_code = None
        if not is_teacher and not is_school_admin:
            access_code = self.generate_access_code(school_id)
            # 确保访问码唯一
            while self.db.execute_query("SELECT * FROM school_members WHERE access_code = %s", (access_code,)):
                access_code = self.generate_access_code(school_id)
        # 执行添加
        query = """
            INSERT INTO school_members (user_id, school_id, class_info, is_teacher, is_school_admin, access_code, join_time)
            VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
        """
        params = (user_id, school_id, class_info, is_teacher, is_school_admin, access_code)
        row_count = self.db.execute_update(query, params)
        return row_count and row_count > 0

    def get_school_by_id(self, school_id: int) -> Optional[Dict]:
        """查询学校信息（含订阅状态）"""
        query = "SELECT * FROM schools WHERE school_id = %s"
        result = self.db.execute_query(query, (school_id,))
        return result[0] if result else None

    def get_students_by_school(self, school_id: int, class_info: Optional[str] = None) -> Optional[List[Dict]]:
        """查询学校学生（支持按班级筛选，含访问码）"""
        query = """
            SELECT sm.*, u.username, u.nickname, u.avatar_url
            FROM school_members sm
            LEFT JOIN users u ON sm.user_id = u.user_id
            WHERE sm.school_id = %s AND sm.is_teacher = 0 AND sm.is_school_admin = 0
        """
        params = (school_id,)
        if class_info:
            query += " AND sm.class_info = %s"
            params = (school_id, class_info)
        return self.db.execute_query(query, params)