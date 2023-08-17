from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# https://www.google.com/intl/ko/chrome/beta/
# https://chromedriver.chromium.org/downloads
# https://www.oliveyoung.co.kr/store/search/getSearchMain.do?startCount=0&sort=RNK/DESC&goods_sort=WEIGHT/DESC,RNK/DESC&collection=ALL&realQuery={keyword}&reQuery=&viewtype=image&category=&catename=LCTG_ID&catedepth=1&rt=&setMinPrice=&setMaxPrice=&listnum=48&tmp_requery=&tmp_requery2=&categoryDepthValue=&cateId=&cateId2=&BenefitAll_CHECK=&query={keyword}&selectCateNm=전체&firstTotalCount=202&typeChk=list&branChk=&brandTop=&attrChk=&attrTop=&onlyOneBrand=&quickYn=N&cateChk=&benefitChk=&attrCheck0=&attrCheck1=&attrCheck2=&attrCheck3=&attrCheck4=&brandChkList=&benefitChkList=&_displayImgUploadUrl=https://image.oliveyoung.co.kr/uploads/images/display/&recobellMbrNo=null&recobellCuid=8b47cf9f-efd1-48e4-8f83-10ee8a07945b&sale_below_price=&sale_over_price=

# startCount = 0, 48, 96 (+48씩 되면서 페이징됨)
# firstTotalCount = 202 (전체 개수)
# sort = WEIGHT/DESC,RNK/DESC (인기순)
# sort = SALE_QTY/DESC (판매량순)
# #w_cate_prd_list 4개씩 있음. 총 12개


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


def search_keyword(startCount, keyword, sort):
    driver.get(
        f"https://www.oliveyoung.co.kr/store/search/getSearchMain.do?startCount={startCount}&sort={sort}&goods_sort={sort}&collection=ALL&realQuery={keyword}&reQuery=&viewtype=image&category=&catename=LCTG_ID&catedepth=1&rt=&setMinPrice=&setMaxPrice=&listnum=48&tmp_requery=&tmp_requery2=&categoryDepthValue=&cateId=&cateId2=&BenefitAll_CHECK=&query={keyword}&selectCateNm=전체&typeChk=list&branChk=&brandTop=&attrChk=&attrTop=&onlyOneBrand=&quickYn=N&cateChk=&benefitChk=&attrCheck0=&attrCheck1=&attrCheck2=&attrCheck3=&attrCheck4=&brandChkList=&benefitChkList=&_displayImgUploadUrl=https://image.oliveyoung.co.kr/uploads/images/display/&recobellMbrNo=null&recobellCuid=8b47cf9f-efd1-48e4-8f83-10ee8a07945b&sale_below_price=&sale_over_price=")
    driver.implicitly_wait(3)


def detail_view(outer_num, inner_num):
    tryCount = 0
    while(True):
        try:
            tryCount = tryCount + 1
            wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"#ajaxList > ul:nth-child({outer_num}) > li:nth-child({inner_num}) a"))).click()
            return 1
        except Exception as e:
            print("#ajaxList 1~12번 ul에 1~4번 li에 a 찾아서 클릭하기 오류")
            print(e)
            if tryCount == 2:
                return -1


def buy_info():
    tryCount = 0
    time.sleep(1)  # 구매정보 클릭전에 페이지 로드가 한번씩 늦어서 1초 쉬어주자!
    while(True):
        try:
            tryCount = tryCount + 1
            wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyInfo > a"))).click()
            return 1
        except Exception as e:
            print("구매정보 클릭시 오류")
            print(e)
            if tryCount == 2:
                return -1


def craw_name():
    tryCount = 0
    while(True):
        try:
            tryCount = tryCount + 1
            name_el = wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#Contents > div.prd_detail_box.renew > div.right_area > div > p.prd_name")))
            return name_el.text
        except Exception as e:
            print("제품명 오류")
            print(e)
            if tryCount == 2:
                return ""


def craw_type():
    tryCount = 0
    while(True):
        try:
            tryCount = tryCount + 1
            type_el = wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#artcInfo > dl:nth-child(2) > dd")))
            return type_el.text
        except Exception as e:
            print("제품주요사양 오류")
            print(e)
            if tryCount == 2:
                return ""


def craw_sungbun():
    tryCount = 0
    while(True):
        try:
            tryCount = tryCount + 1
            sungbun_el = wait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#artcInfo > dl:nth-child(8) > dd")))
            sungbun_text = sungbun_el.text.replace(" ", "")
            sungbun_list = sungbun_text.split(",")
            sungbun_list.sort()
            return sungbun_list
        except Exception as e:
            print("모든 성분 오류")
            print(e)
            if tryCount == 2:
                return []


def craw_data():
    data = {
        "name": craw_name(),
        "type": craw_type(),
        "sungbun": craw_sungbun()
    }
    return data


# 화장품 데이터 수집 시작
driver = set_chrome_driver()
list = []
startCount = 144
keyword = "수분크림"
sort = "WEIGHT/DESC,RNK/DESC"

isContinue = True

while(isContinue):

    search_keyword(startCount, keyword, sort)

    for i in range(1, 13):  # 행
        for k in range(1, 5):  # 열
            print(f"{i}행, {k}열")

            # 상세보기 클릭하기
            step1 = detail_view(i, k)
            if step1 == -1:
                isContinue = False
                break

            # 구매정보 클릭하기
            step2 = buy_info()
            if step2 == -1:
                driver.back()
                continue

            # 제품주요사양, 제품이름, 성분 데이터 만들기 (딕셔너리)

            data = craw_data()
            list.append(data)

            # 뒤로가기
            driver.back()

        if isContinue == False:
            break
    startCount = startCount + 48

print(f"list의 크기 : {len(list)}")
print(list)

# CSV 파일로 저장
