import streamlit as st
from streamlit_option_menu import option_menu

# ---------------------- 1. 页面基础配置 ----------------------
st.set_page_config(
    page_title="Komodo Hub - 印尼濒危物种保护平台",
    page_icon="🐉",
    layout="wide"
)

# ---------------------- 2. 顶部导航栏（含右上角登录入口） ----------------------
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
                印尼濒危濒危物种保护数字化社区平台
            </p>
        """, unsafe_allow_html=True)

    # 右侧：登录入口（并排按钮+缩小尺寸）
    with header_col2:
        # 用列布局实现并排显示
        login_col1, login_col2 = st.columns(2, gap="small")  # 缩小列间距

        # 学校登录按钮（缩小尺寸：使用small按钮类型+减少内边距）
        with login_col1:
            if st.button(
                    "🏫 学校登录",
                    key="school_login",
                    use_container_width=True,
                    type="secondary",  # 次要按钮样式，视觉更简洁
                    help="教师/学生账号登录入口"
            ):
                st.info("学校登录：支持教师/学生账号（学生需输入专属访问码）")

        # 社区登录按钮（同上样式）
        with login_col2:
            if st.button(
                    "👥 社区登录",
                    key="community_login",
                    use_container_width=True,
                    type="secondary",
                    help="社区成员/管理员账号登录入口"
            ):
                st.info("社区登录：支持社区成员/管理员账号")

st.divider()

# ---------------------- 3. 网页式标签切换 ----------------------
selected_tab = option_menu(
    menu_title=None,
    options=["非注册用户资源", "社区目击报告"],
    icons=["person", "eye"],
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

# 后续界面内容与之前保持一致...
# ---------------------- 4. 非注册用户资源界面 ----------------------
if selected_tab == "非注册用户资源":
    st.markdown("<h2 style='color:#333;'>公开保护资源</h2>", unsafe_allow_html=True)
    st.write("无需注册即可访问以下资源，助力了解印尼濒危物种保护现状：")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:30px; height:300px; display:flex; flex-direction:column; justify-content:center;'>
            <h3 style='color:#2E8B57;'>📚 公开知识库</h3>
            <p style='margin:20px 0;'>包含：</p>
            <ul>
                <li>社区公开贡献的保护文章、实践案例</li>
                <li>学校分享的保护教育成果（不含学生隐私）</li>
                <li>印尼动物动物保护政策与最佳实践指南</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("进入公开知识库", key="enter_public", use_container_width=True):
            st.success("已进入公开知识库（示例内容：#SaveOurAnimals社区的爪哇犀牛保护手册）")

    with col2:
        st.markdown("""
        <div style='border:1px solid #ddd; border-radius:10px; padding:30px; height:300px; display:flex; flex-direction:column; justify-content:center;'>
            <h3 style='color:#2E8B57;'>🐾 濒危物种知识库</h3>
            <p style='margin:20px 0;'>包含：</p>
            <ul>
                <li>苏门答腊虎、爪哇犀牛等14种濒危物种数据</li>
                <li>2018-2020年物种数量统计与分布地图</li>
                <li>栖息地丧失等威胁因素分析与保护建议</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        if st.button("进入濒危物种知识库", key="enter_endangered", use_container_width=True):
            st.success("已进入濒危濒危物种知识库（示例：苏门答腊虎现存数量<100只，主要威胁为栖息地破坏）")

# ---------------------- 5. 社区目击报告界面 ----------------------
elif selected_tab == "社区目击报告":
    st.markdown("<h2 style='color:#333;'>社区濒危濒危物种物种目击目击报告</h2>", unsafe_allow_html=True)
    st.write("以下为各社区成员提交并审核通过的公开目击记录（非注册用户可浏览）：")

    reports = [
        {
            "id": 1,
            "species": "爪哇犀牛",
            "community": "#SaveOurAnimals社区",
            "date": "2024-06-15",
            "location": "乌戎库隆国家公园",
            "submitter": "安达（社区成员）",
            "content": "今日上午在公园核心区发现1只成年犀牛，携带1只幼崽，活动正常。已记录GPS位置并反馈至公园管理处。",
            "status": "已审核"
        },
        {
            "id": 2,
            "species": "苏门答腊象",
            "community": "苏门答腊保护联盟",
            "date": "2024-06-10",
            "location": "廖内省森林",
            "submitter": "巴古斯（社区管理员）",
            "content": "红外相机拍摄到3头象群，周边有农作物作物受损痕迹，已协调社区与农户建立防护栏。",
            "status": "已审核"
        },
        {
            "id": 3,
            "species": "巴厘岛八哥",
            "community": "巴厘岛鸟类类保护社区",
            "date": "2024-06-05",
            "location": "巴厘岛乌布地区",
            "submitter": "莱娜（社区成员）",
            "content": "在稻田边缘发现5只八哥，近期周边农药使用频繁，存在中毒风险，已呼吁吁农户农户减少减少农药使用。",
            "status": "审核中"
        }
    ]

    for report in reports:
        with st.expander(f"🐾 {report['species']}（{report['date']} · {report['community']}）", expanded=False):
            st.write(f"**目击地点**：{report['location']}")
            st.write(f"**提交人**：{report['submitter']}")
            st.write(f"**报告内容**：{report['content']}")
            status_badge = "✅ 已审核" if report["status"] == "已审核" else "⏳ 审核中"
            st.write(f"**状态**：{status_badge}")

# ---------------------- 6. 页脚信息 ----------------------
st.divider()
st.markdown("""
    <div style='text-align:center; color:#666; font-size:0.9rem;'>
        © 2024 Komodo Hub | 由 Yayasan Komodo 运营 | 保护印尼濒危物种，人人有责
    </div>
""", unsafe_allow_html=True)