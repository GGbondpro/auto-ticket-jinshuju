from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

#修改以下
link = "https://jsj.top/f/IxLjU0"
your_name = "姓名"
your_phone = "18889"
your_card_id = "32433234220000000"
your_student_id = "3920844533"
# 定义目标时间
target_datetime = datetime(2024, 11, 27, 18, 00, 00)



driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,2000)

driver.get(link)


# 获取当前时间
current_datetime = datetime.now()

# 计算时间差
time_difference = target_datetime - current_datetime

# 将时间差转换为秒
target_time = time.time() + time_difference.total_seconds()

# 循环等待，直到目标时间到达
while time.time() < target_time:
    continue

driver.refresh()

# 定位元素
name = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span/input')))
phone=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[4]/div/div/div[2]/div[1]/div/div/div/div/span/input')))
card_id=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[6]/div/div/div[2]/div[1]/div/div/div/span/input')))
student_id=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span/input')))
campus=wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/form/div[3]/div/div[10]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/label')))
button=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[5]/div/button')))

#清空文本框
name.clear()
phone.clear()
card_id.clear()
student_id.clear()
#填写文本框
name.send_keys(your_name)
phone.send_keys(your_phone)
card_id.send_keys(your_card_id)
student_id.send_keys(your_student_id)
#一些按钮
campus.click()
button.click()
#等待提交成功
time.sleep(5)
print("successfully!")

driver.quit()
