import streamlit as st
from streamlit_option_menu import option_menu

# ---------------------- 1. 页面基础配置（与原风格一致） ----------------------
st.set_page_config(
    page_title="Komodo Hub - 社会身份登录",
    page_icon="🐉",
    layout="wide"
)

# ---------------------- 2. 顶部平台标题（居中加粗，保持品牌一致性） ----------------------
st.markdown("""
    <h1 style='text-align: center; color:#2E8B57; font-weight: bold; font-size: 4.5rem; margin-bottom: 10px;'>
        🐉 Komodo Hub
    </h1>
""", unsafe_allow_html=True)
st.markdown("""
    <p style='text-align: center; color:#666; font-weight: bold; font-size: 1.2rem; margin-top: 0;'>
        印尼濒危物种保护数字化社区平台 - 社会身份登录
    </p>
""", unsafe_allow_html=True)

st.divider()

# ---------------------- 3. 社会身份选择（核心入口，简洁分类） ----------------------
st.markdown("""
    <h2 style='text-align: center; color:#333; margin: 30px 0;'>请选择您的社会身份</h2>
""", unsafe_allow_html=True)

# 身份选择标签（横向排列，图标+文字，直观区分）
selected_identity = option_menu(
    menu_title=None,
    options=["社会身份登入"],
    icons=["user", "hands-helping", "flask-vial", "newspaper"],
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"padding": "0 50px", "background-color": "#fafafa", "margin-bottom": "30px"},
        "icon": {"color": "#2E8B57", "font-size": "18px", "margin-right": "8px"},
        "nav-link": {
            "font-size": "14px",
            "padding": "12px 25px",
            "color": "#333",
            "--hover-color": "#e6f7ef",
            "text-align": "center"
        },
        "nav-link-selected": {"background-color": "#2E8B57", "color": "white"},
    }
)

# ---------------------- 4. 身份对应登录表单（简洁填写项，按需适配） ----------------------

# 根据选择的身份，展示对应登录表单（仅保留核心必填项）
if selected_identity == "社会身份登入":
    st.markdown(f"<h3 style='color:#2E8B57; text-align:center;'>{selected_identity}登录</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; font-size:0.9rem;'>仅需基础信息，即可参与公开保护活动</p>",
                unsafe_allow_html=True)

    with st.form("public_login_form", clear_on_submit=True):
        # 两列布局，简洁紧凑
        col1, col2 = st.columns(2, gap="large")
        with col1:
            username = st.text_input("用户名*", placeholder="请输入您的昵称")
            email = st.text_input("电子邮箱*", placeholder="用于登录验证与通知")
        with col2:
            password = st.text_input("密码*", type="password", placeholder="8-20位字符，含字母与数字")
            verify_code = st.text_input("验证码*", placeholder="输入右侧验证码")

        # 验证码图片（模拟，实际对接接口）
        st.markdown("""
            <div style='display: flex; align-items: center; gap: 15px; margin: 15px 0;'>
                <div style='width: 120px; height: 40px; background-color:#f0f0f0; border-radius:5px; display:flex; align-items:center; justify-content:center; color:#666;'>
                    8A3Z
                </div>
                <a href='#' style='color:#2E8B57; font-size:0.9rem;'>刷新验证码</a>
            </div>
        """, unsafe_allow_html=True)

        # 登录选项（记住密码+忘记密码）
        login_col1, login_col2 = st.columns([1, 2])
        with login_col1:
            remember_me = st.checkbox("记住密码（7天）")
        with login_col2:
            st.markdown(
                "<a href='#' style='color:#2E8B57; font-size:0.9rem; text-align:right; display:block;'>忘记密码？</a>",
                unsafe_allow_html=True)

        # 登录按钮（居中宽按钮，突出核心操作）
        st.form_submit_button("登录账号", use_container_width=True, type="primary",
                              help="登录后可访问公开保护资源与活动")

