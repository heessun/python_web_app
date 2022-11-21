import sys
import io
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# chrome_options = Options()
# #chrome_options.add_argument("--headless")
# chrome_options.add_argument('--log-level=3')
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:/section3/webdriver/chrome/chromedriver')
driver = webdriver.Chrome('C:/Users/heesun_estsecurity/Desktop/autotest/inflearn/webcrawling/webdriver/chrome/chromedriver')

driver.set_window_size(1920, 1280)
driver.implicitly_wait(3)
#driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F')
driver.get('https://account.wishket.com/wishket-member/login/?next=/')

time.sleep(5)
driver.implicitly_wait(3)

driver.find_element_by_name('username').send_keys('test_heesun')

driver.implicitly_wait(3)
driver.find_element_by_name('password').send_keys('estsoft1!')

driver.implicitly_wait(3)
# 로그인
driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
