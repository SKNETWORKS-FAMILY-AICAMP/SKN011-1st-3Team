# # import streamlit as st
# # import plotly.graph_objects as go
# # import os

# # # 자동차 데이터 예시
# # data = {
# #     "현대": ["아반떼", "쏘나타", "팰리세이드"],
# #     "기아": ["K5", "K7", "스포티지"],
# #     "테슬라": ["모델3", "모델Y", "모델S"]
# # }

# # # 성능 및 지원금 정보 예시
# # performance_data = {
# #     "아반떼": {"연비": "15km/L", "마력": "123hp", "지원금": {"서울": 100, "경기": 80}},
# #     "쏘나타": {"연비": "12km/L", "마력": "160hp", "지원금": {"서울": 120, "경기": 90}},
# #     "팰리세이드": {"연비": "9km/L", "마력": "277hp", "지원금": {"서울": 150, "경기": 100}},
# #     "K5": {"연비": "14km/L", "마력": "150hp", "지원금": {"서울": 110, "경기": 85}},
# #     "K7": {"연비": "11km/L", "마력": "180hp", "지원금": {"서울": 130, "경기": 95}},
# #     "스포티지": {"연비": "13km/L", "마력": "200hp", "지원금": {"서울": 140, "경기": 105}},
# #     "모델3": {"연비": "전기차", "마력": "283hp", "지원금": {"서울": 200, "경기": 150}},
# #     "모델Y": {"연비": "전기차", "마력": "345hp", "지원금": {"서울": 250, "경기": 170}},
# #     "모델S": {"연비": "전기차", "마력": "670hp", "지원금": {"서울": 300, "경기": 200}},
# # }

# # # 지역 목록
# # regions = ["서울", "경기", "강원", "충청", "전라", "경상"]

# # st.set_page_config(page_title="전기차 모델 비교", page_icon="🚗", layout="wide")
# # st.title("🔍 전기차 모델 성능 및 지원금 비교")

# # # 다크 모드/라이트 모드 토글
# # theme_toggle = st.toggle("🌗 다크 모드 활성화", value=False)
# # if theme_toggle:
# #     st.markdown("""
# #     <style>
# #         .main, .block-container {
# #             background-color: #2E2E2E;
# #             color: white;
# #         }
# #         .stButton>button, .stSelectbox>div>div {
# #             color: white;
# #             background-color: #3E3E3E;
# #         }
# #     </style>
# #     """, unsafe_allow_html=True)

# # # 모델별 대표 이미지 표시 (로컬 이미지 경로 사용)
# # def show_car_image(model):
# #     base_path = os.path.dirname(__file__)  
# #     image_paths = {
# #         "아반떼": os.path.join(base_path, "images/avante.gif"),
# #         "쏘나타": os.path.join(base_path, "images/sonata.gif"),
# #         "팰리세이드": os.path.join(base_path, "images/palisade.jpg"),
# #         "K5": os.path.join(base_path, "images/k5.jpg"),
# #         "K7": os.path.join(base_path, "images/k7.jpg"),
# #         "스포티지": os.path.join(base_path, "images/sportage.jpg"),
# #         "모델3": os.path.join(base_path, "images/model3.jpg"),
# #         "모델Y": os.path.join(base_path, "images/modely.jpg"),
# #         "모델S": os.path.join(base_path, "images/models.jpg"),
# #     }
# #     image_path = image_paths.get(model, None)
# #     if image_path and os.path.exists(image_path):
# #         st.image(image_path, caption=f"{model} 대표 이미지", use_container_width=True)
# #     else:
# #         st.warning(f"❗ {model}에 대한 로컬 이미지를 찾을 수 없습니다.")

# # # 자동차 비교 여부 선택
# # compare = st.toggle("✨ 두 모델 비교", value=False)

# # # 선택 항목을 가로로 배치
# # col1, col2 = st.columns(2)

# # with col1:
# #     st.subheader("🚗 첫 번째 자동차 선택")
# #     selected_company1 = st.selectbox("**회사**", list(data.keys()), key="company1")
# #     selected_model1 = st.selectbox("**모델**", data[selected_company1], key="model1")
# #     selected_region1 = st.selectbox("**거주 지역**", regions, key="region1")
# #     show_car_image(selected_model1)

# # if compare:
# #     with col2:
# #         st.subheader("🚙 두 번째 자동차 선택")
# #         selected_company2 = st.selectbox("**비교 전기차 회사**", list(data.keys()), key="company2")
# #         selected_model2 = st.selectbox("**비교 전기차 모델**", data[selected_company2], key="model2")
# #         selected_region2 = st.selectbox("**거주 지역**", regions, key="region2")
# #         show_car_image(selected_model2)

