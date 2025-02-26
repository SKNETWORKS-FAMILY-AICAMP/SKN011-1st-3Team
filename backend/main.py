from fastapi import FastAPI,Query
import re
import subprocess
import json
from data_search import equal_serach,search_all
app = FastAPI()


@app.post("/api")
async def get_car_subsidy_info(car_code: str = Query(None), sido: str = Query(None)):
    url = f"https://auto.danawa.com/service/ajax_estimate_EVSigungu.php?trims={car_code}&sido={sido}&option="
    headers = "-H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'"
    curl_cmd = f"curl -k {headers} '{url}'"
    pattern = r"<option[^>]*\svalue=['\"](.*?)['\"][^>]*\sdata-price=['\"](.*?)['\"][^>]*\sdata-remaincount=['\"](.*?)['\"][^>]*>(.*?)</option>"
    result = subprocess.run(curl_cmd, shell=True, capture_output=True, text=True)

    matches = re.findall(pattern, result.stdout, re.DOTALL)

    result = []
    for value, data_price, data_remaincount, text in matches:
        result.append({
            "value": value,
            "data_price": data_price,
            "data_remaincount": data_remaincount,
            "text": text.strip()
        })
    return {"code":200,"resData":result}
@app.get("/api/car-info")
async def get_car_info(car_name: str = Query(None)):
    res_data = equal_serach('CAR','MODEL_NAME',car_name)
    return {"code":200,"resData":res_data}

@app.get("/api/chargeStatistics")
async def get_charge_Statistics():
    res_data = search_all('CHARGE_STATISTICS')
    return {"code":200,"resData":res_data}

@app.get('/api/region-info')
async def get_region_info():
    res_data = search_all('REGION')
    return {"code":200,"resData":res_data}