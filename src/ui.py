import streamlit as st

def init_session_state():
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False

def set_wiki_style():
    dark = st.session_state.get('dark_mode', False)
    
    # Define theme colors
    colors = {
        'bg': "#1a1a1a" if dark else "#F4EEEB",
        'text': "#E1E1E1" if dark else "#202122",
        'border': "#4a4a4a" if dark else "#a2a9b1",
        'input_bg': "#2d2d2d" if dark else "white",
        'input_text': "#E1E1E1" if dark else "#202122",
        'button_bg': "#4a4a4a" if dark else "#1a365d",
        'button_text': "#FFFFFF" if dark else "#FFFFFF",
        'section_bg': "#2d2d2d" if dark else "#f8f9fa"
    }

    st.markdown(
        f"""
    <link href="https://fonts.googleapis.com/css2?family=Bai+Jamjuree:wght@400;500;600;700&amp;family=Crimson+Pro:wght@400;600&amp;display=swap" rel="stylesheet">
    <style>
    .main {{
        background-color: {colors['bg']};
        color: {colors['text']};
        font-family: 'Bai Jamjuree', -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Lato,Helvetica,Arial,sans-serif;
    }}
    .query-title {{
        font-family: 'Crimson Pro', serif;
        text-align: center;
        margin-bottom: 1em;
    }}
    .stApp {{
        max-width: 1366px;
        margin: 0 auto;
    }}
    h1, h2 {{
        font-family: 'Crimson Pro', serif;
        color: {colors['text']};
        border-bottom: 1px solid {colors['border']};
        padding-bottom: 5px;
    }}
    .stTextInput>div>div>input {{
        background-color: {colors['input_bg']};
        color: {colors['input_text']};
        border: 1px solid {colors['border']};
    }}
    .stTextInput>div>div>input::placeholder {{
        color: {colors['border']};
    }}
    p, li, span {{
        color: {colors['text']};
    }}
    .references, .categories {{
        background-color: {colors['section_bg']};
        border: 1px solid {colors['border']};
    }}
    div[data-testid="stToolbar"] {{
        display: none;
    }}
    footer {{
        visibility: hidden;
    }}
    footer:after {{
        content:'Made with Streamlit • '; 
        visibility: visible;
        display: block;
        color: {colors['text']};
        padding: 5px;
        text-align: center;
    }}
    div.stButton > button:not(.theme-toggle) {{
        background-color: {colors['button_bg']} !important;
        color: {colors['button_text']} !important;
    }}
    .theme-toggle {{
        position: fixed !important;
        bottom: 25px !important;
        right: 60px !important;
        background-color: transparent !important;
        color: {colors['text']} !important;
        border: 1px solid {colors['border']} !important;
        padding: 0.25rem 0.75rem !important;
        border-radius: 4px !important;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )

def render_wiki_interface():
    init_session_state()
    set_wiki_style()

    # Create a container for the top bar
    top_bar = st.container()

    with top_bar:
        # Center the Dr. Biết Tuốt banner
        st.markdown(
            "<h1 style='text-align: center;'>Dr. Biết Tuốt</h1>",
            unsafe_allow_html=True,
        )
        
        # Create search container with custom styles
        st.markdown("""
        <style>
        div.stButton > button:first-child {{
            background-color: #1a365d !important;
            color: #FFED4A !important;
            border: none !important;
            border-radius: 4px !important;
            padding: 12px 24px !important;
            width: 100% !important;
            max-width: 280px !important;
            display: block !important;
            margin: 0 auto !important;
            text-align: center !important;
            font-weight: 500 !important;
            font-size: 14px !important;
            transition: all 0.2s ease !important;
        }}
        div.stButton > button:first-child:hover {{
            background-color: #2c5282 !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        }}
        </style>
        """, unsafe_allow_html=True)
        
        # Create search container
        st.markdown('<div style="max-width: 800px; margin: 20px auto;">', unsafe_allow_html=True)
        user_query = st.text_input("Search", placeholder="Search Dr. Biết Tuốt", label_visibility="hidden")
        search_button = st.button("Search")
        st.markdown('</div>', unsafe_allow_html=True)

    if search_button or (
        user_query and st.session_state.get("last_query") != user_query
    ):
        st.session_state["last_query"] = user_query
        return user_query

    if not user_query:
        display_intro()

    # Add theme toggle button using Streamlit's built-in button
    if st.button(f"{'🌞 Light' if st.session_state.dark_mode else '🌒 Dark'} Mode", 
                key="theme_toggle",
                help="Toggle between light and dark mode"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.experimental_rerun()

    return None


def display_intro():
    st.title("Chào mừng đến với Dr. Biết Tuốt")
    st.markdown(
        """
    Dr. Biết Tuốt là một bách khoa toàn thư được hỗ trợ bởi AI, tạo ra các bài viết thông tin về nhiều chủ đề khác nhau.
    Để bắt đầu:

    1. Nhập một chủ đề hoặc câu hỏi vào thanh tìm kiếm ở trên cùng.
    2. Nhấn nút "Tìm kiếm" hoặc nhấn Enter.
    3. Chờ AI tạo ra một bài viết toàn diện dựa trên truy vấn của bạn.

    Xin lưu ý rằng thông tin được cung cấp được tạo ra bởi một mô hình AI và nên được xác minh với các nguồn có thẩm quyền cho các mục đích quan trọng.

    Chúc bạn khám phá vui vẻ!
    """
    )


def display_response(query, response):
    capitalized_query = f'"{query[0].upper() + query[1:]}"'
    st.markdown(f'<h1 class="query-title">{capitalized_query}</h1>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(response)
