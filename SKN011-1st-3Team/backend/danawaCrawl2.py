from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

url = 'https://auto.danawa.com/compare/?Codes='

driver.get(url)
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.buttonAddComp")))

btnContainer = driver.find_elements(By.CSS_SELECTOR,"div.buttonAddComp")

brandObj = {

}


for container in btnContainer:
    add_btn = container.find_element(By.CSS_SELECTOR,".button")
    if add_btn.text == '추가하기':
        add_btn.click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".brand__group")))    
        brand_container = driver.find_elements(By.CSS_SELECTOR,".brand__group")
        for brand in brand_container:
            brand_name_ct = brand.find_elements(By.CSS_SELECTOR,".brand__item")
            brandObj =  brandObj | {brand.text.strip(): {} for brand in brand_name_ct if brand.text.strip()}
            for item in brand_name_ct:
                brandObj[item.text]["brand_code"] = item.get_attribute('data-brand')
            

            # for brand in brand_name_ct:
            #     brand_text = brand.text.strip()
            #     if brand_text:
            #         brand.click()
            #         wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".classify__model")))
            #         car_list = driver.find_elements(By.CSS_SELECTOR, ".classify__model")
            #         brandObj[brand_text] = {car.text.strip(): {} for car in car_list if car.text.strip()}
            #         driver.execute_script("javascript:openAutoTab('brand');")
            #     print(brandObj)
        
    break
print(brandObj)
    


