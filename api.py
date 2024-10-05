
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import calendar

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  


chrome_service = ChromeService(executable_path='D:/chrome/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

base_url = "https://meteostat.net/en/place/vn/quan-tan-phu?s=48900&t={}-{:02d}-{:02d}/{:02d}-{:02d}-{:02d}"


start_year = 1990
start_month = 1
start_day = 1


for year in range(start_year, 2025):  
    if year == start_year:
        month_range = range(start_month, 13)  
        day_range = range(start_day, calendar.monthrange(year, start_month)[1] + 1)  
    else:
        month_range = range(1, 13)  
        day_range = range(1, 32)  

    for month in month_range:
   
        num_days = calendar.monthrange(year, month)[1]
        
        for day in day_range:
            if day > num_days:
                continue  
            
 
            url = base_url.format(year, month, day, year, month, day)
            print(f"Đang crawl dữ liệu cho ngày: {year}-{month:02d}-{day:02d}")

            driver.get(url)

            try:
                accept_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-dismiss='modal' and text()='Accept']"))
                )
                accept_button.click()
                print("Đã xử lý modal 'Privacy Notice'")
            except Exception as e:
                print("Không tìm thấy modal 'Privacy Notice':", e)

            try:
                modal_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@data-bs-toggle='modal']"))
                )
                modal_button.click()  
                print("Đã click mở modal")
            except Exception as e:
                print("Không tìm thấy nút button có data-bs-toggle='modal':", e)

            try:
                save_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))
                )
                save_button.click() 
                print("Đã click nút 'Save'")
            except Exception as e:
                print("Không tìm thấy nút 'Save':", e)



driver.quit()
print("Quá trình crawl đã hoàn tất.")
