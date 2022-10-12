from bs4 import BeautifulSoup
import urllib.request as req


url = "http://finance.naver.com/sise/"



res = req.urlopen(url).read().decode('cp949')  # utf-8 : 한글 깨짐, unicode_escape : 한글 깨짐
# 중간 출력
print(res)

soup = BeautifulSoup(res, "html.parser")
print(soup)

top10 = soup.select("#popularItemList > li > a")
# 파싱 확인
print(top10)

print('네이버 주식 인기검색 종목 10위')
for i, e in enumerate(top10, 1):
    print('순위 : {}, 이름 : {}'.format(i, e.string))
