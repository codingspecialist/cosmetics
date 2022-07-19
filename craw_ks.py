from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


driver = set_chrome_driver()
driver.get(
    "https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=수분크림&giftYn=N")
driver.implicitly_wait(3)

inner_err = 0
outer_err = 0

current_state = 1  # 외부 1, 내부 -1

for k in range(1, 10):
    prefix = f'#ajaxList > ul:nth-child({k})'
    for i in range(1, 10):
        try:
            print("outer", i)
            # ww1 = driver.find_element(
            #     by=By.CSS_SELECTOR, value=f'{prefix} > li:nth-child({i}) > div > a')
            # ww1.click()

            wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'{prefix} > li:nth-child({i}) > div > a'))).click()
            time.sleep(1)
            current_state = -1  # 내부 진입
            try:
                print("inner")

                wait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="buyInfo"]/a'))).click()
                time.sleep(1)

                ww2 = driver.find_element(By.XPATH,
                                          '//*[@id="buyInfo"]/a')  # xpath 로 접근
                sunang = ww2.find_element(By.XPATH,
                                          '//*[@id="artcInfo"]/dl[7]/dd')

                print(sunang.text)
                driver.back()
                time.sleep(1)
                current_state = 1  # 외부로 나옴
            except Exception as e:
                print("내부 예외 발생")
                print(e)
        except Exception as e:
            print("외부 예외 발생")
            print(f"현재 위치 {current_state}")
            print(e)

            if current_state == 1:
                break
            else:
                driver.back()
