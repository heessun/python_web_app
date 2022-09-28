import urllib.request
import urllib.parse


API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

values = {
    'stnId': '109',
}

print('before', values)
params = urllib.parse.urlencode(values)
print('after', params)
url = API+"?"+params
print("요청 URL : ", url)


f = urllib.request.urlopen(url).read()

savePath = "C:/weather_seoulgyeonggido.xml"

# saveFile = open(savePath,'wb') # w : write , wb : write_byte, r : read , a : add
# saveFile.write(f)
# saveFile.close()

with open(savePath, 'wb') as saveFile:
    saveFile.write(f)

print('다운로드 완료')
