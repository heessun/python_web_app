import urllib.request as req
import os.path, random
import simplejson as json   #simplejson 으로 성능 강화 계속 업데이트

#URL
url = "https://api.github.com/repositories"   #json데이터

#경로 & 파일명
savename = "c:/section4/repo.json"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

items = json.load(open(savename, "r", encoding="utf-8"))
#items = json.loads(open(savename, "r", encoding="utf-8").read())

print(items)

# 출력
for item in items:    #저장소 단위별  #dict 확인
    print(item["full_name"] + " - " + item["owner"]["url"])  #object, object
