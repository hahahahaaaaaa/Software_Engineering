import streamlit as st
from streamlit_option_menu import option_menu

# ---------------------- 1. 页面基础配置 ----------------------
st.set_page_config(
    page_title="Komodo Hub - 超级管理中心",
    page_icon="🐉",
    layout="wide"
)

# ---------------------- 2. 顶部导航栏（超级管理员登录状态） ----------------------
with st.container():
    header_col1, header_col2 = st.columns([4, 1])

    # 左侧：平台标题与品牌（保持原风格居中）
    with header_col1:
        st.markdown("""
            <h1 style='text-align: center; color:#2E8B57; font-weight: bold; font-size: 4.5rem;'>
                🐉 Komodo Hub
            </h1>
        """, unsafe_allow_html=True)
        st.markdown("""
            <p style='text-align: center; color:#666; font-weight: bold; font-size: 1.2rem;'>
                印尼濒危物种保护数字化社区平台 - 超级管理中心
            </p>
        """, unsafe_allow_html=True)

    # 右侧：超级管理员标识（替换原登录入口）
    with header_col2:
        st.markdown("""
            <div style='text-align: right; padding-top: 20px;'>
                <span style='color:#DAA520; font-weight: bold;'>👑 超级管理员</span>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# ---------------------- 3. 核心功能标签 ----------------------
selected_tab = option_menu(
    menu_title=None,
    options=["社区组织管理", "学校组织管理"],
    icons=["people-group", "school"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#2E8B57", "font-size": "18px"},
        "nav-link": {
            "font-size": "12px",
            "padding": "10px 20px",
            "color": "#333",
            "--hover-color": "#e6f7ef"
        },
        "nav-link-selected": {"background-color": "#2E8B57", "color": "white"},
    }
)

# ---------------------- 模拟数据（具体组织下的具体账号） ----------------------
# 1. 社区组织及下属账号
community_accounts = {
    "COM001": {  # #SaveOurAnimals社区
        "org_info": {"name": "#SaveOurAnimals社区", "region": "雅加达", "admin": "巴古斯", "email": "bagus@xxx.org",
                     "status": "正常"},
        "user_accounts": [
            {"user_id": "COM001-ADM001", "name": "巴古斯", "role": "社区管理员", "email": "bagus@xxx.org",
             "phone": "+62 812-1234-5678", "join_date": "2024-01-15", "status": "活跃"},
            {"user_id": "COM001-MEM001", "name": "安达", "role": "社区成员", "email": "anda@xxx.org",
             "phone": "+62 813-2345-6789", "join_date": "2024-02-20", "status": "活跃"},
            {"user_id": "COM001-MEM002", "name": "莱娜", "role": "社区成员", "email": "lena@xxx.org",
             "phone": "+62 814-3456-7890", "join_date": "2024-03-10", "status": "不活跃"},
            {"user_id": "COM001-MEM003", "name": "哈迪", "role": "社区成员", "email": "hadi@xxx.org",
             "phone": "+62 815-4567-8901", "join_date": "2024-04-05", "status": "活跃"}
        ]
    },
    "COM002": {  # 苏门答腊保护联盟
        "org_info": {"name": "苏门答腊保护联盟", "region": "苏门答腊", "admin": "安迪", "email": "andi@xxx.org",
                     "status": "正常"},
        "user_accounts": [
            {"user_id": "COM002-ADM001", "name": "安迪", "role": "社区管理员", "email": "andi@xxx.org",
             "phone": "+62 812-5678-9012", "join_date": "2024-01-20", "status": "活跃"},
            {"user_id": "COM002-MEM001", "name": "莎莉", "role": "社区成员", "email": "sari@xxx.org",
             "phone": "+62 813-6789-0123", "join_date": "2024-02-25", "status": "活跃"}
        ]
    },
    "COM003": {  # 巴厘岛鸟类社区
        "org_info": {"name": "巴厘岛鸟类社区", "region": "巴厘岛", "admin": "妮娅", "email": "nia@xxx.org",
                     "status": "禁用"},
        "user_accounts": [
            {"user_id": "COM003-ADM001", "name": "妮娅", "role": "社区管理员", "email": "nia@xxx.org",
             "phone": "+62 812-9012-3456", "join_date": "2024-01-22", "status": "禁用"},
            {"user_id": "COM003-MEM001", "name": "拉玛", "role": "社区成员", "email": "rama@xxx.org",
             "phone": "+62 813-0123-4567", "join_date": "2024-03-01", "status": "禁用"}
        ]
    }
}

# 2. 学校组织及下属账号
school_accounts = {
    "SCH001": {  # 雅加达第一中学
        "org_info": {"name": "雅加达第一中学", "type": "中学", "admin": "卡尔", "email": "karl@xxx.edu",
                     "status": "正常"},
        "user_accounts": [
            {"user_id": "SCH001-ADM001", "name": "卡尔", "role": "学校管理员", "email": "karl@xxx.edu",
             "phone": "+62 812-2345-6789", "join_date": "2024-01-10", "status": "活跃"},
            {"user_id": "SCH001-TCH001", "name": "李老师", "role": "教师", "subject": "生物",
             "email": "teacher.li@xxx.edu", "join_date": "2024-01-15", "status": "活跃"},
            {"user_id": "SCH001-TCH002", "name": "王老师", "role": "教师", "subject": "地理",
             "email": "teacher.wang@xxx.edu", "join_date": "2024-01-20", "status": "活跃"},
            {"user_id": "SCH001-STU001", "name": "张三", "role": "学生", "grade": "初三", "class": "3班",
             "email": "student.zhang@xxx.edu", "join_date": "2024-02-01", "status": "活跃"},
            {"user_id": "SCH001-STU002", "name": "李四", "role": "学生", "grade": "初二", "class": "2班",
             "email": "student.li@xxx.edu", "join_date": "2024-02-05", "status": "活跃"}
        ]
    },
    "SCH002": {  # 巴厘岛环保小学
        "org_info": {"name": "巴厘岛环保小学", "type": "小学", "admin": "茉莉", "email": "moli@xxx.edu",
                     "status": "正常"},
        "user_accounts": [
            {"user_id": "SCH002-ADM001", "name": "茉莉", "role": "学校管理员", "email": "moli@xxx.edu",
             "phone": "+62 812-3456-7890", "join_date": "2024-01-12", "status": "活跃"},
            {"user_id": "SCH002-TCH001", "name": "张老师", "role": "教师", "subject": "科学",
             "email": "teacher.zhang@xxx.edu", "join_date": "2024-01-18", "status": "活跃"},
            {"user_id": "SCH002-STU001", "name": "王五", "role": "学生", "grade": "五年级", "class": "1班",
             "email": "student.wang@xxx.edu", "join_date": "2024-02-10", "status": "活跃"}
        ]
    },
    "SCH003": {  # 苏门答腊实验高中
        "org_info": {"name": "苏门答腊实验高中", "type": "高中", "admin": "阿明", "email": "amin@xxx.edu",
                     "status": "禁用"},
        "user_accounts": [
            {"user_id": "SCH003-ADM001", "name": "阿明", "role": "学校管理员", "email": "amin@xxx.edu",
             "phone": "+62 812-4567-8901", "join_date": "2024-01-14", "status": "禁用"},
            {"user_id": "SCH003-TCH001", "name": "刘老师", "role": "教师", "subject": "化学",
             "email": "teacher.liu@xxx.edu", "join_date": "2024-01-25", "status": "禁用"}
        ]
    }
}

# ---------------------- 4. 社区组织管理（含具体账号查看） ----------------------
if selected_tab == "社区组织管理":
    st.markdown("""
        <h2 style='text-align: center; color:#333;'>社区组织账号管理</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center;'>管理社区组织及下属具体用户账号</p>
    """, unsafe_allow_html=True)

    # 4.1 新增社区组织（保持极简）
    st.markdown("""
    <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
        <h3 style='color:#2E8B57;'>📝 新增社区组织</h3>
    </div>
    """, unsafe_allow_html=True)

    with st.form("add_community"):
        col1, col2 = st.columns(2)
        with col1:
            comm_name = st.text_input("社区名称*", placeholder="例：#SaveOurAnimals社区")
            comm_region = st.selectbox("所在区域*", ["雅加达", "巴厘岛", "苏门答腊", "爪哇岛"])
        with col2:
            comm_admin = st.text_input("负责人姓名*", placeholder="社区主账号持有人")
            comm_email = st.text_input("负责人邮箱*", placeholder="用于登录的账号")

        submit_btn = st.form_submit_button("创建账号", use_container_width=True, type="primary")
        if submit_btn:
            if comm_name and comm_region and comm_admin and comm_email:
                st.success(f"「{comm_name}」社区账号已创建，初始密码已发送至 {comm_email}")
            else:
                st.warning("带「*」字段为必填项，请补充完整")

    # 4.2 社区组织列表（新增“查看账号”按钮）
    st.markdown("""
    <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
        <h3 style='color:#2E8B57;'>📋 现有社区组织</h3>
    </div>
    """, unsafe_allow_html=True)

    # 展示社区列表（含查看账号功能）
    for comm_id, comm_data in community_accounts.items():
        comm_info = comm_data["org_info"]
        col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])
        col1.write(f"**{comm_info['name']}**（{comm_id}）")
        col2.write(comm_info['region'])
        col3.write(comm_info['admin'])
        col4.write(
            f"<span style='color:{'green' if comm_info['status'] == '正常' else 'red'}'>{comm_info['status']}</span>",
            unsafe_allow_html=True)

        # 查看账号按钮
        view_btn = col5.button("查看账号", key=f"view_comm_{comm_id}", use_container_width=True)
        # 状态切换按钮
        if comm_info['status'] == "正常":
            if col6.button("禁用", key=f"ban_comm_{comm_id}", use_container_width=True, type="secondary"):
                st.success(f"「{comm_info['name']}」及下属账号已全部禁用")
        else:
            if col6.button("启用", key=f"unban_comm_{comm_id}", use_container_width=True, type="primary"):
                st.success(f"「{comm_info['name']}」及下属账号已全部启用")

        # 点击“查看账号”后展示具体用户列表
        if view_btn:
            st.markdown(f"""
            <div style='border:1px solid #d4eedd; border-radius:10px; padding:15px; margin:10px 0; background-color:#f9fbf9;'>
                <h4 style='color:#2E8B57; margin-top:0;'>{comm_info['name']} - 具体用户账号（共{len(comm_data['user_accounts'])}个）</h4>
            </div>
            """, unsafe_allow_html=True)

            # 展示该社区下的具体账号
            for user in comm_data['user_accounts']:
                with st.expander(f"🆔 {user['user_id']} | {user['name']}（{user['role']}）", expanded=False):
                    col_a, col_b, col_c = st.columns(3)
                    col_a.write(f"**邮箱**：{user['email']}")
                    col_a.write(f"**电话**：{user.get('phone', '未填写')}")
                    col_b.write(f"**加入时间**：{user['join_date']}")
                    col_b.write(
                        f"**账号状态**：<span style='color:{'green' if user['status'] == '活跃' else 'red'}'>{user['status']}</span>",
                        unsafe_allow_html=True)
                    col_c.write(f"**角色权限**：{user['role']}")

                    # 单个账号状态切换（独立于组织状态）
                    if user['status'] == "活跃":
                        if st.button("禁用该账号", key=f"ban_user_{user['user_id']}", use_container_width=True,
                                     type="secondary"):
                            st.success(f"「{user['name']}」账号已禁用")
                    else:
                        if st.button("启用该账号", key=f"unban_user_{user['user_id']}", use_container_width=True,
                                     type="primary"):
                            st.success(f"「{user['name']}」账号已启用")

# ---------------------- 5. 学校组织管理（含具体账号查看） ----------------------
else:
    st.markdown("""
        <h2 style='text-align: center; color:#333;'>学校组织账号管理</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center;'>管理学校组织及下属具体用户账号（管理员/教师/学生）</p>
    """, unsafe_allow_html=True)

    # 5.1 新增学校组织（保持极简）
    st.markdown("""
    <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
        <h3 style='color:#2E8B57;'>📝 新增学校组织</h3>
    </div>
    """, unsafe_allow_html=True)

    with st.form("add_school"):
        col1, col2 = st.columns(2)
        with col1:
            school_name = st.text_input("学校名称*", placeholder="例：雅加达第一中学")
            school_type = st.selectbox("学校类型*", ["小学", "中学", "高中", "综合性学校"])
        with col2:
            school_admin = st.text_input("管理员姓名*", placeholder="负责平台对接人")
            school_email = st.text_input("管理员邮箱*", placeholder="用于登录的账号")

        submit_btn = st.form_submit_button("创建账号", use_container_width=True, type="primary")
        if submit_btn:
            if school_name and school_type and school_admin and school_email:
                st.success(f"「{school_name}」学校账号已创建，初始密码已发送至 {school_email}")
            else:
                st.warning("带「*」字段为必填项，请补充完整")

    # 5.2 学校组织列表（新增“查看账号”按钮）
    st.markdown("""
    <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
        <h3 style='color:#2E8B57;'>📋 现有学校组织</h3>
    </div>
    """, unsafe_allow_html=True)

    # 展示学校列表（含查看账号功能）
    for sch_id, sch_data in school_accounts.items():
        sch_info = sch_data["org_info"]
        col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])
        col1.write(f"**{sch_info['name']}**（{sch_id}）")
        col2.write(sch_info['type'])
        col3.write(sch_info['admin'])
        col4.write(f"<span style='color:{'green' if sch_info['status']=='正常' else 'red'}'>{sch_info['status']}</span>", unsafe_allow_html=True)

        # 查看账号按钮
        view_btn = col5.button("查看账号", key=f"view_sch_{sch_id}", use_container_width=True)
        # 状态切换按钮
        if sch_info['status'] == "正常":
            if col6.button("禁用", key=f"ban_sch_{sch_id}", use_container_width=True, type="secondary"):
                st.success(f"「{sch_info['name']}」及下属账号已全部禁用")
        else:
            if col6.button("启用", key=f"unban_sch_{sch_id}", use_container_width=True, type="primary"):
                st.success(f"「{sch_info['name']}」及下属账号已全部启用")

        # 点击“查看账号”后展示具体用户列表（区分教师/学生角色）
        if view_btn:
            st.markdown(f"""
            <div style='border:1px solid #d4eedd; border-radius:10px; padding:15px; margin:10px 0; background-color:#f9fbf9;'>
                <h4 style='color:#2E8B57; margin-top:0;'>{sch_info['name']} - 具体用户账号（共{len(sch_data['user_accounts'])}个）</h4>
            </div>
            """, unsafe_allow_html=True)

            # 按角色分类展示（管理员→教师→学生）
            admins = [user for user in sch_data['user_accounts'] if user['role'] == "学校管理员"]
            teachers = [user for user in sch_data['user_accounts'] if user['role'] == "教师"]
            students = [user for user in sch_data['user_accounts'] if user['role'] == "学生"]

            # 展示管理员账号
            if admins:
                st.subheader("👑 学校管理员账号")
                for user in admins:
                    with st.expander(f"🆔 {user['user_id']} | {user['name']}", expanded=False):
                        col_a, col_b, col_c = st.columns(3)
                        col_a.write(f"**邮箱**：{user['email']}")
                        col_a.write(f"**电话**：{user.get('phone', '未填写')}")
                        col_b.write(f"**加入时间**：{user['join_date']}")
                        col_b.write(f"**账号状态**：<span style='color:{'green' if user['status']=='活跃' else 'red'}'>{user['status']}</span>", unsafe_allow_html=True)
                        col_c.write(f"**角色权限**：{user['role']}")

                        # 单个账号状态切换
                        if user['status'] == "活跃":
                            if st.button("禁用该账号", key=f"ban_user_{user['user_id']}", use_container_width=True, type="secondary"):
                                st.success(f"「{user['name']}」（管理员）账号已禁用")
                        else:
                            if st.button("启用该账号", key=f"unban_user_{user['user_id']}", use_container_width=True, type="primary"):
                                st.success(f"「{user['name']}」（管理员）账号已启用")

            # 展示教师账号
            if teachers:
                st.subheader("👨‍🏫 教师账号")
                for user in teachers:
                    with st.expander(f"🆔 {user['user_id']} | {user['name']}", expanded=False):
                        col_a, col_b, col_c = st.columns(3)
                        col_a.write(f"**邮箱**：{user['email']}")
                        col_a.write(f"**教授科目**：{user.get('subject', '未填写')}")
                        col_b.write(f"**加入时间**：{user['join_date']}")
                        col_b.write(f"**账号状态**：<span style='color:{'green' if user['status']=='活跃' else 'red'}'>{user['status']}</span>", unsafe_allow_html=True)
                        col_c.write(f"**角色权限**：{user['role']}")

                        if user['status'] == "活跃":
                            if st.button("禁用该账号", key=f"ban_user_{user['user_id']}", use_container_width=True, type="secondary"):
                                st.success(f"「{user['name']}」（{user['subject']}教师）账号已禁用")
                        else:
                            if st.button("启用该账号", key=f"unban_user_{user['user_id']}", use_container_width=True, type="primary"):
                                st.success(f"「{user['name']}」（{user['subject']}教师）账号已启用")

            # 展示学生账号
            if students:
                st.subheader("🎓 学生账号")
                for user in students:
                    with st.expander(f"🆔 {user['user_id']} | {user['name']}", expanded=False):
                        col_a, col_b, col_c = st.columns(3)
                        col_a.write(f"**邮箱**：{user['email']}")
                        col_a.write(f"**年级班级**：{user['grade']}{user['class']}")
                        col_b.write(f"**加入时间**：{user['join_date']}")
                        col_b.write(f"**账号状态**：<span style='color:{'green' if user['status']=='活跃' else 'red'}'>{user['status']}</span>", unsafe_allow_html=True)
                        col_c.write(f"**角色权限**：{user['role']}")

                        if user['status'] == "活跃":
                            if st.button("禁用该账号", key=f"ban_user_{user['user_id']}", use_container_width=True, type="secondary"):
                                st.success(f"「{user['name']}」（{user['grade']}{user['class']}）学生账号已禁用")
                        else:
                            if st.button("启用该账号", key=f"unban_user_{user['user_id']}", use_container_width=True, type="primary"):
                                st.success(f"「{user['name']}」（{user['grade']}{user['class']}）学生账号已启用")

# ---------------------- 6. 页脚信息 ----------------------
st.divider()
st.markdown("""
    <div style='text-align:center; color:#666; font-size:0.9rem;'>
        © 2024 Komodo Hub | 由 Yayasan Komodo 运营 | 保护印尼濒危物种，人人有责
    </div>
""", unsafe_allow_html=True)