elif selected_identity == "环保志愿者":
    st.markdown(f"<h3 style='color:#2E8B57; text-align:center;'>{selected_identity}登录</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; font-size:0.9rem;'>需验证志愿者身份，可参与线下保护行动</p>",
                unsafe_allow_html=True)

    with st.form("volunteer_login_form", clear_on_submit=True):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            volunteer_id = st.text_input("志愿者编号*", placeholder="由环保组织发放的唯一编号")
            email = st.text_input("注册邮箱*", placeholder="与志愿者编号绑定的邮箱")
        with col2:
            password = st.text_input("密码*", type="password", placeholder="8-20位字符")
            verify_code = st.text_input("验证码*", placeholder="输入右侧验证码")

        # 验证码模拟
        st.markdown("""
            <div style='display: flex; align-items: center; gap: 15px; margin: 15px 0;'>
                <div style='width: 120px; height: 40px; background-color:#f0f0f0; border-radius:5px; display:flex; align-items:center; justify-content:center; color:#666;'>
                    2Y7X（模拟验证码）
                </div>
                <a href='#' style='color:#2E8B57; font-size:0.9rem;'>刷新验证码</a>
            </div>
        """, unsafe_allow_html=True)

        # 登录选项
        login_col1, login_col2 = st.columns([1, 2])
        with login_col1:
            remember_me = st.checkbox("记住密码（7天）")
        with login_col2:
            st.markdown(
                "<a href='#' style='color:#2E8B57; font-size:0.9rem; text-align:right; display:block;'>忘记密码？| 找回志愿者编号</a>",
                unsafe_allow_html=True)

        st.form_submit_button("登录志愿者账号", use_container_width=True, type="primary")

elif selected_identity == "科研工作者":
    st.markdown(f"<h3 style='color:#2E8B57; text-align:center;'>{selected_identity}登录</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; font-size:0.9rem;'>需机构认证，可访问科研数据与协作功能</p>",
                unsafe_allow_html=True)

    with st.form("researcher_login_form", clear_on_submit=True):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            work_id = st.text_input("机构工号*", placeholder="如大学/研究所工号")
            institution = st.selectbox("所属机构*", ["印尼科学院", "大学环保系", "国际环保组织", "其他（请手动输入）"])
            if institution == "其他（请手动输入）":
                custom_institution = st.text_input("其他机构名称", placeholder="请输入您的所属机构")
        with col2:
            email = st.text_input("机构邮箱*", placeholder="需含机构域名，如 xxx@inst.edu")
            password = st.text_input("密码*", type="password", placeholder="8-20位字符")

        # 科研身份无需验证码，增加“身份验证提示”
        st.markdown("""
            <div style='background-color:#e6f7ef; border-left:4px solid #2E8B57; padding:10px 15px; border-radius:5px; margin:15px 0; font-size:0.9rem; color:#333;'>
                提示：首次登录需验证机构邮箱（点击邮件链接完成认证）
            </div>
        """, unsafe_allow_html=True)

        st.form_submit_button("登录科研账号", use_container_width=True, type="primary")

else:  # 媒体从业者
    st.markdown(f"<h3 style='color:#2E8B57; text-align:center;'>{selected_identity}登录</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; font-size:0.9rem;'>需媒体资质验证，可获取保护动态采访权限</p>",
                unsafe_allow_html=True)

    with st.form("media_login_form", clear_on_submit=True):
        col1, col2 = st.columns(2, gap="large")
        with col1:
            media_name = st.text_input("所属媒体*", placeholder="如报社/电视台/新媒体名称")
            job_title = st.selectbox("职位*", ["记者", "编辑", "摄影师", "其他"])
        with col2:
            email = st.text_input("工作邮箱*", placeholder="需含媒体域名")
            password = st.text_input("密码*", type="password", placeholder="8-20位字符")

        # 媒体资质提示
        st.markdown("""
            <div style='background-color:#fff3cd; border-left:4px solid #DAA520; padding:10px 15px; border-radius:5px; margin:15px 0; font-size:0.9rem; color:#333;'>
                注意：首次登录需上传媒体资质证明（记者证/工作证照片），审核通过后开通权限
            </div>
        """, unsafe_allow_html=True)

        st.form_submit_button("登录媒体账号", use_container_width=True, type="primary")

# 关闭表单容器
st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- 5. 底部辅助链接（简洁排列，不喧宾夺主） ----------------------
st.markdown("""
    <div style='text-align:center; margin: 30px 0; font-size:0.9rem; color:#666;'>
        <a href='#' style='color:#2E8B57; margin:0 15px; text-decoration: none;'>首次使用？注册账号</a>
        <span style='color:#ddd;'>|</span>
        <a href='#' style='color:#2E8B57; margin:0 15px; text-decoration: none;'>登录帮助</a>
        <span style='color:#ddd;'>|</span>
        <a href='#' style='color:#2E8B57; margin:0 15px; text-decoration: none;'>隐私政策</a>
    </div>
""", unsafe_allow_html=True)

# ---------------------- 6. 页脚信息（与原平台风格统一） ----------------------
st.divider()
st.markdown("""
    <div style='text-align:center; color:#666; font-size:0.9rem; margin-bottom:20px;'>
        © 2024 Komodo Hub | 由 Yayasan Komodo 运营 | 保护印尼濒危物种，人人有责
    </div>
""", unsafe_allow_html=True)