# # # 성능 세부 정보 확장 기능
# # def display_car_info(model, region):
# #     model_info = performance_data.get(model, {})
# #     support = model_info.get("지원금", {}).get(region, "지원금 정보 없음")
# #     with st.expander(f"🔎 {model} 상세 정보 보기"):
# #         st.success(f"💡 **연비:** {model_info.get('연비', '정보 없음')}")
# #         st.info(f"⚡ **마력:** {model_info.get('마력', '정보 없음')}")
# #         st.warning(f"💸 **{region} 지역 지원금:** {support}만원")
# #     return model_info, support

# # if selected_model1 and selected_region1:
# #     model_info1, support1 = display_car_info(selected_model1, selected_region1)

# #     if compare and selected_model2 and selected_region2:
# #         model_info2, support2 = display_car_info(selected_model2, selected_region2)

# #         # 지원금 비율 파이 차트 추가
# #         fig_pie = go.Figure(data=[go.Pie(labels=[selected_model1, selected_model2],
# #                                         values=[support1, support2],
# #                                         hole=.3)])
# #         fig_pie.update_layout(title_text="💰 지원금 비율 비교",
# #                               paper_bgcolor="#2E2E2E" if theme_toggle else "white",
# #                               font_color="white" if theme_toggle else "black")
# #         st.plotly_chart(fig_pie, use_container_width=True)

# #         # 성능 비교 차트
# #         if model_info1.get("연비") != "전기차" and model_info2.get("연비") != "전기차":
# #             fig = go.Figure()
# #             fig.add_trace(go.Bar(name=selected_model1,
# #                                  x=["연비 (km/L)", "마력 (hp)", "지원금 (만원)"],
# #                                  y=[int(model_info1["연비"].replace("km/L", "")),
# #                                     int(model_info1["마력"].replace("hp", "")),
# #                                     support1]))
# #             fig.add_trace(go.Bar(name=selected_model2,
# #                                  x=["연비 (km/L)", "마력 (hp)", "지원금 (만원)"],
# #                                  y=[int(model_info2["연비"].replace("km/L", "")),
# #                                     int(model_info2["마력"].replace("hp", "")),
# #                                     support2]))
# #             fig.update_layout(barmode='group', title="🚀 모델 간 성능 및 지원금 비교",
# #                               xaxis_title="항목", yaxis_title="값",
# #                               paper_bgcolor="#2E2E2E" if theme_toggle else "white",
# #                               font_color="white" if theme_toggle else "black")
# #             st.plotly_chart(fig, use_container_width=True)
# #         else:
# #             st.info("⚡ 전기차 모델은 연비가 다르게 표시됩니다.")

# # st.markdown("""
# # ---
# # ### 💬 **추가 정보**
# # ✅ 비교하고 싶은 모델을 선택해 주세요. 
# # ⚡ 전기차 모델의 경우 연비 대신 전기차로 표시됩니다.
# # 💡 지원금 정보는 선택한 지역에 따라 달라질 수 있습니다.
# # 🌐 언어 지원 기능 추가 예정입니다.
# # """)

# import streamlit as st  # 📦 Streamlit 라이브러리를 가져와 웹 앱을 생성합니다.
# import plotly.graph_objects as go  # 📊 Plotly의 그래프 객체를 가져와 시각화를 처리합니다.
# import os  # 🗂️ OS 모듈을 가져와 파일 경로를 다루는 데 사용합니다.

# # 🚗 **자동차 데이터 정의**
# data = {
#     "현대": ["아반떼", "쏘나타", "팰리세이드"],  # 현대 자동차의 모델 목록
#     "기아": ["K5", "K7", "스포티지"],           # 기아 자동차의 모델 목록
#     "테슬라": ["모델3", "모델Y", "모델S"]        # 테슬라 자동차의 모델 목록
# }

