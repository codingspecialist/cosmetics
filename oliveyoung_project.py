from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import parse_qs, urlparse
import time
import math

# https://www.google.com/intl/ko/chrome/beta/
# https://chromedriver.chromium.org/downloads
# https://www.oliveyoung.co.kr/store/search/getSearchMain.do?startCount=0&sort=RNK/DESC&goods_sort=WEIGHT/DESC,RNK/DESC&collection=ALL&realQuery={keyword}&reQuery=&viewtype=image&category=&catename=LCTG_ID&catedepth=1&rt=&setMinPrice=&setMaxPrice=&listnum=48&tmp_requery=&tmp_requery2=&categoryDepthValue=&cateId=&cateId2=&BenefitAll_CHECK=&query={keyword}&selectCateNm=전체&firstTotalCount=202&typeChk=list&branChk=&brandTop=&attrChk=&attrTop=&onlyOneBrand=&quickYn=N&cateChk=&benefitChk=&attrCheck0=&attrCheck1=&attrCheck2=&attrCheck3=&attrCheck4=&brandChkList=&benefitChkList=&_displayImgUploadUrl=https://image.oliveyoung.co.kr/uploads/images/display/&recobellMbrNo=null&recobellCuid=8b47cf9f-efd1-48e4-8f83-10ee8a07945b&sale_below_price=&sale_over_price=

# startCount = 0, 48, 96 (+48씩 되면서 페이징됨)
# firstTotalCount = 202 (전체 개수)
# sort = RNK/DESC (인기순)
# sort = SALE_QTY/DESC (판매량순)
# #w_cate_prd_list 4개씩 있음. 총 12개

startCount = 0
firstTotalCount = 0
sort = "RNK/DESC"
totalPageCount = 0
pageItemCount = 48
list = []


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    return driver

# def set_chrome_driver():
#     chrome_driver_path = "C:/workspace/ks_lab/chromedriver_win32/chromedriver.exe"
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = "C:/Program Files/Google/Chrome Beta/Application/chrome.exe"
#     chrome_options.add_experimental_option(
#         "excludeSwitches", ["enable-logging"])
#     driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)
#     return driver


def search_keyword(keyword):
    driver.get(
        f"https://www.oliveyoung.co.kr/store/search/getSearchMain.do?onlyOneBrand=&query={keyword}&listnum=24&giftYn=N")
    driver.implicitly_wait(3)


def convert_48():
    global firstTotalCount
    global totalPageCount
    while(True):
        try:
            wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#Contents > div.cate_align_box > div.count_sort.tx_num > ul > li:nth-child(3) > a"))).click()
            url = urlparse(driver.current_url)
            qs = parse_qs(url.query)
            firstTotalCount = int(qs["firstTotalCount"][0])
            totalPageCount = math.ceil(firstTotalCount/pageItemCount)
            break
        except Exception as e:
            print("3. view 48로 변경 오류")
            print(e)


def detail_view(outer_num, inner_num):
    while(True):
        try:
            wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"#ajaxList > ul:nth-child({outer_num}) > li:nth-child({inner_num}) a"))).click()
            break
        except Exception as e:
            print("4. #ajaxList 1~12번 ul에 1~4번 li에 a 찾아서 클릭하기 오류")
            print(e)


def buy_info():
    time.sleep(1)  # 구매정보 클릭전에 페이지 로드가 한번씩 늦어서 1초 쉬어주자!
    while(True):
        try:
            wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyInfo > a"))).click()
            break
        except Exception as e:
            print("5. 구매정보 클릭시 오류")
            print(e)


def craw_name():
    while(True):
        try:
            name_el = wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#Contents > div.prd_detail_box.renew > div.right_area > div > p.prd_name")))
            return name_el.text
        except Exception as e:
            print("6-1 제품명 오류")
            print(e)


def craw_type():
    while(True):
        try:
            type_el = wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#artcInfo > dl:nth-child(2) > dd")))
            return type_el.text
        except Exception as e:
            print("6-2 제품주요사양 오류")
            print(e)


def craw_sungbun():
    while(True):
        try:
            sungbun_el = wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#artcInfo > dl:nth-child(7) > dd")))
            sungbun_text = sungbun_el.text.replace(" ", "")
            sungbun_list = sungbun_text.split(",")
            return sungbun_list
        except Exception as e:
            print("6-3 모든 성분 오류")
            print(e)


def craw_data():
    data = {
        "name": craw_name(),
        "type": craw_type(),
        "sungbun": craw_sungbun()
    }
    return data


# 1. 크롬 브라우저 열기
driver = set_chrome_driver()

# 2. 수분크림 검색
search_keyword("수분크림")

# 3. view 48로 변경 후 firstTotalCount 확인하기
convert_48()

# 5. #ajaxList 1~12번 ul에 1~4번 li에 a 찾아서 클릭하기
for i in range(1, 12):
    for k in range(1, 4):
        detail_view(i, k)

        # 6. 구매정보 클릭하기
        buy_info()

        # 7. 제품주요사양, 제품이름, 성분 데이터 만들기 (딕셔너리)
        data = craw_data()
        list.append(data)

        # 8. 뒤로가기
        driver.back()

print(f"list의 크기 : {len(list)}")
print(list)
