import streamlit as st
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


@st.cache_data
def FoodData():
    return pd.read_csv("food.csv", encoding="cp949")

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
            transition: all 0.1s ease-in-out;
        }
        .stButton>button:active {
            color: white;
            background-color: #cc3300;
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

# 세부사항 변수 초기화 ( 이름만 입력할 시 문제 방지 )
chk_energy = st.session_state.get("chk_energy", False)
val_energy = st.session_state.get("val_energy", "")
chk_protein = st.session_state.get("chk_protein", False)
val_protein = st.session_state.get("val_protein", "")
chk_fat = st.session_state.get("chk_fat", False)
val_fat = st.session_state.get("val_fat", "")
chk_sugar = st.session_state.get("chk_sugar", False)
val_sugar = st.session_state.get("val_sugar", "")
chk_calcium = st.session_state.get("chk_calcium", False)
val_calcium = st.session_state.get("val_calcium", "")
chk_cholesterol = st.session_state.get("chk_cholesterol", False)
val_cholesterol = st.session_state.get("val_cholesterol", "")

# 세부사항 
if st.session_state.show_detail:
    st.markdown("## 원하는 영양소양을 입력해주세요.")

    col1, col2 = st.columns([0.3, 0.7]) # 열 끼리 차지하는 크기 설정정
    with col1:
        chk_energy = st.checkbox("에너지(kcal)", key="chk_energy")
    with col2:
        val_energy = st.text_input("에너지 입력", placeholder="예: 250", key="val_energy", disabled=not chk_energy)

    col1, col2 = st.columns([0.3, 0.7]) 
    with col1:
        chk_protein = st.checkbox("단백질(g)", key="chk_protein")
    with col2:
        val_protein = st.text_input("단백질 입력", placeholder="예: 10", key="val_protein", disabled=not chk_protein)

    col1, col2 = st.columns([0.3, 0.7]) 
    with col1:
        chk_fat = st.checkbox("지방(g)", key="chk_fat")
    with col2:
        val_fat = st.text_input("지방 입력", placeholder="예: 5", key="val_fat", disabled=not chk_fat)

    col1, col2 = st.columns([0.3, 0.7]) 
    with col1:
        chk_sugar = st.checkbox("당류(g)", key="chk_sugar")
    with col2:
        val_sugar = st.text_input("당류 입력", placeholder="예: 3", key="val_sugar", disabled=not chk_sugar)

    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        chk_calcium = st.checkbox("칼슘(mg)", key="chk_calcium")
    with col2:
        val_calcium = st.text_input("칼슘 입력", placeholder="예: 100", key="val_calcium", disabled=not chk_calcium)

    col1, col2 = st.columns([0.3, 0.7])
    with col1:
        chk_cholesterol = st.checkbox("콜레스테롤(mg)", key="chk_cholesterol")
    with col2:
        val_cholesterol = st.text_input("콜레스테롤 입력", placeholder="예: 50", key="val_cholesterol", disabled=not chk_cholesterol)

if st.session_state.show_result:

    def numTrue(value):
        return value.strip().isdigit()

    numT = False

    if chk_energy and val_energy.strip() and not numTrue(val_energy):
        st.warning("에너지에는 숫자만 입력해주세요.")
        numT = True
    if chk_protein and val_protein.strip() and not numTrue(val_protein):
        st.warning("단백질에는 숫자만 입력해주세요.")
        numT = True
    if chk_fat and val_fat.strip() and not numTrue(val_fat):
        st.warning("지방에는 숫자만 입력해주세요.")
        numT = True
    if chk_sugar and val_sugar.strip() and not numTrue(val_sugar):
        st.warning("당류에는 숫자만 입력해주세요.")
        numT = True
    if chk_calcium and val_calcium.strip() and not numTrue(val_calcium):
        st.warning("칼슘에는 숫자만 입력해주세요.")
        numT = True
    if chk_cholesterol and val_cholesterol.strip() and not numTrue(val_cholesterol):
        st.warning("콜레스테롤에는 숫자만 입력해주세요.")
        numT = True

    st.markdown("## 검색 결과")

    data = FoodData()
    search = food_input.strip()

    if not numT:
        if search:
            filtered = data[data["식품명"].str.contains(search, case=False, na=False)]
        else:
            filtered = data.copy()

        nutrientDic = {
            "chk_energy": ("val_energy", "에너지(kcal)"),
            "chk_protein": ("val_protein", "단백질(g)"),
            "chk_fat": ("val_fat", "지방(g)"),
            "chk_sugar": ("val_sugar", "당류(g)"),
            "chk_calcium": ("val_calcium", "칼슘(mg)"),
            "chk_cholesterol": ("val_cholesterol", "콜레스테롤(mg)")
        }

        pickNutrient = []        # 영양소소 수치값 리스트
        compareNutrient = []     # 그에 대응하는 영양소 이름들

        for chk_key, (val_key, col_name) in nutrientDic.items():
            if st.session_state.get(chk_key) and st.session_state.get(val_key, "").strip().isdigit():
                pickNutrient.append(float(st.session_state[val_key].strip()))
                compareNutrient.append(col_name)

        if compareNutrient:
            filtered = filtered.dropna(subset=compareNutrient).copy()
            for col in compareNutrient:
                filtered[col] = pd.to_numeric(filtered[col], errors='coerce')

            filtered[compareNutrient] = filtered[compareNutrient].fillna(0)  #  NaN을 0으로 처리

            pickNutrient_np = np.array(pickNutrient)

            filtered["유사도"] = filtered[compareNutrient].apply(
                lambda row: np.linalg.norm(row.values - pickNutrient_np), axis=1
            )

            filtered = filtered.sort_values("유사도").reset_index(drop=True)

            best_match = filtered.iloc[0]
            st.success(f"\U0001F4A1 입력한 값들과 가장 유사한 음식: **{best_match['식품명']}**")
            for col in compareNutrient:
                st.write(f"✔️ {col}: {best_match[col]}")
            st.markdown("---")

        if filtered.empty:
            st.warning("검색 결과가 없습니다.")
        else:
            st.markdown("---")
            for i, row in filtered.iterrows():
                st.markdown(f"###  {row['식품명']}")
                st.write(f"에너지: {row['에너지(kcal)']} kcal")
                st.write(f"단백질: {row['단백질(g)']} g")
                st.write(f"지방: {row['지방(g)']} g")
                st.write(f"당류: {row['당류(g)']} g")
                st.write(f"칼슘: {row['칼슘(mg)']} mg")
                st.write(f"콜레스테롤: {row['콜레스테롤(mg)']} mg")
                st.markdown("---")

    if st.button("처음으로 돌아가기"):
        resetValue = [
            "search_clicked", "show_detail", "show_result",
            "chk_energy", "val_energy",
            "chk_protein", "val_protein",
            "chk_fat", "val_fat",
            "chk_sugar", "val_sugar",
            "chk_calcium", "val_calcium",
            "chk_cholesterol", "val_cholesterol"
        ]

        for k in resetValue:
            if k in st.session_state:
                del st.session_state[k]  

        st.rerun()


