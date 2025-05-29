# One-Meal-Bot

## 웹 사이트 링크
- https://one-meal-bot-5jmnbjhcwdpuqvpf8bqlmr.streamlit.app/

## 기능
- 재료명이나 키워드는 **한국어**로만 입력 가능합니다.
- 세부 필터 기능:
  - 사용자가 원하는 키워드를 입력하고, 해당 키워드 및 선택한 영양소와 일치하는 음식을 추천합니다.
  - 키워드를 생략해도 필터링이 가능합니다.
- 여러 영양소를 선택하면 **유클리드 거리 기반 유사도 계산**을 통해 유사한 음식을 추천합니다.
- 자동 맞춤형 식사 추천 기능:
  - 사용자로부터 **성별, 나이, 키, 체중, 활동량**을 입력받아 **BMR**과 **TDEE**를 계산합니다.
  - 제외할 식사 시간을 선택하면, 남은 식사에 **칼로리를 자동 분배**하여 음식을 추천합니다.
  - 아침, 점심, 저녁 각각 하나의 음식을 추천하며, 점심과 저녁은 디저트류를 제외합니다.
  - 활동량 기준은 하단 설명을 참조해 선택할 수 있습니다.

---

## 구현 도구
- **Python (Streamlit)** – 백엔드 및 UI 구현
- **Streamlit Community Cloud** – 프론트엔드 서버 및 배포

---

## 라이선스 및 사용한 오픈소스
- [Streamlit](https://github.com/streamlit/streamlit) (Apache License 2.0)  
- [Pandas](https://github.com/pandas-dev/pandas) (BSD 3-Clause)  
- [NumPy](https://github.com/numpy/numpy) (BSD 3-Clause)


## 데이터 출처
- 본 프로젝트에서 사용한 식품 영양성분 데이터는 **공공데이터포털**에서 제공하는  
  **전국 통합 식품영양성분정보 표준 데이터셋**을 기반으로 합니다.
- 데이터의 저작권은 **식품의약품안전처**에 있으며,  
  공공데이터 이용 조건에 따라 자유롭게 활용하되 출처를 명시해야 합니다.

---

## 전체 라이선스 안내
- 본 프로젝트는 **MIT 라이선스**를 따릅니다.
- 자세한 라이선스 내용은 [LICENSE](./LICENSE) 및 [LICENSES.md](./LICENSES.md)를 참조하세요.

- 본 프로젝트는 **MIT 라이선스**를 따르지만, 사용된 일부 라이브러리는 어피치와 BSD 3-Clause License를 따릅니다.
  
