from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,2000)
# 如果网址有变, 请自行修改
driver.get("https://jinshuju.net/f/LgvX7x")


# 定义目标时间
target_datetime = datetime(2023, 9, 22, 20, 29, 00)

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
student_id=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[6]/div/div/div[2]/div[1]/div/div/div/span/input')))
id=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[8]/div/div/div[2]/div[1]/div/div[2]/div/span/input')))
campus=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[10]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/label')))
button=wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[5]/div/button')))

#清空文本框
name.clear()
phone.clear()
student_id.clear()
id.clear()
#填写文本框
name.send_keys("哇哦")
phone.send_keys("18889292938")
student_id.send_keys("3243323422")
id.send_keys("39208445")
#一些按钮
campus.click()
button.click()
#等待提交成功
time.sleep(5)
print("successfully!")

driver.quit()




# 以下位临时记录，不用管
"""
/html/body/div[1]/div/div/form/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span/input
/html/body/div[1]/div/div/form/div[3]/div/div[4]/div/div/div[2]/div[1]/div/div/div/div/span/input
/html/body/div[1]/div/div/form/div[3]/div/div[6]/div/div/div[2]/div[1]/div/div/div/span/input
/html/body/div[1]/div/div/form/div[3]/div/div[8]/div/div/div[2]/div[1]/div/div[2]/div/span/input
/html/body/div[1]/div/div/form/div[3]/div/div[10]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/label
/html/body/div[1]/div/div/form/div[5]/div/button
"""
"""
/html/body/div[1]/div/div/form/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span/input
/html/body/div[1]/div/div/form/div[3]/div/div[4]/div/div/div[2]/div[1]/div/div/div/div/span/input
/html/body/div[1]/div/div/form/div[3]/div/div[6]/div/div/div[2]/div[1]/div/div/div/span/input
/html/body/div[1]/div/div/form/div[3]/div/div[8]/div/div/div[2]/div[1]/div/div[2]/div/span/input
/html/body/div[1]/div/div/form/div[3]/div/div[10]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/label
/html/body/div[1]/div/div/form/div[5]/div/button
"""