# # 🏎️ **성능 및 지원금 정보 정의**
# performance_data = {
#     "아반떼": {"연비": "15km/L", "마력": "123hp", "지원금": {"서울": 100, "경기": 80}},  # 아반떼 정보
#     "쏘나타": {"연비": "12km/L", "마력": "160hp", "지원금": {"서울": 120, "경기": 90}},  # 쏘나타 정보
#     "팰리세이드": {"연비": "9km/L", "마력": "277hp", "지원금": {"서울": 150, "경기": 100}}, # 팰리세이드 정보
#     "K5": {"연비": "14km/L", "마력": "150hp", "지원금": {"서울": 110, "경기": 85}},       # K5 정보
#     "K7": {"연비": "11km/L", "마력": "180hp", "지원금": {"서울": 130, "경기": 95}},       # K7 정보
#     "스포티지": {"연비": "13km/L", "마력": "200hp", "지원금": {"서울": 140, "경기": 105}},  # 스포티지 정보
#     "모델3": {"연비": "전기차", "마력": "283hp", "지원금": {"서울": 200, "경기": 150}},     # 모델3 정보
#     "모델Y": {"연비": "전기차", "마력": "345hp", "지원금": {"서울": 250, "경기": 170}},     # 모델Y 정보
#     "모델S": {"연비": "전기차", "마력": "670hp", "지원금": {"서울": 300, "경기": 200}},     # 모델S 정보
# }

# # 🗺️ **지역 목록 정의**
# regions = ["서울", "경기", "강원", "충청", "전라", "경상"]  # 사용자가 선택할 수 있는 지역 목록입니다.

# # 🌟 **페이지 설정 및 다크 모드 토글**
# st.set_page_config(page_title="전기차 모델 비교", page_icon="🚗", layout="wide")  # 페이지 설정
# st.title("🔍 전기차 모델 성능 및 지원금 비교")  # 페이지 제목 출력

# theme_toggle = st.toggle("🌗 다크 모드 활성화", value=False)  # 다크 모드 토글 버튼 생성
# if theme_toggle:  # 다크 모드가 활성화되면 아래 스타일 적용
#     st.markdown("""
#     <style>
#         .main, .block-container { background-color: #2E2E2E; color: white; }  # 다크 모드 배경/텍스트 색상
#         .stButton>button, .stSelectbox>div>div { color: white; background-color: #3E3E3E; }  # 버튼/선택박스 색상
#     </style>
#     """, unsafe_allow_html=True)

# # 🖼️ **모델별 대표 이미지 표시 함수**
# def show_car_image(model):
#     base_path = os.path.dirname(__file__)  # 현재 파일 경로 가져오기
#     image_paths = {  # 각 모델별 이미지 경로 정의
#         "아반떼": os.path.join(base_path, "images/avante.gif"),
#         "쏘나타": os.path.join(base_path, "images/sonata.gif"),
#         "팰리세이드": os.path.join(base_path, "images/palisade.jpg"),
#         "K5": os.path.join(base_path, "images/k5.jpg"),
#         "K7": os.path.join(base_path, "images/k7.jpg"),
#         "스포티지": os.path.join(base_path, "images/sportage.jpg"),
#         "모델3": os.path.join(base_path, "images/model3.jpg"),
#         "모델Y": os.path.join(base_path, "images/modely.jpg"),
#         "모델S": os.path.join(base_path, "images/models.jpg"),
#     }
#     image_path = image_paths.get(model, None)  # 선택된 모델의 이미지 경로 가져오기
#     if image_path and os.path.exists(image_path):
#         st.image(image_path, caption=f"{model} 대표 이미지", use_container_width=True)  # 이미지 출력
#     else:
#         st.warning(f"❗ {model}에 대한 로컬 이미지를 찾을 수 없습니다.")  # 이미지 없을 때 경고

# # 🏎️ **모델 선택 UI 및 비교 기능**
# compare = st.toggle("✨ 두 모델 비교", value=False)  # 두 모델 비교 여부 토글

# col1, col2 = st.columns(2)  # 두 개의 컬럼 생성하여 나란히 배치

# with col1:
#     st.subheader("🚗 첫 번째 자동차 선택")  # 첫 번째 모델 선택 섹션 제목
#     selected_company1 = st.selectbox("**회사**", list(data.keys()), key="company1")  # 회사 선택
#     selected_model1 = st.selectbox("**모델**", data[selected_company1], key="model1")  # 모델 선택
#     selected_region1 = st.selectbox("**거주 지역**", regions, key="region1")  # 지역 선택
#     show_car_image(selected_model1)  # 선택된 모델 이미지 표시

# if compare:  # 두 번째 모델 비교가 활성화되었을 때
#     with col2:
#         st.subheader("🚙 두 번째 자동차 선택")  # 두 번째 모델 선택 섹션 제목
#         selected_company2 = st.selectbox("**비교 전기차 회사**", list(data.keys()), key="company2")
#         selected_model2 = st.selectbox("**비교 전기차 모델**", data[selected_company2], key="model2")
#         selected_region2 = st.selectbox("**거주 지역**", regions, key="region2")
#         show_car_image(selected_model2)  # 두 번째 모델 이미지 표시

