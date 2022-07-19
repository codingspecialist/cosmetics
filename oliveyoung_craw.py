import requests
from bs4 import BeautifulSoup

# 1. requests 모듈로 데이터 다운받기
url = "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000161890&dispCatNo=1000001000400080001&trackingCd=Result_11_30"
response = requests.get(url)
parseResponse = response.json()


ob = BeautifulSoup(parseResponse, "html.parser")
kk = ob.select(".detail_info_list")
# print(kk)
