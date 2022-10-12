from bs4 import BeautifulSoup
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

fp = open("food-list.html", "rt", encoding="utf-8").read()

#print(fp)

# html = """<html>
# <body>
# <div id="foods">
#   <h1>안주 및 주류</h1>
#   <ul id="fd-list">
#     <li class="food hot" data-lo="ko">닭도리탕</li>
#     <li class="food" data-lo="jp">돈까스</li>
#     <li class="food hot" data-lo="ko">삼겹살</li>
#     <li class="food" data-lo="us">스테이크</li>
#   </ul>
#   <ul id="ac-list">
#     <li class="alcohol" data-lo="ko">소주</li>
#     <li class="alcohol" data-lo="us">맥주</li>
#     <li class="alcohol" data-lo="ko">막걸리</li>
#     <li class="alcohol high" data-lo="cn">양주</li>
#     <li class="alcohol" data-lo="ko">동동주</li>
#   </ul>
# </div>
# <body>
# </html>"""

soup = BeautifulSoup(fp, "html.parser")
print(soup.prettify())

print("1", soup.select("li:nth-of-type(8)")[0].string) #각 li 태그 그룹의 nth-of-type (css 인자) 8번째 요소 선택
print("2", soup.select_one("#ac-list > li:nth-of-type(4)").string)  # id(#)  
print("3", soup.select("#ac-list > li[data-lo='cn']")[0].string) #li 태그중에 요소 data-lo 값이 cn 인 경우
print("4", soup.select("#ac-list > li.alcohol.high")[0].string) #li 태그중에 .(클래스) alcohol.high 

param = {"data-lo": "cn", "class": "alcohol"}
print("5", soup.find("li", param).string)
print("6", soup.find(id="ac-list").find("li",param).string)

for ac in soup.find_all("li"):
    print(ac)
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