# # 🔎 **성능 및 지원금 정보 표시 함수**
# def display_car_info(model, region):
#     model_info = performance_data.get(model, {})  # 모델 정보 가져오기
#     support = model_info.get("지원금", {}).get(region, "지원금 정보 없음")  # 지원금 정보 가져오기
#     with st.expander(f"🔎 {model} 상세 정보 보기"):  # 확장형 UI로 정보 표시
#         st.success(f"💡 **연비:** {model_info.get('연비', '정보 없음')}")  # 연비 출력
#         st.info(f"⚡ **마력:** {model_info.get('마력', '정보 없음')}")    # 마력 출력
#         st.warning(f"💸 **{region} 지역 지원금:** {support}만원")        # 지원금 출력
#     return model_info, support

# # 🎯 **선택된 모델 정보 출력 및 비교 차트**
# if selected_model1 and selected_region1:
#     model_info1, support1 = display_car_info(selected_model1, selected_region1)  # 첫 번째 모델 정보 표시

#     if compare and selected_model2 and selected_region2:
#         model_info2, support2 = display_car_info(selected_model2, selected_region2)  # 두 번째 모델 정보 표시

#         # 💰 **지원금 비율 파이 차트**
#         fig_pie = go.Figure(data=[go.Pie(labels=[selected_model1, selected_model2],
#                                         values=[support1, support2], hole=.3)])
#         fig_pie.update_layout(title_text="💰 지원금 비율 비교",
#                               paper_bgcolor="#2E2E2E" if theme_toggle else "white",
#                               font_color="white" if theme_toggle else "black")
#         st.plotly_chart(fig_pie, use_container_width=True)  # 파이 차트 출력

#         # 🚀 **성능 비교 바 차트**
#         if model_info1.get("연비") != "전기차" and model_info2.get("연비") != "전기차":  # 둘 다 전기차가 아닐 때
#             fig = go.Figure()
#             fig.add_trace(go.Bar(name=selected_model1,
#                                  x=["연비 (km/L)", "마력 (hp)", "지원금 (만원)"],
#                                  y=[int(model_info1["연비"].replace("km/L", "")),
#                                     int(model_info1["마력"].replace("hp", "")),
#                                     support1]))
#             fig.add_trace(go.Bar(name=selected_model2,
#                                  x=["연비 (km/L)", "마력 (hp)", "지원금 (만원)"],
#                                  y=[int(model_info2["연비"].replace("km/L", "")),
#                                     int(model_info2["마력"].replace("hp", "")),
#                                     support2]))
#             fig.update_layout(barmode='group', title="🚀 모델 간 성능 및 지원금 비교",
#                               xaxis_title="항목", yaxis_title="값",
#                               paper_bgcolor="#2E2E2E" if theme_toggle else "white",
#                               font_color="white" if theme_toggle else "black")
#             st.plotly_chart(fig, use_container_width=True)  # 바 차트 출력
#         else:
#             st.info("⚡ 전기차 모델은 연비가 다르게 표시됩니다.")  # 전기차일 경우 정보 표시

# # ℹ️ **추가 정보 안내 마크다운**
# st.markdown("""
# ---
# ### 💬 **추가 정보**
# ✅ 비교하고 싶은 모델을 선택해 주세요. 
# ⚡ 전기차 모델의 경우 연비 대신 전기차로 표시됩니다.
# 💡 지원금 정보는 선택한 지역에 따라 달라질 수 있습니다.
# 🌐 언어 지원 기능 추가 예정입니다.
# """)  # 추가적인 안내 메시지를 마크다운 형식으로 출력


import streamlit as st
import plotly.graph_objects as go
import requests

url = 'http://127.0.0.1:8000/api'

# 데이터 불러오기
# 브랜드, 차량, 지역 데이터를 API에서 가져옵니다.
data = requests.get(url + '/brand-info').json()["resData"]
car_data = requests.get(url + '/car-info').json()["resData"]
regions = requests.get(url + '/region-info').json()["resData"]

# 페이지 설정 및 제목 출력
st.set_page_config(page_title="전기차 모델 비교", page_icon="🚗", layout="wide")
st.title("🔍 전기차 모델 성능 및 지원금 비교")

# ✅ [수정1] 다크 모드/라이트 모드 토글 추가 및 스타일 적용
theme_toggle = st.toggle("🌗 다크 모드 활성화", value=False)
if theme_toggle:
    st.markdown("""
    <style>
        .main, .block-container {
            background-color: #2E2E2E;
            color: white;
        }
        .stButton>button, .stSelectbox>div>div {
            color: white;
            background-color: #3E3E3E;
        }
    </style>
    """, unsafe_allow_html=True)

