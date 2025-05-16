import streamlit as st

# 세션 상태 초기화
if 'search_clicked' not in st.session_state:
    st.session_state.search_clicked = False
if 'show_detail' not in st.session_state:
    st.session_state.show_detail = False
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

# 타이틀
st.markdown("<h1 style='text-align:center;'>ONE<br>MEAL - BOT</h1>", unsafe_allow_html=True)
st.markdown("---")

# 검색 입력
st.title("One Meal Bot")
food_input = st.text_input("음식 이름을 입력하세요", placeholder="예: 김치찌개")

# 버튼 영역: 검색 + 세부사항
col1, col2 = st.columns(2)
with col1:
    if st.button("검색"):
        st.session_state.search_clicked = True
        st.session_state.show_result = True  # ✅ 검색 == 결과 보기
with col2:
    if st.button("세부사항"):
        st.session_state.show_detail = not st.session_state.show_detail

# 세부사항 UI
if st.session_state.show_detail:
    st.markdown("## 📋 음식별 칼로리를 입력해주세요.")
    for i in range(5):
        cols = st.columns([0.2, 0.8])
        with cols[0]:
            checked = st.checkbox(f"항목 {i+1}", key=f"chk{i}")
        with cols[1]:
            st.text_input("칼로리", placeholder="예: 250 kcal", key=f"kcal{i}", disabled=not checked)

# 🧾 검색 결과 출력
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
