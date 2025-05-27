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
if "mode" not in st.session_state:
    st.session_state.mode = None

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
            st.session_state.mode = None
            st.session_state.show_detail = False
            st.session_state.show_result = False
            st.rerun()

else:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>ONE<br>MEAL - BOT</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.title("One Meal Bot")
    with st.form("search_form"):
        col_input, col_search = st.columns([5, 1])
        with col_input:
            food_input = st.text_input("음식 이름을 입력하세요", placeholder="예: 김치찌개")

        with col_search:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.form_submit_button("검색"):
                st.session_state.search_clicked = True
                st.session_state.show_result = True

                if st.session_state.mode == "auto":
                    st.session_state.search_mode = "auto"
                elif st.session_state.mode == "manual":
                    st.session_state.search_mode = "manual"
                else:
                    st.session_state.search_mode = "basic"

    # 모드 선택 버튼 (세부사항 / 자동맞춤형)
    col1, col2 = st.columns([2, 2])
    with col1:
        btn_manual = st.button("세부사항")
    with col2:
        btn_auto = st.button("자동맞춤형")

    # 세부사항 버튼 클릭시 토글 
    if btn_manual:
        if st.session_state.mode == "manual":
            st.session_state.mode = None
            st.session_state.show_detail = False
        else:
            st.session_state.mode = "manual"
            st.session_state.show_detail = True

    # 자동맞춤형 버튼 클릭시 토글 
    if btn_auto:
        if st.session_state.mode == "auto":
            st.session_state.mode = None
        else:
            st.session_state.mode = "auto"
            st.session_state.show_detail = False

    # 자동맞춤형 UI -----------------------------
    if st.session_state.mode == "auto":

        st.markdown("<br>", unsafe_allow_html=True)
        # 자동맞춤형 설명란
        st.warning("""
                   ❗ 이 기능은 BMR을 계산하여 맞춤형으로 음식을 검색해줍니다.
                   \n
                   ❗ 세부사항을 입력한 후 검색 버튼을 눌러주세요.
                   """)
        #st.warning("❗ 세부사항을 입력한 후 검색 버튼을 눌러주세요.")
     
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("### 나에게 맞는 하루 칼로리 계산기")

        age = st.number_input("나이", min_value=1, max_value=120, step=1)
        gender = st.radio("성별", ["남성", "여성"], horizontal=True)
        height = st.number_input("키 (cm)", min_value=100, max_value=250, step=1)
        weight = st.number_input("몸무게 (kg)", min_value=20, max_value=200, step=1)

        st.markdown("**활동량 선택 (1~5단계)**")
        activityLevel = st.slider("활동량", min_value=1, max_value=5)

        activity_desc = {
            1: " 1 : 거의 움직이지 않음 (앉아서 일하거나 매우 낮은 활동 수준)",
            2: " 2 :가벼운 활동 (가벼운 운동 주 1~3회)",
            3: " 3 : 보통 활동 (중간 강도 운동 주 3~5회)",
            4: " 4️ : 높은 활동 (매일 운동하거나 격렬한 운동 주 3~4회)",
            5: " 5 : 매우 높은 활동 (하루 2회 운동, 육체 노동 등)"
        }   
        st.markdown(f" 선택한 활동 수준 설명: {activity_desc[activityLevel]}")

        st.markdown("**오늘 이미 먹은 식사를 선택하세요**")
        eatenMeals = st.multiselect("먹은 식사", ["아침", "점심", "저녁"])

        col4 = st.columns([1, 2, 1])
        with col4[1]:
            if st.button("검색",key="bmr_search_auto_bottom"):
                st.session_state.search_clicked = True
                st.session_state.show_result = True

                if st.session_state.mode == "auto":
                    st.session_state.search_mode = "auto"
                elif st.session_state.mode == "manual":
                    st.session_state.search_mode = "manual"
                else:
                    st.session_state.search_mode = None

        # BMR 계산
        if gender == "남성":
            bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
        else:
            bmr = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

        # Tdee 계산 
        activity = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
        tdee = bmr * activity[activityLevel]

        st.session_state.tdee = tdee

        # 선택하지 않은은 끼니당 칼로리 계산
        take_meal = {"아침": 0.25, "점심": 0.40, "저녁": 0.35}

        take_meals = [m for m in take_meal if m not in eatenMeals]
        user_kcal = {meal: tdee * take_meal[meal] for meal in take_meals}
        st.session_state.user_kcal = user_kcal
        st.markdown("---")

    # 세부사항 목록 복구 
    st.session_state.show_detail = st.session_state.mode == "manual"


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

# 세부사항 -----------------------------
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

    col5 = st.columns([1, 2, 1])
    with col5[1]:
        if st.button("검색",key="detail_search_auto_bottom"):
            st.session_state.search_clicked = True
            st.session_state.show_result = True

            if st.session_state.mode == "auto":
                st.session_state.search_mode = "auto"
            elif st.session_state.mode == "manual":
                st.session_state.search_mode = "manual"
            else:
                    st.session_state.search_mode = None