# ✅ [수정2] 자동차 비교 여부 토글 추가
compare = st.toggle("✨ 두 모델 비교", value=False)

# 선택 항목을 가로로 배치하여 첫 번째와 두 번째 자동차 선택 영역 구분
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 첫 번째 자동차 선택")
    selected_company1 = st.selectbox("**회사**", list(data.keys()), key="company1")
    selected_model1 = st.selectbox("**모델**", data[selected_company1], key="model1")
    selected_region1 = st.selectbox("**거주 지역**", list(regions.keys()), key="region1")

if compare:
    with col2:
        st.subheader("🚙 두 번째 자동차 선택")
        selected_company2 = st.selectbox("**비교 전기차 회사**", list(data.keys()), key="company2")
        selected_model2 = st.selectbox("**비교 전기차 모델**", data[selected_company2], key="model2")
        selected_region2 = st.selectbox("**거주 지역**", list(regions.keys()), key="region2")

# ✅ [수정3] 성능 세부 정보 표시 함수 개선 (header 반환 포함)
def display_car_info(model, region):
    model_info = requests.get(url + '/car-info', params={"car_name": model}).json()["resData"]
    header = model_info[0]
    values = model_info[1]
    result = {header[i]: values[i] for i in range(len(header))}

    with st.expander(f"🔎 {model} 상세 정보 보기"):
        # ✅ [수정4] 이미지 표시를 상세 정보 보기 내부로 이동
        st.image(result["IMG_URL"], caption=f"{model} 대표 이미지", use_container_width=True)

        # ✅ [수정5] 모든 차량 정보 동적 표시
        for key, value in result.items():
            if key != "IMG_URL":
                st.write(f"**{key}:** {value}")
    
    support = result["SUBSIDY"]
    return model_info, support, header

# ✅ [수정6] 첫 번째 자동차 선택 시 상세 정보 표시
if selected_model1 and selected_region1:
    model_info1, support1, header1 = display_car_info(selected_model1, selected_region1)

    # ✅ [수정7] 두 번째 모델 선택 시 지원금 비교 파이 차트 및 성능 비교 바 차트 생성
    if compare and selected_model2 and selected_region2:
        model_info2, support2, header2 = display_car_info(selected_model2, selected_region2)

        # 💰 지원금 비율 비교 파이 차트
        fig_pie = go.Figure(data=[go.Pie(labels=[selected_model1, selected_model2],
                                        values=[support1, support2],
                                        hole=.3)])
        fig_pie.update_layout(title_text="💰 지원금 비율 비교",
                              paper_bgcolor="#2E2E2E" if theme_toggle else "white",
                              font_color="white" if theme_toggle else "black")
        st.plotly_chart(fig_pie, use_container_width=True)

        # ✅ [수정8] 연비, 마력, 지원금 성능 비교 차트
        try:
            fig = go.Figure()
            fig.add_trace(go.Bar(name=selected_model1,
                                 x=["연비", "마력", "지원금"],
                                 y=[int(model_info1[1][header1.index("FUEL_EFFICIENCY")].replace("km/L", "")) if "km/L" in model_info1[1][header1.index("FUEL_EFFICIENCY")] else 0,
                                    int(model_info1[1][header1.index("MAX_DISTANCE")].replace("hp", "")),
                                    support1]))

            fig.add_trace(go.Bar(name=selected_model2,
                                 x=["연비", "마력", "지원금"],
                                 y=[int(model_info2[1][header2.index("FUEL_EFFICIENCY")].replace("km/L", "")) if "km/L" in model_info2[1][header2.index("FUEL_EFFICIENCY")] else 0,
                                    int(model_info2[1][header2.index("MAX_DISTANCE")].replace("hp", "")),
                                    support2]))

            fig.update_layout(barmode='group', title="🚀 모델 간 성능 및 지원금 비교",
                              xaxis_title="항목", yaxis_title="값",
                              paper_bgcolor="#2E2E2E" if theme_toggle else "white",
                              font_color="white" if theme_toggle else "black")
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"차트 생성 중 오류가 발생했습니다: {e}")

# 추가 정보 안내
st.markdown("""
---
### 💬 **추가 정보**
✅ 비교하고 싶은 모델을 선택해 주세요.  
⚡ 전기차 모델의 경우 연비 대신 전기차로 표시됩니다.  
💡 지원금 정보는 선택한 지역에 따라 달라질 수 있습니다.  
🌐 언어 지원 기능 추가 예정입니다.
""")
