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


def search_keyword(keyword):
    driver.get(
        f"https://www.oliveyoung.co.kr/store/search/getSearchMain.do?startCount=0&sort=RNK/DESC&goods_sort=WEIGHT/DESC,RNK/DESC&collection=ALL&realQuery={keyword}&reQuery=&viewtype=image&category=&catename=LCTG_ID&catedepth=1&rt=&setMinPrice=&setMaxPrice=&listnum=48&tmp_requery=&tmp_requery2=&categoryDepthValue=&cateId=&cateId2=&BenefitAll_CHECK=&query={keyword}&selectCateNm=전체&firstTotalCount=202&typeChk=list&branChk=&brandTop=&attrChk=&attrTop=&onlyOneBrand=&quickYn=N&cateChk=&benefitChk=&attrCheck0=&attrCheck1=&attrCheck2=&attrCheck3=&attrCheck4=&brandChkList=&benefitChkList=&_displayImgUploadUrl=https://image.oliveyoung.co.kr/uploads/images/display/&recobellMbrNo=null&recobellCuid=8b47cf9f-efd1-48e4-8f83-10ee8a07945b&sale_below_price=&sale_over_price=")
    driver.implicitly_wait(3)


# 1. 크롬 브라우저 열기
driver = set_chrome_driver()

# 2. 수분크림 검색
search_keyword("수분크림")

# 3. 격자형식에서 리스트 형식으로 보기
while(True):
    try:
        wait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#Contents > div.cate_align_box > div.type_sort > button.btn_list"))).click()
        break
    except:
        print("3. 격자형식에서 리스트 형식으로 보기 오류")
        pass

# 4. #ajaxList 1~12번 ul에 1~4번 li에 a 찾아서 클릭하기
while(True):
    try:
        wait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ajaxList > ul:nth-child(1) > li:nth-child(1) a"))).click()
        break
    except:
        print("4. #ajaxList 1~12번 ul에 1~4번 li에 a 찾아서 클릭하기 오류")
        pass


# 5. 구매정보 클릭하기
while(True):
    try:
        wait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyInfo > a"))).click()
        break
    except:
        print("5. 구매정보 클릭시 오류")
        pass


# 6. 제품주요사양, 제품이름, 성분 데이터 만들기 (딕셔너리)

# 6-1 제품명
while(True):
    try:
        name_el = wait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#Contents > div.prd_detail_box.renew > div.right_area > div > p.prd_name")))
        print(name_el.text)
        break
    except:
        print("6-1 제품명 오류")
        pass


# 6-2 제품주요사양
while(True):
    try:
        type_el = wait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#artcInfo > dl:nth-child(2) > dd")))
        print(type_el.text)
        break
    except:
        print("6-2 제품주요사양 오류")
        pass


# 6-3 모든 성분
while(True):
    try:
        sungbun_el = wait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#artcInfo > dl:nth-child(7) > dd")))
        sungbun_text = sungbun_el.text.replace(" ", "")
        sungbun_list = sungbun_text.split(",")
        print(sungbun_list)
        break
    except:
        print("6-3 모든 성분 오류")
        pass


# 7. 뒤로가기
driver.back()
