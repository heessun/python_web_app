import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#CLI(Command-Line Interface) 환경으로 만들기 #웹페이지 보여지지 않음
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/Users/heesun_estsecurity/Desktop/autotest/inflearn/webcrawling/webdriver/chrome/chromedriver')
#driver = webdriver.Chrome('C:/Users/heesun_estsecurity/Desktop/autotest/inflearn/webcrawling/webdriver/chrome/chromedriver')

driver.set_window_size(1920, 1280)
#driver.implicitly_wait(5)

driver.get('https://google.com')

driver.save_screenshot("c:/Website1_ch.png")

#driver.implicitly_wait(5)

driver.get('https://www.daum.net')

#driver.implicitly_wait(5)

driver.save_screenshot("c:/Website2_ch.png")

#driver.implicitly_wait(5)

driver.quit()
