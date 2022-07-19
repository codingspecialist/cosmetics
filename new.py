from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver


driver = set_chrome_driver()

driver.get("https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000166641&dispCatNo=1000001000100090002&trackingCd=Result_1")
driver.implicitly_wait(3)

ww = driver.find_element_by_xpath(
    '//*[@id="buyInfo"]/a')  # xpath 로 접근


ww.click()

sunang = ww.find_element_by_xpath('//*[@id="artcInfo"]/dl[7]/dd')

print(sunang.text)
