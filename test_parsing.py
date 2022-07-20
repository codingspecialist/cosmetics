from urllib.parse import parse_qs, urlparse

str = "https://www.oliveyoung.co.kr/store/search/getSearchMain.do?startCount=0&sort=RNK%2FDESC&goods_sort=WEIGHT%2FDESC%2CRNK%2FDESC&collection=ALL&realQuery=%EC%88%98%EB%B6%84%ED%81%AC%EB%A6%BC&reQuery=&viewtype=image&category=&catename=LCTG_ID&catedepth=1&rt=&setMinPrice=&setMaxPrice=&listnum=48&tmp_requery=&tmp_requery2=&categoryDepthValue=&cateId=&cateId2=&BenefitAll_CHECK=&query=%EC%88%98%EB%B6%84%ED%81%AC%EB%A6%BC&selectCateNm=%EC%A0%84%EC%B2%B4&firstTotalCount=202&typeChk=thum&branChk=&brandTop=&attrChk=&attrTop=&onlyOneBrand=&quickYn=N&cateChk=&benefitChk=&attrCheck0=&attrCheck1=&attrCheck2=&attrCheck3=&attrCheck4=&brandChkList=&benefitChkList=&_displayImgUploadUrl=https%3A%2F%2Fimage.oliveyoung.co.kr%2Fuploads%2Fimages%2Fdisplay%2F&recobellMbrNo=null&recobellCuid=8b47cf9f-efd1-48e4-8f83-10ee8a07945b&sale_below_price=&sale_over_price="

url = urlparse(str)

qs = parse_qs(url.query)

print(qs["firstTotalCount"][0])
