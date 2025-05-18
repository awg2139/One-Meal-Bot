import streamlit as st

# 첫 번째 화면 

# 화면 전환을 위해 초기화화
if "hide_content" not in st.session_state:
    st.session_state.hide_content = False
if "search_clicked" not in st.session_state:
    st.session_state.search_clicked = False
if "show_detail" not in st.session_state:
    st.session_state.show_detail = False
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# 시작화면 로고 스타일 
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

# ui 첫 장면 생성성
if not st.session_state.hide_content:
    title_container = st.empty()
    button_container = st.empty()

    # 로고 불러오기.
    with title_container:
        st.markdown("""
            <div class='centered-title-wrapper'>
                <h1>ONE</h1>
                <h1>MEAL</h1>
                <h1>BOT</h1>
            </div>
        """, unsafe_allow_html=True)

    # 버튼 영역 만들기기
    with button_container:
        if st.button("시작하기 ▶"):
            st.session_state.hide_content = True
            st.rerun()
          
# 두 번째 화면 

# 시작하기 버튼이 눌러 졌을 경우우
else:
    #위에 로고 생성
    st.markdown("<h1 style='text-align:center;'>ONE<br>MEAL BOT</h1>", unsafe_allow_html=True)
    st.markdown("---") # 구분선선

    st.title("One Meal Bot")
    foodSh = st.text_input("음식 이름을 입력하세요", placeholder="ex) 김치찌개")

    # 버튼 두 개 배치치
    tg1, tg2 = st.columns(2)
    with tg1:
        if st.button("검색"):
            st.session_state.search_clicked = True
            st.session_state.show_result = True
    with tg2:
        if st.button("세부사항"):
            st.session_state.show_detail = not st.session_state.show_detail

        # 세부사항 버튼을 눌렀을 경우에만 보임임
        if st.session_state.show_detail:
            st.markdown("## 📋 음식별 칼로리를 입력해주세요.")
            for i in range(5):
                cols = st.columns([0.2, 0.8])  # ✅ tgs → cols
                with cols[0]:
                    checked = st.checkbox(f"항목 {i+1}", key=f"chk{i}")  # ✅ checkBx → checked
                # 체크된 경우에만 입력 가능 
                with cols[1]:
                    st.text_input("칼로리", placeholder="예: 250 kcal", key=f"kcal{i}", disabled=not checked)

    # 검색 결과 출력 
    if st.session_state.show_result:
        st.markdown("## 🧾 검색 결과")

        for i in range(3):
            cols = st.columns([0.3, 0.7])
            with cols[0]:
                st.image("https://via.placeholder.com/100", width=100)
            with cols[1]:
                st.write(f"음식 설명 {i+1}")

        # 새로고침 버튼
        st.markdown("---")
        if st.button("처음으로 돌아가기"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.experimental_rerun()
