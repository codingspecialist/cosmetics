# 화장품 데이터 수집

### 1. 설치
- python 설치

```txt
  pip install selenium
  pip install webdriver-manager
  pip install pandas
```

### 2. 크롤링 수집 방법
```txt
    # startCount = 0, 48, 96 (+48씩 되면서 페이징됨)
    # firstTotalCount = 202 (수분크림 검색시 전체 개수)
    # sort = WEIGHT/DESC,RNK/DESC (인기순)
    # sort = SALE_QTY/DESC (판매량순)
    # #w_cate_prd_list 4개씩 있음. 총 12개
```