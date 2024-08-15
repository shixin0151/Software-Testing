import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 初始化WebDriver
driver = webdriver.Chrome()

# 1. 打开12306官网
driver.get("https://www.12306.cn/index/")

# 2. 点击登录按钮
login_button = driver.find_element(By.LINK_TEXT, "登录")
login_button.click()

# 3. 输入用户名
username_field = driver.find_element(By.ID, "J-userName")
username_field.send_keys("输入账号123456789")

# 4. 输入密码
password_field = driver.find_element(By.ID, "J-password")
password_field.send_keys("输入密码*********")

driver.find_element(By.LINK_TEXT, "立即登录").click()

# 5. 输入验证码（12306使用短信验证码，因此无法自动填写，需手动完成）
# 输入身份证后四位
id_card_field = driver.find_element(By.ID, "id_card")
id_card_field.send_keys("6238")

# 点击获取手机短信验证码
driver.find_element(By.LINK_TEXT, "获取验证码").click()

# 在此处等待用户手动输入验证码并提交
time.sleep(15)

# 6. 提交登录表单
driver.find_element(By.LINK_TEXT, "确定").click()

# 7. 验证是否成功登录
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "退出"))
    )
    print("测试成功：登录成功")
except:
    print("测试失败：登录失败")
    driver.quit()
    exit()

# driver.find_element(By.LINK_TEXT, "车票预定").click()

# 8. 输入出发地
from_station = driver.find_element(By.ID, "fromStationText")
from_station.click()
from_station.clear()
from_station.send_keys("南京\n")  # \n代表回车

# 9. 输入目的地
to_station = driver.find_element(By.ID, "toStationText")
to_station.click()
to_station.clear()
to_station.send_keys("上海\n")

# 10. 选择出发日期
train_date = driver.find_element(By.ID, "train_date")
train_date.clear()
train_date.send_keys("2024-08-15")  # 输入日期

# 11. 点击查询按钮
search_button = driver.find_element(By.ID, "search_one")
search_button.click()

# 12. 等待查询结果加载并选择一趟车次
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn72"))
    )
    print("测试成功：查询成功")
    # 选择第一趟有票的车次
    book_button = driver.find_element(By.CSS_SELECTOR, ".btn72")
    book_button.click()
except:
    print("测试失败：查询失败")
    driver.quit()
    exit()

# 13. 等待订票页面加载并选择座位类型
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "normalPassenger_0"))
    )
    print("测试成功：进入订票页面")

    # 选择座位类型（硬座、硬卧、软卧等）
    seat_type = driver.find_element(By.CSS_SELECTOR, "select#seatType_1")
    seat_type.click()

    # 选择乘客
    passenger_checkbox = driver.find_element(By.ID, "normalPassenger_0")
    passenger_checkbox.click()
except:
    print("测试失败：进入订票页面失败")

# 14. 由于实际订票涉及支付，这里不进行真正的提交操作，测试到此结束

# 关闭浏览器
driver.quit()