if st.session_state.show_result:
    # 기본 검색 
    if st.session_state.get("search_mode") == "basic":
        search = food_input.strip()
        data = FoodData()

        if search:
            filtered = data[data["식품명"].str.contains(search, case=False, na=False)]
        else:
            st.warning("❌ 음식 이름을 입력해주세요. ❌")
            st.stop()

        filtered = filtered.dropna(subset=["에너지(kcal)"]).copy()
        filtered["에너지(kcal)"] = pd.to_numeric(filtered["에너지(kcal)"], errors='coerce')
        filtered = filtered.sample(n=min(30, len(filtered)), random_state=42).reset_index(drop=True)
        
        if filtered.empty:
            st.warning("해당 검색어에 대한 결과가 없습니다.")
        else:
            st.markdown("## 검색 결과")
            st.success(f"🔍 검색 결과: **{filtered.shape[0]}개 음식 발견**")
            for i, row in filtered.head(30).iterrows(): 
                st.markdown(f"### {row['식품명']}")
                st.write(f"에너지: {row['에너지(kcal)']} kcal")
                st.write(f"단백질: {row['단백질(g)']} g")
                st.write(f"지방: {row['지방(g)']} g")
                st.write(f"당류: {row['당류(g)']} g")
                st.write(f"칼슘: {row['칼슘(mg)']} mg")
                st.write(f"콜레스테롤: {row['콜레스테롤(mg)']} mg")
                st.markdown("---")


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


    # 검색 결과 -----------------------------
    if st.session_state.show_result:
        data = FoodData()

        # 자동 맞춤형 식단
        if st.session_state.get("search_mode") == "auto" and "user_kcal" in st.session_state:
            for meal, target_kcal in st.session_state.user_kcal.items():
                st.markdown(f"### {meal} 추천 ({int(target_kcal)} kcal 기준)")
                filtered = data.dropna(subset=["에너지(kcal)"]).copy()
                filtered["에너지(kcal)"] = pd.to_numeric(filtered["에너지(kcal)"], errors='coerce')
                
                # 음식 이름 입력값이 있으면 해당 이름 포함하는 것만 필터링
                if food_input.strip():
                    filtered = filtered[filtered["식품명"].str.contains(food_input.strip(), case=False, na=False)]

                
                # 조미료, 양념류 제외
                filtered = filtered[
                    ~filtered["식품대분류명"].isin(["조미식품류", "장류, 양념류"])
                ]

                # 식사에 추가 되면 안되는 것들 
                filtered = filtered[
                    ~filtered["식품명"].str.contains("기름|소스|장|드레싱|분말|액젓|마요네즈|쌈장", na=False)
                ]
                # 점심, 저녁에는 빵이나 디저트류 제외 
                if meal in ["점심", "저녁"]:
                    exclude_if_lunch_or_dinner = ["빵 및 과자류", "디저트류", "음료 및 차류", "유제품류 및 빙과류" , "음료 및 주류류", "아침식사용 대체식품", "아이스크림류", "시리얼류"]
                    filtered = filtered[~filtered["식품대분류명"].isin(exclude_if_lunch_or_dinner)]
                    
                filtered["유사도"] = abs(filtered["에너지(kcal)"] - target_kcal)
                filtered = filtered.sort_values("유사도").reset_index(drop=True)
                if filtered.empty:
                    st.warning(f"{meal} 선택하신 값의 결과가 존재하지 않습니다. .")
                    continue
                best = filtered.iloc[0]
                st.success(f" {meal} 추천 음식: **{best['식품명']}**")
                st.write(f"에너지: {best['에너지(kcal)']} kcal")
                st.write(f"단백질: {best['단백질(g)']} g")
                st.write(f"지방: {best['지방(g)']} g")
                st.write(f"당류: {best['당류(g)']} g")
                st.write(f"칼슘: {best['칼슘(mg)']} mg")
                st.write(f"콜레스테롤: {best['콜레스테롤(mg)']} mg")
                st.markdown("---")
            st.stop()

        # 세부사항 결과값 
        def numTrue(value):
            return value.strip().isdigit()

        numT = False
        for chk_key in ["chk_energy", "chk_protein", "chk_fat", "chk_sugar", "chk_calcium", "chk_cholesterol"]:
            val_key = chk_key.replace("chk", "val")
            if st.session_state.get(chk_key) and not numTrue(st.session_state.get(val_key, "")):
                st.warning(f"{chk_key}에는 숫자만 입력해주세요.")
                numT = True

        if not numT:
            search = food_input.strip()
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

            pickNutrient = []
            compareNutrient = []

            for chk_key, (val_key, col_name) in nutrientDic.items():
                if st.session_state.get(chk_key) and st.session_state.get(val_key, "").strip().isdigit():
                    pickNutrient.append(float(st.session_state[val_key].strip()))
                    compareNutrient.append(col_name)

            if compareNutrient:
                st.markdown("## 검색 결과")
                filtered = filtered.dropna(subset=compareNutrient).copy()
                for col in compareNutrient:
                    filtered[col] = pd.to_numeric(filtered[col], errors='coerce')
                filtered[compareNutrient] = filtered[compareNutrient].fillna(0)

                pickNutrient_np = np.array(pickNutrient)
                filtered["유사도"] = filtered[compareNutrient].apply(
                    lambda row: np.linalg.norm(row.values - pickNutrient_np), axis=1
                )
                filtered = filtered.sort_values("유사도").reset_index(drop=True)

                if filtered.empty:
                    st.warning("죄송합니다. 음식을 찾을 수 없습니다. 음식 이름을 다시 입력해주세요.")
                else:
                    best_match = filtered.iloc[0]
                    st.success(f"\U0001F4A1 입력한 값들과 가장 유사한 음식: **{best_match['식품명']}**")
                    for col in compareNutrient:
                        st.write(f" {col}: {best_match[col]}")
                    st.markdown("---")

                    for i, row in filtered.head(30).iterrows():
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
            "chk_cholesterol", "val_cholesterol",
            "search_mode", "user_kcal", "tdee"
        ]

        for k in resetValue:
            if k in st.session_state:
                del st.session_state[k]  

        st.rerun()
