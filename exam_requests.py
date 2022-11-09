from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


#요청 URL
URL = 'https://account.wishket.com/wishket-member/login/?next=/'

#Fake User-Agent 생성
ua = UserAgent()

#print(ua.ie)
#print(ua.chrome)
#print(ua.random)

with requests.Session() as s:
    #URL연결
    s.get(URL)
    #Login 정보 Payload
    LOGIN_INFO = {
        'identification': 'test_heesun',
        'password': 'estsoft1!',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    print('token', s.cookies['csrftoken'])
    #요청
    response = s.post(URL,data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome), 'Referer':'https://account.wishket.com/wishket-member/login/?next=/'})
    #HTML 결과 확인
    print('response',response.text)
    if response.status_code == 200 and response.ok: #200 정상 #404 없음 #403 거절  #500 서버에러
        soup = BeautifulSoup(response.text,'html.parser')
        #projectList = soup.select("table.table-responsive > tbody > tr")
        #print(soup)
        projectList = soup.select("div.user-project>div")
        #print(soup.select_one("div.user-project").string)
        print(projectList)
        for i in projectList:
            print(i.text)
            #print(i.find('div').string,i.find('p').text)
