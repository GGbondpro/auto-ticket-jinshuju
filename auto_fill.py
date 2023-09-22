from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,200)
# 如果网址有变, 请自行修改
driver.get("https://jinshuju.net/f/GPDuXZ")
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
name.send_keys("王鑫培")
phone.send_keys("17841733149")
student_id.send_keys("3022244362")
id.send_keys("440983200310308018")
#一些按钮
campus.click()
button.click()
#等待提交成功
time.sleep(50)
print("successfully!")

driver.quit()


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