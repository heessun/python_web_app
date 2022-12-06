from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#지역별 최저온도 출력

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "C:/section4/forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)  #url데이터가져오기

# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')  #xml데이터형식파서사용 #태그이용하기위함

# 지역 확인
info = {}
for location in soup.find_all("location"):
    loc = location.find('city').string
    #print(loc)
    weather = location.find_all('tmn')
    #print(weather)
    if not (loc in info):   #혹시 city이름이 중복되있을 경우도 있을 수 있으니..
        info[loc] = []     #Dictionary key를 만들고 값은 [] 빈리스트를 만든다
    for tmn in weather:
        info[loc].append(tmn.string)   #Dictionary 값 넣기

print(info)

# 각 지역의 날씨 출력
with open('C:/section4/forecast.txt', "wt", encoding="utf-8") as f:
    for loc in sorted(info.keys()):   #Dictionary는 순서가 없기때문에 sorted(글자순) > list 식으로 바꿈
        print("+", loc)
        f.write(str(loc)+'\n')
        for name in info[loc]:
            print(" - ", name)
            f.write('\t'+str(name)+'\n')
