import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

# ---------------------- 1. 页面基础配置 ----------------------
st.set_page_config(
    page_title="Komodo Hub - 印尼濒危物种保护平台",
    page_icon="🐉",
    layout="wide"
)

# ---------------------- 2. 顶部导航栏（含右上角登录状态） ----------------------
with st.container():
    header_col1, header_col2 = st.columns([4, 1])

    # 左侧：平台标题与品牌
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

    # 右侧：登录状态显示
    with header_col2:
        st.markdown("""
            <div style='text-align: right; padding-top: 20px;'>
                <span style='color:#2E8B57; font-weight: bold;'>👤 已登录</span>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# ---------------------- 3. 角色选择标签 ----------------------
selected_role = option_menu(
    menu_title=None,
    options=["社区管理员"],
    icons=["person", "shield"],
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

# ---------------------- 4. 社区成员界面 ----------------------
if selected_role == "社区成员":
    st.markdown("<h2 style='color:#333;'>社区成员中心</h2>", unsafe_allow_html=True)
    st.write("欢迎参与社区保护行动，您可以提交内容和管理个人资料：")

    # 功能标签页
    member_tab = option_menu(
        menu_title=None,
        options=["提交内容", "个人资料管理"],
        icons=["file-earmark-text", "person-circle"],
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

    # 提交内容界面
    if member_tab == "提交内容":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>📝 内容提交</h3>
            <p>分享您的保护经验、研究成果或物种目击信息</p>
        </div>
        """, unsafe_allow_html=True)

        # 内容类型选择
        content_type = st.radio("选择内容类型", ["保护文章", "物种目击报告"], horizontal=True)

        if content_type == "保护文章":
            with st.form("article_form"):
                col1, col2 = st.columns(2)
                with col1:
                    title = st.text_input("文章标题")
                    category = st.selectbox("文章分类", ["物种介绍", "保护技术", "社区行动", "政策解读", "其他"])

                with col2:
                    community = st.selectbox("所属社区", ["#SaveOurAnimals", "苏门答腊保护联盟", "巴厘岛鸟类保护社区",
                                                          "爪哇犀牛守护者"])
                    is_public = st.checkbox("允许公开分享（非注册用户可浏览）", value=True)

                content = st.text_area("文章内容", height=200, placeholder="请输入您的文章内容...")
                attachments = st.file_uploader("上传图片/附件（可选）", accept_multiple_files=True)

                submit_col1, submit_col2 = st.columns([1, 5])
                with submit_col1:
                    submitted = st.form_submit_button("提交审核", use_container_width=True)
                    if submitted:
                        st.success("文章已提交至管理员审核，感谢您的贡献！")

        else:  # 物种目击报告
            with st.form("sighting_form"):
                col1, col2 = st.columns(2)
                with col1:
                    species = st.text_input("物种名称", placeholder="例如：爪哇犀牛")
                    sighting_date = st.date_input("目击日期", value=datetime.now())
                    location = st.text_input("目击地点", placeholder="尽可能详细的位置信息")

                with col2:
                    community = st.selectbox("所属社区", ["#SaveOurAnimals", "苏门答腊保护联盟", "巴厘岛鸟类保护社区",
                                                          "爪哇犀牛守护者"])
                    quantity = st.number_input("数量", min_value=1, value=1)
                    gps_coords = st.text_input("GPS坐标（可选）", placeholder="例如：-6.2088, 106.8456")

                description = st.text_area("目击详情", height=150,
                                           placeholder="请描述您看到的情况，包括物种行为、周围环境等...")
                photos = st.file_uploader("上传现场照片（可选）", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

                submit_col1, submit_col2 = st.columns([1, 5])
                with submit_col1:
                    submitted = st.form_submit_button("提交报告", use_container_width=True)
                    if submitted:
                        st.success("目击报告已提交，管理员将尽快审核发布！")

    # 个人资料管理界面
    else:
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>👤 个人资料管理</h3>
            <p>维护您的社区个人信息和偏好设置</p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("profile_form"):
            col1, col2 = st.columns(2, gap="large")

            with col1:
                st.subheader("基本信息")
                full_name = st.text_input("姓名", value="安达")
                nickname = st.text_input("社区昵称", value="anda_nature")
                email = st.text_input("电子邮箱", value="anda@example.com")
                phone = st.text_input("联系电话", value="+62 812-xxxx-xxxx")

            with col2:
                st.subheader("社区信息")
                joined_communities = st.multiselect(
                    "已加入社区",
                    ["#SaveOurAnimals", "苏门答腊保护联盟", "巴厘岛鸟类保护社区", "爪哇犀牛守护者"],
                    default=["#SaveOurAnimals"]
                )
                interests = st.multiselect(
                    "关注物种",
                    ["爪哇犀牛", "苏门答腊虎", "巴厘岛八哥", "苏门答腊象", "其他"],
                    default=["爪哇犀牛", "苏门答腊象"]
                )
                notification = st.checkbox("接收社区活动通知", value=True)

            st.subheader("个人简介")
            bio = st.text_area("介绍一下自己（保护经历、专业背景等）",
                               height=100,
                               value="我是一名野生动物爱好者，从事保护志愿者工作5年，主要关注爪哇犀牛的保护。")

            submit_col1, submit_col2 = st.columns([1, 5])
            with submit_col1:
                updated = st.form_submit_button("保存修改", use_container_width=True)
                if updated:
                    st.success("个人资料已更新！")

# ---------------------- 5. 社区管理员界面 ----------------------
else:
    st.markdown("<h2 style='color:#333;'>社区管理中心</h2>", unsafe_allow_html=True)
    st.write("作为社区管理员，您可以审核内容、管理社区资源和成员：")

    # 管理功能标签页
    admin_tab = option_menu(
        menu_title=None,
        options=["内容审核", "社区图书馆", "成员管理", "公开信息维护"],
        icons=["check-circle", "book", "people", "file-text"],
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

    # 内容审核界面
    if admin_tab == "内容审核":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>🔍 内容审核</h3>
            <p>审核社区成员提交的文章和目击报告</p>
        </div>
        """, unsafe_allow_html=True)

        # 待审核内容列表
        pending_items = [
            {
                "id": "A001",
                "type": "文章",
                "title": "爪哇犀牛保护新策略",
                "submitter": "巴古斯",
                "date": "2024-10-27",
                "status": "待审核"
            },
            {
                "id": "S045",
                "type": "目击报告",
                "title": "苏门答腊虎目击记录",
                "submitter": "莱娜",
                "date": "2024-10-28",
                "status": "待审核"
            },
            {
                "id": "A002",
                "type": "文章",
                "title": "社区参与保护的成功案例",
                "submitter": "安达",
                "date": "2024-10-28",
                "status": "待审核"
            }
        ]

        # 筛选选项
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            filter_type = st.selectbox("内容类型", ["全部", "文章", "目击报告"])
        with filter_col2:
            filter_status = st.selectbox("状态", ["全部", "待审核", "已通过", "已拒绝"])

        # 显示待审核内容
        for item in pending_items:
            with st.expander(f"{item['type']} #{item['id']}: {item['title']}（{item['submitter']} · {item['date']}）"):
                st.write("**提交人信息**：社区成员，加入时间2023-05-12，贡献值120")
                st.write("**内容预览**：这是一份关于...（内容预览）")

                if item["type"] == "目击报告":
                    st.write("**附加信息**：包含2张现场照片，GPS坐标已验证")

                # 审核操作按钮
                col_approve, col_reject, col_more = st.columns([1, 1, 3])
                with col_approve:
                    if st.button("通过", key=f"approve_{item['id']}", use_container_width=True):
                        st.success(f"{item['type']}已通过审核！")
                with col_reject:
                    if st.button("拒绝", key=f"reject_{item['id']}", use_container_width=True):
                        reason = st.text_input("拒绝原因", key=f"reason_{item['id']}")
                        if reason:
                            st.success(f"{item['type']}已拒绝，原因：{reason}")

    # 社区图书馆管理界面
    elif admin_tab == "社区图书馆":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>📚 社区图书馆管理</h3>
            <p>管理社区知识库资源，包括分类和访问权限设置</p>
        </div>
        """, unsafe_allow_html=True)

        # 图书馆统计
        stats_col1, stats_col2, stats_col3 = st.columns(3)
        with stats_col1:
            st.metric("总资源数", "128")
        with stats_col2:
            st.metric("文章数量", "86")
        with stats_col3:
            st.metric("报告数量", "42")

        # 资源分类管理
        st.subheader("资源分类管理")
        with st.expander("现有分类", expanded=True):
            categories = [
                {"name": "物种介绍", "count": 32, "public": "是"},
                {"name": "保护技术", "count": 24, "public": "是"},
                {"name": "社区行动", "count": 18, "public": "是"},
                {"name": "政策解读", "count": 12, "public": "是"},
                {"name": "内部资料", "count": 42, "public": "否"}
            ]

            for cat in categories:
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                col1.write(cat["name"])
                col2.write(f"{cat['count']} 项")
                col3.write(cat["public"])
                col4.button("编辑", key=f"edit_cat_{cat['name']}", use_container_width=True)

        # 添加新分类
        with st.form("new_category"):
            st.subheader("添加新分类")
            col1, col2 = st.columns(2)
            cat_name = st.text_input("分类名称")
            is_public = st.checkbox("允许公开访问", value=True)
            submit = st.form_submit_button("添加分类")
            if submit:
                st.success(f"新分类 '{cat_name}' 已创建！")

    # 成员管理界面
    elif admin_tab == "成员管理":
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>👥 社区成员管理</h3>
            <p>审批新成员注册申请，管理现有成员信息</p>
        </div>
        """, unsafe_allow_html=True)

        # 成员管理标签
        member_management_tab = st.tabs(["注册审批", "现有成员"])

        with member_management_tab[0]:
            st.subheader("待审批注册申请")
            applications = [
                {"name": "里基", "email": "ricky@example.com", "reason": "野生动物摄影师，希望分享照片和观察记录",
                 "date": "2024-10-28"},
                {"name": "米拉", "email": "mira@example.com", "reason": "环境科学学生，想参与保护研究",
                 "date": "2024-10-28"},
                {"name": "约瑟夫", "email": "joseph@example.com", "reason": "公园巡护员，希望提交官方数据",
                 "date": "2024-10-29"}
            ]

            for app in applications:
                with st.expander(f"{app['name']} ({app['email']})"):
                    st.write(f"**申请日期**：{app['date']}")
                    st.write(f"**加入原因**：{app['reason']}")

                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("批准", key=f"approve_{app['email']}", use_container_width=True):
                            st.success(f"已批准 {app['name']} 的加入申请！")
                    with col2:
                        if st.button("拒绝", key=f"deny_{app['email']}", use_container_width=True):
                            st.success(f"已拒绝 {app['name']} 的加入申请！")

        with member_management_tab[1]:
            st.subheader("现有社区成员")
            st.write("总成员数：142 人")

            # 搜索和筛选
            search_col1, search_col2 = st.columns(2)
            with search_col1:
                search = st.text_input("搜索成员")
            with search_col2:
                sort_by = st.selectbox("排序方式", ["贡献值", "加入时间", "姓名"])

            # 成员列表（示例）
            members = [
                {"name": "安达", "role": "成员", "join_date": "2023-01-15", "contributions": 48, "status": "活跃"},
                {"name": "巴古斯", "role": "管理员", "join_date": "2022-11-10", "contributions": 127, "status": "活跃"},
                {"name": "莱娜", "role": "成员", "join_date": "2023-03-22", "contributions": 36, "status": "活跃"},
                {"name": "哈迪", "role": "成员", "join_date": "2023-05-30", "contributions": 18, "status": "不活跃"}
            ]

            for member in members:
                cols = st.columns([2, 1, 1, 1, 1, 1])
                cols[0].write(member["name"])
                cols[1].write(member["role"])
                cols[2].write(member["join_date"])
                cols[3].write(member["contributions"])
                cols[4].write(member["status"])
                cols[5].button("详情", key=f"detail_{member['name']}", use_container_width=True)

    # 公开信息维护界面
    else:
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:20px; margin-bottom:20px;'>
            <h3 style='color:#2E8B57;'>📢 社区公开信息维护</h3>
            <p>管理社区公告、活动信息和保护动态</p>
        </div>
        """, unsafe_allow_html=True)

        # 公告管理
        st.subheader("社区公告")
        with st.form("announcement_form"):
            announcement_title = st.text_input("公告标题")
            announcement_content = st.text_area("公告内容", height=150)
            is_important = st.checkbox("置顶重要公告")
            announce_col1, announce_col2 = st.columns([1, 5])
            with announce_col1:
                发布 = st.form_submit_button("发布公告", use_container_width=True)
                if 发布:
                    st.success("公告已发布！")

    # 现有公告列表
    st.subheader("现有公告")
    announcements = [
        {"title": "11月社区保护行动招募", "date": "2024-10-25", "author": "巴古斯", "pinned": True},
        {"title": "社区贡献奖励计划更新", "date": "2024-10-20", "author": "安达", "pinned": False},
        {"title": "新成员指南发布", "date": "2024-10-15", "author": "莱娜", "pinned": False}
    ]

    for ann in announcements:
        pin_label = "📌 " if ann["pinned"] else ""
        with st.expander(f"{pin_label}{ann['title']}（{ann['date']}）"):
            st.write(f"**发布人**：{ann['author']}")
            st.write("公告内容预览...")
            col1, col2 = st.columns(2)
            with col1:
                st.button("编辑", key=f"edit_ann_{ann['title']}", use_container_width=True)
            with col2:
                if ann["pinned"]:
                    st.button("取消置顶", key=f"unpin_ann_{ann['title']}", use_container_width=True)
                else:
                    st.button("置顶", key=f"pin_ann_{ann['title']}", use_container_width=True)

# ---------------------- 6. 页脚信息 ----------------------
st.divider()
st.markdown("""
    <div style='text-align:center; color:#666; font-size:0.9rem;'>
        © 2024 Komodo Hub | 由 Yayasan Komodo 运营 | 保护印尼濒危物种，人人有责
    </div>
""", unsafe_allow_html=True)