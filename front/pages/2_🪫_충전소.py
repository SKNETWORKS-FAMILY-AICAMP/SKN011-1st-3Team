import streamlit as st
import pandas as pd
import plotly.express as px
import os
import requests
import pandas as pd
import plotly.express as px
import streamlit as st

# CSV 데이터 로드 (지정된 경로에서 로드)
def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "csv", "example_1.csv")
    return pd.read_csv(file_path)
url = 'http://127.0.0.1:8000/api'
data  = requests.get(url + '/chargeStatistics').json()["resData"]

# for idx,item in enumerate(new_data):
#     if idx ==1:
        



st.set_page_config(page_title="전국 전기차 충전소 현황", page_icon="⚡", layout="wide")
st.title("⚡전국 전기차 충전소 현황⚡")



# DataFrame 생성 (헤더는 첫 행, 데이터는 그 이후 행)
df = pd.DataFrame(data[1:], columns=data[0])

# DataFrame을 wide format에서 long format으로 변환
# REGOIN_NAME는 그대로 두고, 충전기 종류별 컬럼을 CHARGE_TYPE, 수량을 '수량' 컬럼으로 변환합니다.
df_long = pd.melt(
    df,
    id_vars=["REGOIN_NAME"],
    value_vars=["AC_COUNT", "DC_COUNT", "SUPERCHARGER_COUNT", "FAST_CHARGER_COUNT", "SLOW_CHARGER_COUNT"],
    var_name="CHARGE_TYPE",
    value_name="수량"
)

# AC와 DC 데이터만 따로 추출
ac_data = df_long[df_long["CHARGE_TYPE"] == "AC_COUNT"]
dc_data = df_long[df_long["CHARGE_TYPE"] == "DC_COUNT"]

# 예를 들어 도시별 총합을 구해서 파이 차트를 만든다면:
# (피벗 전 데이터가 도시별로 나누어져 있으므로, 그룹화(groupby)로 합계를 구할 수 있습니다.)
ac_counts = ac_data.groupby("REGOIN_NAME")["수량"].sum().reset_index()
dc_counts = dc_data.groupby("REGOIN_NAME")["수량"].sum().reset_index()

# 레이아웃 컬럼 예시
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔌 AC 충전기 타입 분포")
    fig_ac_pie = px.pie(ac_counts, names="REGOIN_NAME", values="수량", title="AC 충전기 도시별 분포")
    st.plotly_chart(fig_ac_pie, use_container_width=True)

with col2:
    st.subheader("⚡ DC 충전기 타입 분포")
    fig_dc_pie = px.pie(dc_counts, names="REGOIN_NAME", values="수량", title="DC 충전기 도시별 분포")
    st.plotly_chart(fig_dc_pie, use_container_width=True)


# 전국 AC/DC 타입 현황 및 급속/완속 타입 현황 (가로 바 차트로 변경, 바 크기 더 얇게 조정)
st.header("🔌 전국 충전기 타입 현황")

left_column,right_column = st.columns(2)
pt_data = pd.DataFrame(data[1:], columns=data[0])
pt_data = pt_data.rename(columns={
    'REGOIN_NAME': '도',
    'AC_COUNT': 'AC 수량',
    'DC_COUNT': 'DC 수량',
    'FAST_CHARGER_COUNT': '고속 충전기 수',
    'SLOW_CHARGER_COUNT': '완속 충전기 수'
})

with left_column:
    st.caption('도별 AC와 DC 충전기 수 비교표')
    st.bar_chart(pt_data, x='도', y=['AC 수량', 'DC 수량'])
    
with right_column:
    st.caption('도별 고속, 완속 충전기 수 비교표')
    st.bar_chart(pt_data, x='도', y=['고속 충전기 수', '완속 충전기 수'])

# 시만 선택할 수 있도록 토글 기능 단순화
# st.header("📍 지역별 상세 충전소 정보 보기 (시 단위)")

# regionData = requests.get(url + '/region-info').json()["resData"]
# print(regionData)

# region_dict = data["주소"].apply(lambda x: x.split()[0]).unique().tolist()

# selected_region = st.selectbox('지역을 선택하세요', list(region_dict.keys()))

# if selected_region:
#     # API URL 설정 (url 변수는 미리 정의했다고 가정)
#     api_url = url + '/charge-search'
    
#     response = requests.get(api_url, params={"car_name": selected_region})
#     print(response)
#     # 응답 JSON에서 "resData" 키의 데이터를 가져옴
#     charge_data = response.json()["resData"]
    
#     # API 응답 데이터를 DataFrame으로 변환
#     charge_df = pd.DataFrame(charge_data)
    
#     # "주소" 컬럼에 선택된 지역명이 포함된 행만 필터링하여 "충전소", "주소" 컬럼만 선택
#     filtered_data = charge_df[charge_df["주소"].str.contains(selected_region)][["충전소", "주소"]]
    
#     st.subheader(f"🔎 {selected_region}의 충전소 목록")
#     st.dataframe(filtered_data.reset_index(drop=True), use_container_width=True)