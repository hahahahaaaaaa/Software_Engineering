import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, date
import random
import string

# ---------------------- 1. 页面基础配置 ----------------------
st.set_page_config(
    page_title="Komodo Hub - 印尼濒危物种保护平台",
    page_icon="🐉",
    layout="wide"
)

# ---------------------- 2. 顶部导航栏（含右上角登录状态） ----------------------
with st.container():
    header_col1, header_col2 = st.columns([4, 1])

    # 左侧：平台标题与品牌（居中加粗放大）
    with header_col1:
        st.markdown("""
            <h1 style='text-align: center; color:#2E8B57; font-weight: bold; font-size: 4.5rem;'>
                🐉 Komodo Hub
            </h1>
        """, unsafe_allow_html=True)
        st.markdown("""
            <p style='text-align: center; color:#666; font-weight: bold; font-size: 1.2rem;'>
                印尼濒危物种保护数字化社区平台
            </p>
        """, unsafe_allow_html=True)

    # 右侧：登录状态（学校角色专属）
    with header_col2:
        st.markdown("""
            <div style='text-align: right; padding-top: 20px;'>
                <span style='color:#2E8B57; font-weight: bold;'>👤 学校账号已登录</span>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# ---------------------- 3. 学校角色选择标签 ----------------------
selected_school_role = option_menu(
    menu_title=None,
    options=["学生", "学校教师", "学校管理员"],
    icons=["graduation-cap", "chalkboard-user", "user-shield"],
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

# ---------------------- 4. 学生界面 ----------------------
if selected_school_role == "学生":
    # 标题居中
    st.markdown("""
        <h2 style='text-align: center; color:#333;'>学生中心</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center;'>参与保护项目、提交作业与报告，管理个人账号</p>
    """, unsafe_allow_html=True)

    # 学生功能子标签
    student_tab = option_menu(
        menu_title=None,
        options=["保护项目", "提交作业/报告", "个人账号设置"],
        icons=["clipboard-check", "file-upload", "gear"],
        orientation="horizontal",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f9f9f9"},
            "icon": {"color": "#2E8B57", "font-size": "16px"},
            "nav-link": {
                "font-size": "11px",
                "padding": "8px 15px",
                "color": "#555",
                "--hover-color": "#e6f7ef"
            },
            "nav-link-selected": {"background-color": "#d4eedd", "color": "#2E8B57"},
        }
    )

    # 4.1 保护项目界面
    if student_tab == "保护项目":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>📋 学校定制保护项目</h3>
            <p>参与老师布置的保护主题项目，查看项目要求与进度</p>
        </div>
        """, unsafe_allow_html=True)

        # 项目列表
        projects = [
            {
                "name": "爪哇犀牛栖息地调查",
                "teacher": "李老师",
                "deadline": "2024-11-15",
                "status": "进行中",
                "progress": 60
            },
            {
                "name": "校园鸟类观察日记",
                "teacher": "王老师",
                "deadline": "2024-11-30",
                "status": "未开始",
                "progress": 0
            },
            {
                "name": "保护海报设计大赛",
                "teacher": "张老师",
                "deadline": "2024-11-10",
                "status": "已提交",
                "progress": 100
            }
        ]

        for proj in projects:
            with st.expander(f"📌 {proj['name']}（{proj['status']}）", expanded=False):
                col1, col2, col3 = st.columns(3)
                col1.write(f"**指导老师**：{proj['teacher']}")
                col2.write(f"**截止日期**：{proj['deadline']}")
                col3.write(f"**完成进度**：{proj['progress']}%")

                st.progress(proj['progress'], text=f"进度：{proj['progress']}%")
                if proj['status'] == "进行中":
                    if st.button("查看项目详情", key=f"proj_detail_{proj['name']}", use_container_width=True):
                        st.info(f"{proj['name']}要求：1. 收集3个栖息地样本数据 2. 撰写500字分析报告 3. 制作数据图表")

    # 4.2 提交作业/报告界面
    elif student_tab == "提交作业/报告":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>📤 提交作业/目击报告</h3>
            <p>选择提交类型，上传相关文件或填写报告内容</p>
        </div>
        """, unsafe_allow_html=True)

        # 提交类型选择
        submit_type = st.radio("选择提交类型", ["课程作业", "物种目击报告"], horizontal=True)

        if submit_type == "课程作业":
            with st.form("homework_form"):
                col1, col2 = st.columns(2)
                with col1:
                    proj_name = st.selectbox("关联项目", ["爪哇犀牛栖息地调查", "校园鸟类观察日记", "保护海报设计大赛"])
                    submit_date = st.date_input("提交日期", value=date.today())
                with col2:
                    teacher = st.selectbox("提交给", ["李老师", "王老师", "张老师"])
                    homework_desc = st.text_input("作业描述", placeholder="简单说明作业内容")

                # 文件上传
                homework_file = st.file_uploader("上传作业文件（支持PDF/Word/图片）",
                                                 type=["pdf", "docx", "jpg", "png"])
                notes = st.text_area("补充说明（可选）", height=80, placeholder="如有特殊说明可在此填写")

                submit_col1, submit_col2 = st.columns([1, 5])
                with submit_col1:
                    submitted = st.form_submit_button("提交作业", use_container_width=True)
                    if submitted and homework_file:
                        st.success(f"已成功提交《{proj_name}》作业至{teacher}，等待批改！")
                    elif submitted and not homework_file:
                        st.warning("请先上传作业文件再提交")

        else:  # 物种目击报告
            with st.form("student_sighting_form"):
                col1, col2 = st.columns(2)
                with col1:
                    species = st.text_input("物种名称", placeholder="例如：巴厘岛八哥")
                    sighting_date = st.date_input("目击日期", value=date.today())
                    location = st.text_input("目击地点", placeholder="例如：学校后花园/家附近公园")
                with col2:
                    grade = st.selectbox("年级", ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"])
                    quantity = st.number_input("数量", min_value=1, value=1)
                    is_teacher_verify = st.checkbox("是否经老师现场确认", value=False)

                description = st.text_area("目击详情", height=120, placeholder="描述看到的物种特征、行为、周围环境等")
                photos = st.file_uploader("上传现场照片（可选）", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

                submit_col1, submit_col2 = st.columns([1, 5])
                with submit_col1:
                    submitted = st.form_submit_button("提交报告", use_container_width=True)
                    if submitted:
                        st.success("目击报告已提交，学校管理员将审核后发布！")

    # 4.3 个人账号设置界面
    else:
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>👤 个人账号设置</h3>
            <p>修改个人信息，上传个性化头像</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("student_profile_form"):
            # 头像上传与预览
            col1, col2 = st.columns([1, 3])
            with col1:
                st.subheader("头像预览")
                # 初始默认头像
                st.markdown("""
                    <div style='width:120px; height:120px; border-radius:50%; background-color:#e6f7ef; 
                               display:flex; align-items:center; justify-content:center; margin-bottom:10px;'>
                        <span style='font-size:30px; color:#2E8B57;'>👧</span>
                    </div>
                """, unsafe_allow_html=True)
                avatar = st.file_uploader("上传新头像", type=["jpg", "jpeg", "png"])
                if avatar:
                    st.success("头像已上传，保存后生效！")

            with col2:
                st.subheader("基本信息")
                full_name = st.text_input("真实姓名", value="张三")
                student_id = st.text_input("学号", value="2024001", disabled=True)  # 学号不可修改
                grade = st.selectbox("年级", ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"], index=2)
                class_num = st.selectbox("班级", ["1班", "2班", "3班", "4班"], index=1)
                email = st.text_input("家长邮箱（用于接收通知）", value="parent@example.com")

            # 密码修改（可选）
            st.subheader("密码修改（可选）")
            old_pwd = st.text_input("原密码", type="password")
            new_pwd = st.text_input("新密码", type="password")
            confirm_pwd = st.text_input("确认新密码", type="password")

            submit_col1, submit_col2 = st.columns([1, 5])
            with submit_col1:
                saved = st.form_submit_button("保存修改", use_container_width=True)
                if saved:
                    if new_pwd and new_pwd != confirm_pwd:
                        st.warning("两次输入的新密码不一致，请重新输入！")
                    else:
                        st.success("个人账号信息已保存！")

# ---------------------- 5. 学校教师界面 ----------------------
elif selected_school_role == "学校教师":
    # 标题居中
    st.markdown("""
        <h2 style='text-align: center; color:#333;'>学校教师中心</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center;'>设计课程活动，评估学生提交的作业与成果</p>
    """, unsafe_allow_html=True)

    # 教师功能子标签
    teacher_tab = option_menu(
        menu_title=None,
        options=["课程活动设计", "学生成果评估", "我的班级"],
        icons=["pen-ruler", "check-double", "users"],
        orientation="horizontal",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f9f9f9"},
            "icon": {"color": "#2E8B57", "font-size": "16px"},
            "nav-link": {
                "font-size": "11px",
                "padding": "8px 15px",
                "color": "#555",
                "--hover-color": "#e6f7ef"
            },
            "nav-link-selected": {"background-color": "#d4eedd", "color": "#2E8B57"},
        }
    )

    # 5.1 课程活动设计界面
    if teacher_tab == "课程活动设计":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>🎯 设计课程活动</h3>
            <p>创建与保护主题相关的课程活动，设置提交要求与截止日期</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("activity_design_form"):
            st.subheader("活动基本信息")
            col1, col2 = st.columns(2)
            with col1:
                activity_name = st.text_input("活动名称", placeholder="例如：校园植物多样性调查")
                activity_type = st.selectbox("活动类型", ["调查类", "报告类", "设计类", "实践类"])
                grade_range = st.multiselect("适用年级", ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"],
                                             default=["三年级", "四年级"])
            with col2:
                start_date = st.date_input("开始日期", value=date.today())
                end_date = st.date_input("截止日期", value=datetime(2024, 11, 30).date())
                max_score = st.number_input("满分分值", min_value=50, max_value=100, value=80)

            st.subheader("活动要求")
            activity_desc = st.text_area("活动描述", height=120, placeholder="说明活动目的、内容与具体要求")
            materials = st.text_input("所需材料", placeholder="例如：调查表、相机、笔记本")
            submit_require = st.text_area("提交要求", height=80,
                                          placeholder="说明学生需提交的成果形式，如报告、照片、视频等")

            # 附件（如活动模板）
            template_file = st.file_uploader("上传活动模板（可选）", type=["pdf", "docx", "xlsx"])

            submit_col1, submit_col2 = st.columns([1, 5])
            with submit_col1:
                created = st.form_submit_button("创建活动", use_container_width=True)
                if created and activity_name:
                    st.success(f"《{activity_name}》课程活动已创建，适用年级：{', '.join(grade_range)}")
                elif created and not activity_name:
                    st.warning("请先填写活动名称再创建！")

    # 5.2 学生成果评估界面
    elif teacher_tab == "学生成果评估":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>📝 学生成果评估</h3>
            <p>查看学生提交的作业/报告，评分并添加评语</p>
        </div>
        """, unsafe_allow_html=True)

        # 筛选条件
        filter_col1, filter_col2, filter_col3 = st.columns(3)
        with filter_col1:
            eval_activity = st.selectbox("选择活动", ["爪哇犀牛栖息地调查", "校园鸟类观察日记", "保护海报设计大赛"])
        with filter_col2:
            eval_grade = st.selectbox("选择年级", ["全部", "三年级", "四年级", "五年级"])
        with filter_col3:
            eval_status = st.selectbox("提交状态", ["全部", "已提交", "未提交", "已评分"])

        # 待评估列表
        submissions = [
            {
                "student": "张三",
                "grade": "三年级",
                "activity": "爪哇犀牛栖息地调查",
                "submit_time": "2024-10-28 14:30",
                "status": "已提交",
                "file": "张三_栖息地调查.pdf"
            },
            {
                "student": "李四",
                "grade": "三年级",
                "activity": "爪哇犀牛栖息地调查",
                "submit_time": "2024-10-29 09:15",
                "status": "已提交",
                "file": "李四_犀牛报告.docx"
            },
            {
                "student": "王五",
                "grade": "三年级",
                "activity": "爪哇犀牛栖息地调查",
                "submit_time": "",
                "status": "未提交",
                "file": ""
            }
        ]

        for sub in submissions:
            with st.expander(f"🎓 {sub['student']} - {sub['activity']}（{sub['status']}）", expanded=False):
                col1, col2, col3 = st.columns(3)
                col1.write(f"**年级**：{sub['grade']}")
                col2.write(f"**提交时间**：{sub['submit_time'] if sub['submit_time'] else '未提交'}")
                col3.write(f"**状态**：{sub['status']}")

                if sub['status'] == "已提交":
                    st.write(f"**提交文件**：{sub['file']}")
                    st.download_button("下载文件", data=b"example content", file_name=sub['file'],
                                       use_container_width=True)

                    # 评分区域
                    st.subheader("评分与评语")
                    score_col1, score_col2 = st.columns([1, 3])
                    with score_col1:
                        score = st.slider("评分", 0, 80, 60)
                    with score_col2:
                        comment = st.text_area("评语", height=60, placeholder="请输入对该作业的评语...")

                    if st.button("提交评分", key=f"score_{sub['student']}", use_container_width=True):
                        st.success(f"已完成对{sub['student']}的评分：{score}分")

    # 5.3 我的班级界面
    else:
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>👨‍👩‍👧‍👦 我的班级</h3>
            <p>查看所教班级学生列表及参与情况统计</p>
        </div>
        """, unsafe_allow_html=True)

        # 班级统计
        stats_col1, stats_col2, stats_col3 = st.columns(3)
        with stats_col1:
            st.metric("总学生数", "45")
        with stats_col2:
            st.metric("活跃学生数", "38")
        with stats_col3:
            st.metric("平均完成率", "85%")

        # 班级选择
        class_selected = st.selectbox("选择班级", ["三年级1班", "三年级2班", "四年级1班"])

        # 学生列表
        st.subheader(f"{class_selected} 学生列表")
        students = [
            {"name": "张三", "id": "2024001", "progress": 100, "status": "活跃"},
            {"name": "李四", "id": "2024002", "progress": 80, "status": "活跃"},
            {"name": "王五", "id": "2024003", "progress": 60, "status": "一般"},
            {"name": "赵六", "id": "2024004", "progress": 30, "status": "不活跃"},
            {"name": "钱七", "id": "2024005", "progress": 90, "status": "活跃"}
        ]

        for student in students:
            cols = st.columns([2, 1, 1, 1, 1])
            cols[0].write(student["name"])
            cols[1].write(student["id"])
            cols[2].write(f"{student['progress']}%")
            cols[3].write(student["status"])
            cols[4].button("详情", key=f"student_{student['id']}", use_container_width=True)

# ---------------------- 6. 学校管理员界面 ----------------------
else:
    # 标题居中
    st.markdown("""
        <h2 style='text-align: center; color:#333;'>学校管理中心</h2>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align: center;'>管理学校订阅、账号与访问权限设置</p>
    """, unsafe_allow_html=True)

    # 管理员功能子标签
    admin_tab = option_menu(
        menu_title=None,
        options=["学校订阅管理", "账号注册", "访问码管理", "公开范围设置"],
        icons=["credit-card", "person-plus", "key", "eye-slash"],
        orientation="horizontal",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f9f9f9"},
            "icon": {"color": "#2E8B57", "font-size": "16px"},
            "nav-link": {
                "font-size": "11px",
                "padding": "8px 15px",
                "color": "#555",
                "--hover-color": "#e6f7ef"
            },
            "nav-link-selected": {"background-color": "#d4eedd", "color": "#2E8B57"},
        }
    )

    # 6.1 学校订阅管理界面
    if admin_tab == "学校订阅管理":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>💳 学校订阅管理</h3>
            <p>查看当前订阅状态，管理订阅计划与付款信息</p>
        </div>
        """, unsafe_allow_html=True)

        # 当前订阅信息
        st.subheader("当前订阅信息")
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <div style='display: flex; justify-content: space-between; flex-wrap: wrap;'>
                <div>
                    <h4 style='margin-top:0; color:#2E8B57;'>教育机构高级版</h4>
                    <p>包含全部教育资源与管理功能</p>
                    <p>最多支持100名教师账号，500名学生账号</p>
                </div>
                <div style='text-align: right;'>
                    <p>订阅到期日：2025-06-30</p>
                    <p>状态：<span style='color:green; font-weight:bold;'>活跃</span></p>
                    <button style='background-color:#2E8B57; color:white; border:none; padding:8px 15px; border-radius:5px; cursor:pointer;'>
                        续费
                    </button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 订阅历史
        st.subheader("订阅历史记录")
        history = [
            {"period": "2024-07-01 至 2025-06-30", "plan": "教育机构高级版", "amount": "Rp 2,500,000",
             "status": "已付款"},
            {"period": "2023-07-01 至 2024-06-30", "plan": "教育机构标准版", "amount": "Rp 1,800,000",
             "status": "已付款"}
        ]

        for h in history:
            with st.expander(f"{h['period']} - {h['plan']}", expanded=False):
                col1, col2, col3 = st.columns(3)
                col1.write(f"**金额**：{h['amount']}")
                col2.write(f"**状态**：{h['status']}")
                col3.write(f"**付款日期**：{h['period'].split(' 至 ')[0]}")
                st.button("查看发票", key=f"invoice_{h['period']}", use_container_width=True)

    # 6.2 账号注册界面
    elif admin_tab == "账号注册":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>👤 账号注册管理</h3>
            <p>为教师和学生创建账号，管理现有账号状态</p>
        </div>
        """, unsafe_allow_html=True)

        # 账号类型选择
        account_type = st.radio("选择账号类型", ["教师账号", "学生账号"], horizontal=True)

        if account_type == "教师账号":
            with st.form("teacher_account_form"):
                st.subheader("创建教师账号")
                col1, col2 = st.columns(2)
                with col1:
                    teacher_name = st.text_input("教师姓名")
                    teacher_email = st.text_input("电子邮箱")
                    teacher_subject = st.text_input("教授科目")
                with col2:
                    teacher_id = st.text_input("教师工号")
                    department = st.selectbox("所属部门", ["生物系", "地理系", "环境科学系", "其他"])
                    is_admin = st.checkbox("授予教研组管理员权限")

                # 初始密码设置
                auto_gen_pwd = st.checkbox("自动生成初始密码", value=True)
                if not auto_gen_pwd:
                    init_pwd = st.text_input("设置初始密码", type="password")
                    confirm_pwd = st.text_input("确认初始密码", type="password")

                submit_col1, submit_col2 = st.columns([1, 5])
                with submit_col1:
                    created = st.form_submit_button("创建账号", use_container_width=True)
                    if created and teacher_name and teacher_email:
                        st.success(f"已成功创建{teacher_name}的教师账号，初始密码将发送至邮箱！")

            # 现有教师账号列表
            st.subheader("现有教师账号")
            teachers = [
                {"name": "李老师", "id": "T001", "email": "li@school.com", "status": "活跃"},
                {"name": "王老师", "id": "T002", "email": "wang@school.com", "status": "活跃"},
                {"name": "张老师", "id": "T003", "email": "zhang@school.com", "status": "禁用"}
            ]

            for t in teachers:
                cols = st.columns([2, 1, 2, 1, 1])
                cols[0].write(t["name"])
                cols[1].write(t["id"])
                cols[2].write(t["email"])
                cols[3].write(t["status"])
                cols[4].button("编辑", key=f"edit_teacher_{t['id']}", use_container_width=True)

        else:  # 学生账号
            with st.form("student_batch_form"):
                st.subheader("学生账号创建")
                col1, col2 = st.columns(2)
                with col1:
                    grade = st.selectbox("年级", ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"])
                    class_num = st.selectbox("班级", ["1班", "2班", "3班", "4班"])
                    student_count = st.number_input("创建数量", min_value=1, max_value=50, value=30)
                with col2:
                    id_prefix = st.text_input("学号前缀", value="2024")
                    generate_access = st.checkbox("同时生成访问码", value=True)
                    send_notify = st.checkbox("发送账号信息至家长", value=True)

                submit_col1, submit_col2 = st.columns([1, 5])
                with submit_col1:
                    created = st.form_submit_button("批量创建", use_container_width=True)
                    if created:
                        st.success(f"已为{grade}{class_num}成功创建{student_count}个学生账号！")

            # 现有学生账号列表（示例）
            st.subheader("学生账号查询")
            search_col1, search_col2 = st.columns(2)
            with search_col1:
                search_stu = st.text_input("搜索学生姓名或学号")
            with search_col2:
                filter_grade = st.selectbox("筛选年级",
                                            ["全部", "一年级", "二年级", "三年级", "四年级", "五年级", "六年级"])

    # 6.3 访问码管理界面
    elif admin_tab == "访问码管理":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>🔑 学生专属访问码</h3>
            <p>生成、查看和管理学生访问码，用于平台登录验证</p>
        </div>
        """, unsafe_allow_html=True)

        # 生成新访问码
        with st.form("access_code_form"):
            col1, col2, col3 = st.columns(3)
            with col1:
                code_grade = st.selectbox("年级", ["一年级", "二年级", "三年级", "四年级", "五年级", "六年级"])
            with col2:
                code_class = st.selectbox("班级", ["1班", "2班", "3班", "4班"])
            with col3:
                code_count = st.number_input("生成数量", min_value=1, max_value=100, value=30)

            submit_col1, submit_col2 = st.columns([1, 5])
            with submit_col1:
                generated = st.form_submit_button("生成访问码", use_container_width=True)
                if generated:
                    st.success(f"已为{code_grade}{code_class}生成{code_count}个访问码！")
                    # 显示生成的示例访问码
                    st.subheader("生成的访问码（前5个）")
                    codes = [''.join(random.choices(string.ascii_uppercase + string.digits, k=8)) for _ in range(5)]
                    for c in codes:
                        st.code(c)
                    st.download_button("下载全部访问码", data="\n".join(codes), file_name="access_codes.txt",
                                       use_container_width=True)

        # 访问码列表
        st.subheader("访问码使用状态")
        code_list = [
            {"code": "A2B3C4D5", "student": "张三", "grade": "三年级", "status": "已使用", "used_date": "2024-10-01"},
            {"code": "E6F7G8H9", "student": "", "grade": "三年级", "status": "未使用", "used_date": ""},
            {"code": "I0J1K2L3", "student": "李四", "grade": "三年级", "status": "已使用", "used_date": "2024-10-05"},
            {"code": "M4N5O6P7", "student": "", "grade": "三年级", "status": "已过期", "used_date": ""},
            {"code": "Q8R9S0T1", "student": "王五", "grade": "三年级", "status": "已使用", "used_date": "2024-10-10"}
        ]

        for code in code_list:
            cols = st.columns([2, 2, 1, 1, 2])
            cols[0].write(code["code"])
            cols[1].write(code["student"] if code["student"] else "未分配")
            cols[2].write(code["grade"])
            cols[3].write(code["status"])
            cols[4].write(code["used_date"] if code["used_date"] else "-")

    # 6.4 公开范围设置界面
    else:
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>🔒 学校公开范围设置</h3>
            <p>控制学校内容的公开范围，保护学生隐私</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("公开范围设置")
        with st.form("privacy_settings_form"):
            # 保护项目公开设置
            st.markdown("### 保护项目与成果")
            project_scope = st.radio(
                "学校保护项目成果的公开范围",
                ["仅校内可见", "平台内学校群组可见", "全平台公开（不含学生个人信息）"],
                index=1
            )

            # 学生作品公开设置
            st.markdown("### 学生作品与报告")
            work_scope = st.radio(
                "学生作业与报告的公开范围",
                ["仅本校师生可见", "经教师审核后可平台内共享", "禁止任何外部共享"],
                index=0
            )

            # 个人信息保护
            st.markdown("### 个人信息保护")
            col1, col2 = st.columns(2)
            with col1:
                st.checkbox("隐藏学生真实姓名（使用匿名或学号）", value=True)
                st.checkbox("限制学生头像上传格式（仅系统头像）", value=False)
            with col2:
                st.checkbox("教师联系方式仅对本校学生可见", value=True)
                st.checkbox("自动模糊学生作品中的面部信息", value=True)

            # 特殊设置
            st.markdown("### 特殊设置")
            public_exceptions = st.text_area(
                "允许全平台公开的内容类型（每行一项）",
                height=80,
                value="• 学校组织的保护活动照片（不含学生）\n• 教师发表的保护教育文章\n• 匿名化的学生优秀作品"
            )

            submit_col1, submit_col2 = st.columns([1, 5])
            with submit_col1:
                saved = st.form_submit_button("保存设置", use_container_width=True)
                if saved:
                    st.success("学校公开范围设置已更新并生效！")

# ---------------------- 7. 页脚信息 ----------------------
st.divider()
st.markdown("""
    <div style='text-align:center; color:#666; font-size:0.9rem;'>
        © 2024 Komodo Hub | 由 Yayasan Komodo 运营 | 保护印尼濒危物种，人人有责
    </div>
""", unsafe_allow_html=True)