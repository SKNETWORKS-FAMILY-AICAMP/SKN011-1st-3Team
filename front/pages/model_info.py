import streamlit as st
import plotly.graph_objects as go
import os

# 자동차 데이터 예시
data = {
    "현대": ["아반떼", "쏘나타", "팰리세이드"],
    "기아": ["K5", "K7", "스포티지"],
    "테슬라": ["모델3", "모델Y", "모델S"]
}

# 성능 및 지원금 정보 예시
performance_data = {
    "아반떼": {"연비": "15km/L", "마력": "123hp", "지원금": {"서울": 100, "경기": 80}},
    "쏘나타": {"연비": "12km/L", "마력": "160hp", "지원금": {"서울": 120, "경기": 90}},
    "팰리세이드": {"연비": "9km/L", "마력": "277hp", "지원금": {"서울": 150, "경기": 100}},
    "K5": {"연비": "14km/L", "마력": "150hp", "지원금": {"서울": 110, "경기": 85}},
    "K7": {"연비": "11km/L", "마력": "180hp", "지원금": {"서울": 130, "경기": 95}},
    "스포티지": {"연비": "13km/L", "마력": "200hp", "지원금": {"서울": 140, "경기": 105}},
    "모델3": {"연비": "전기차", "마력": "283hp", "지원금": {"서울": 200, "경기": 150}},
    "모델Y": {"연비": "전기차", "마력": "345hp", "지원금": {"서울": 250, "경기": 170}},
    "모델S": {"연비": "전기차", "마력": "670hp", "지원금": {"서울": 300, "경기": 200}},
}

# 지역 목록
regions = ["서울", "경기", "강원", "충청", "전라", "경상"]

st.set_page_config(page_title="전기차 모델 비교", page_icon="🚗", layout="wide")
st.title("🔍 전기차 모델 성능 및 지원금 비교")

# 다크 모드/라이트 모드 토글
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

# 모델별 대표 이미지 표시 (로컬 이미지 경로 사용)
def show_car_image(model):
    base_path = os.path.dirname(__file__)  
    image_paths = {
        "아반떼": os.path.join(base_path, "images/avante.gif"),
        "쏘나타": os.path.join(base_path, "images/sonata.gif"),
        "팰리세이드": os.path.join(base_path, "images/palisade.jpg"),
        "K5": os.path.join(base_path, "images/k5.jpg"),
        "K7": os.path.join(base_path, "images/k7.jpg"),
        "스포티지": os.path.join(base_path, "images/sportage.jpg"),
        "모델3": os.path.join(base_path, "images/model3.jpg"),
        "모델Y": os.path.join(base_path, "images/modely.jpg"),
        "모델S": os.path.join(base_path, "images/models.jpg"),
    }
    image_path = image_paths.get(model, None)
    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=f"{model} 대표 이미지", use_container_width=True)
    else:
        st.warning(f"❗ {model}에 대한 로컬 이미지를 찾을 수 없습니다.")

# 자동차 비교 여부 선택
compare = st.toggle("✨ 두 모델 비교", value=False)

# 선택 항목을 가로로 배치
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 첫 번째 자동차 선택")
    selected_company1 = st.selectbox("**회사**", list(data.keys()), key="company1")
    selected_model1 = st.selectbox("**모델**", data[selected_company1], key="model1")
    selected_region1 = st.selectbox("**거주 지역**", regions, key="region1")
    show_car_image(selected_model1)

if compare:
    with col2:
        st.subheader("🚙 두 번째 자동차 선택")
        selected_company2 = st.selectbox("**비교 전기차 회사**", list(data.keys()), key="company2")
        selected_model2 = st.selectbox("**비교 전기차 모델**", data[selected_company2], key="model2")
        selected_region2 = st.selectbox("**거주 지역**", regions, key="region2")
        show_car_image(selected_model2)

# 성능 세부 정보 확장 기능
def display_car_info(model, region):
    model_info = performance_data.get(model, {})
    support = model_info.get("지원금", {}).get(region, "지원금 정보 없음")
    with st.expander(f"🔎 {model} 상세 정보 보기"):
        st.success(f"💡 **연비:** {model_info.get('연비', '정보 없음')}")
        st.info(f"⚡ **마력:** {model_info.get('마력', '정보 없음')}")
        st.warning(f"💸 **{region} 지역 지원금:** {support}만원")
    return model_info, support

if selected_model1 and selected_region1:
    model_info1, support1 = display_car_info(selected_model1, selected_region1)

    if compare and selected_model2 and selected_region2:
        model_info2, support2 = display_car_info(selected_model2, selected_region2)

        # 지원금 비율 파이 차트 추가
        fig_pie = go.Figure(data=[go.Pie(labels=[selected_model1, selected_model2],
                                        values=[support1, support2],
                                        hole=.3)])
        fig_pie.update_layout(title_text="💰 지원금 비율 비교",
                              paper_bgcolor="#2E2E2E" if theme_toggle else "white",
                              font_color="white" if theme_toggle else "black")
        st.plotly_chart(fig_pie, use_container_width=True)

        # 성능 비교 차트
        if model_info1.get("연비") != "전기차" and model_info2.get("연비") != "전기차":
            fig = go.Figure()
            fig.add_trace(go.Bar(name=selected_model1,
                                 x=["연비 (km/L)", "마력 (hp)", "지원금 (만원)"],
                                 y=[int(model_info1["연비"].replace("km/L", "")),
                                    int(model_info1["마력"].replace("hp", "")),
                                    support1]))
            fig.add_trace(go.Bar(name=selected_model2,
                                 x=["연비 (km/L)", "마력 (hp)", "지원금 (만원)"],
                                 y=[int(model_info2["연비"].replace("km/L", "")),
                                    int(model_info2["마력"].replace("hp", "")),
                                    support2]))
            fig.update_layout(barmode='group', title="🚀 모델 간 성능 및 지원금 비교",
                              xaxis_title="항목", yaxis_title="값",
                              paper_bgcolor="#2E2E2E" if theme_toggle else "white",
                              font_color="white" if theme_toggle else "black")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("⚡ 전기차 모델은 연비가 다르게 표시됩니다.")

st.markdown("""
---
### 💬 **추가 정보**
✅ 비교하고 싶은 모델을 선택해 주세요. 
⚡ 전기차 모델의 경우 연비 대신 전기차로 표시됩니다.
💡 지원금 정보는 선택한 지역에 따라 달라질 수 있습니다.
🌐 언어 지원 기능 추가 예정입니다.
""")
