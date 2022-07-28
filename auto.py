import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

s = Service("D:\chromeDriver\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.get('https://cas.sustech.edu.cn/cas/login?service=https://openlab.sustech.edu.cn/PassPort/Cas/Login?serviceURL=https://openlab.sustech.edu.cn/Console/Account/Login?topLogin=1')
browser.implicitly_wait(5)

# 登录,
username = "xxxxxxx"
password = "xxxxxxxx"
Name = "多尺度高分辨缺陷分析扫描电子显微镜"
acc_input = browser.find_element(By.XPATH, '//*[@id="username"]')
acc_input.send_keys(username)
pwd_input = browser.find_element(By.XPATH, '//*[@id="password"]')
pwd_input.send_keys(password)
browser.find_element(By.XPATH, '//*[@id="fm1"]/span/button/span').click()

# 工作台
browser.find_element(By.XPATH, '//*[@id="changeItem"]/span/i').click()
browser.find_element(By.XPATH, '//*[@id="changeItem"]/div/li/a/div').click()
# 获取当前打开的全部窗口并切换窗口
handles = browser.window_handles
browser.switch_to.window(handles[1])
# 选择电镜+点击预约按钮   悬停显示+点击
ActionChains(browser).move_to_element\
    (browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div')).perform()
browser.find_element\
    (By.XPATH, '//*[@id="main"]/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[4]/div/span/span/a[1]').click()


browser.find_element(By.CLASS_NAME,"txt.next-btn").click()# 下周

# 机时选择
browser.execute_script('window.scrollBy(0, 300)')
time.sleep(0.5)
js = "document.getElementById('mCSB_3_container').style.top = '-700px'"
browser.execute_script(js)
target_date = str(datetime.date.today() + datetime.timedelta(days=7))
timeIDArr = [target_date + ' 14:00:00', target_date + ' 15:00:00', target_date + ' 16:00:00']
for timeID in timeIDArr:
    browser.find_element(By.ID, timeID).click()
# 下一步,下一步
browser.find_element(By.XPATH, '//*[@id="nextStep"]').click()
time.sleep(0.005)
browser.find_element(By.XPATH, '//*[@id="nextStep2"]').click()
time.sleep(0.002)
browser.execute_script('window.scrollBy(0, 230)')
browser.find_element(By.XPATH, '//*[@id="stepWrap"]/div[3]/div[3]/div/div[1]/div[4]/div/i').click()
time.sleep(0.002)
browser.find_element(By.XPATH, '//*[@id="submitBooking"]').click()
browser.quit()