import streamlit as st

if "hide_content" not in st.session_state:
    st.session_state.hide_content = False
if "search_clicked" not in st.session_state:
    st.session_state.search_clicked = False
if "show_detail" not in st.session_state:
    st.session_state.show_detail = False
if "show_result" not in st.session_state:
    st.session_state.show_result = False

st.markdown(
    """
    <style>
        .block-container {
            padding-top: 0rem;
        }
        .centered-title-wrapper {
            text-align: center;
            color: OrangeRed;
            margin: 0;
        }
        .centered-title-wrapper h1 {
            font-size: 215px;
            line-height: 1.1;
            margin: 0;
        }
        .stButton>button {
            font-size: 24px;
            padding: 0.5em 2em;
            color: white;
            background-color: OrangeRed;
            display: block;
            margin: 50px auto 0 auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

if not st.session_state.hide_content:
    title_container = st.empty()
    button_container = st.empty()

    with title_container:
        st.markdown("""
            <div class='centered-title-wrapper'>
                <h1>ONE</h1>
                <h1>MEAL</h1>
                <h1>BOT</h1>
            </div>
        """, unsafe_allow_html=True)

    with button_container:
        if st.button("시작하기 ▶"):
            st.session_state.hide_content = True
            st.rerun()
          
else:
    st.markdown("<h1 style='text-align:center;'>ONE<br>MEAL - BOT</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.title("One Meal Bot")
    food_input = st.text_input("음식 이름을 입력하세요", placeholder="예: 김치찌개")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("검색"):
            st.session_state.search_clicked = True
            st.session_state.show_result = True
    with col2:
        if st.button("세부사항"):
            st.session_state.show_detail = not st.session_state.show_detail

    if st.session_state.show_detail:
        st.markdown("## 📋 음식별 칼로리를 입력해주세요.")
        for i in range(5):
            cols = st.columns([0.2, 0.8])
            with cols[0]:
                checked = st.checkbox(f"항목 {i+1}", key=f"chk{i}")
            with cols[1]:
                st.text_input("칼로리", placeholder="예: 250 kcal", key=f"kcal{i}", disabled=not checked)

    if st.session_state.show_result:
        st.markdown("## 🧾 검색 결과")

        for i in range(3):
            cols = st.columns([0.3, 0.7])
            with cols[0]:
                st.image("https://via.placeholder.com/100", width=100)
            with cols[1]:
                st.write(f"음식 설명 {i+1}")

        st.markdown("---")
        if st.button("처음으로 돌아가기"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.experimental_rerun()
