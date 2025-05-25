# One-Meal-Bot

## 기능 
- 재료명이나, 키워드는 한국어만 입력시 결과를 확인할 수 있습니다.
  
- 세부 필터 기능 : 사용자가 원하는 키워드를 입력하고 그에 맞는 칼로리나
  영양소를 분석하면 입력한 키워드와 선택한 영양소와 둘 다 일치하는 음식을
  추천해줍니다. ( 물론 키워드를 입력하지 않아도 됩니다. )
- 여러 영양소를 선택했을 시 유클리드 거리 계산 기반으로 전체적으로 유사한
  음식을 추천해 줍니다.

- 자동 맞춤형 식사 추천 기능은 사용자에게 성별, 나이, 키, 체중, 활동량
  을 입력 받아서 BMR과 TDEE를 계산해줍니다.
- 사용자가 제외할 식사 시간을 선택하면 그날 식사를 제외한 기준으로 비율에
  맞게 칼로리를 자동 분배해 음식을 추천해 줍니다.
- 아침, 점심, 저녁 각각 하나의 음식을 추천해주며, 점심 저녁은 디저트 같은
  가벼운 음식을 제외하였습니다.
- 활동량을 체크하실때 각 단계의 활동량 설명을 밑에서 확인 할 수 있으니
  그에 맞게 선택하면 좋습니다. 
  

## 사용할 도구
- python 
/ 코드 구현
- python(Streamlit) 
/ ui 구현
- Streamlit Community Cloud
/ 프론트엔드 서버

## 사용한 라이선스
- [Streamlit](https://github.com/streamlit/streamlit) (Apache License 2.0)
- [Pandas](https://github.com/pandas-dev/pandas) (BSD 3-Clause)
- [Scikit-learn](https://github.com/scikit-learn/scikit-learn) (BSD 3-Clause)
- [sklearn-pandas](https://github.com/scikit-learn-contrib/sklearn-pandas) (MIT License)
- [NumPy](https://github.com/numpy/numpy) (BSD 3-Clause)

## 데이터 출처
본 프로젝트에서 사용한 식품 영양성분 데이터는
공공데이터포털에서 제공하는
전국 통합 식품영양성분정보 표준 데이터셋을 기반으로 하였습니다.

해당 데이터의 저작권은 식품의약품안전처에 있으며,
공공데이터 이용조건에 따라 자유롭게 활용하되, 출처를 명시해야 합니다.


본 프로젝트는 MIT 라이선스를 따릅니다.  
또한 다음과 같은 오픈소스 라이브러리를 사용하며, 각 라이브러리는 해당 라이선스를 따릅니다:
- Streamlit (Apache 2.0)
- Pandas, Scikit-learn, NumPy (BSD 3-Clause)
- sklearn-pandas (MIT)

자세한 내용은 [LICENSE](./LICENSE) 및 [LICENSES.md](./LICENSES.md)를 참조해주세요.


