
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# 如果网址有变, 请自行修改
driver.get("https://jinshuju.net/f/lSIrOE")

# 定位元素
name = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span/input')))
name_x = name.location['x']
name_y = name.location['y']
# driver.execute_script(f"window.scrollBy(-200, -5000);")

phone = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[4]/div/div/div[2]/div[1]/div/div/div/div/span/input')))
student_id = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[6]/div/div/div[2]/div[1]/div/div/div/span/input')))
id = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[8]/div/div/div[2]/div[1]/div/div[2]/div/span/input')))
campus = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[10]/div/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/label/span[2]/span[1]')))
button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/form/div[5]/div/button')))

# 滚动到目标元素可见
#driver.execute_script("arguments[0].scrollIntoView();", name)

# 获取各个元素的坐标


phone_x = phone.location['x']
phone_y = phone.location['y']

student_id_x = student_id.location['x']
student_id_y = student_id.location['y']

id_x = id.location['x']
id_y = id.location['y']

campus_x = campus.location['x']
campus_y = campus.location['y']

button_x = button.location['x']
button_y = button.location['y']

print(phone_x,phone_y,student_id_x,student_id_y ,id_x,id_y)
time.sleep(3)

driver.get("https://jinshuju.net/f/WtF9IK")

time.sleep(3)


# 使用坐标定位点击输入框,使用键盘输入内容
name= ActionChains(driver)
name.move_by_offset(name_x, name_y).click().perform()# 点击
name_input = driver.switch_to.active_element  # 获取当前活跃的元素（通常是刚刚点击的输入框）
name_input.send_keys("欧克")#输入
driver.switch_to.default_content()
time.sleep(10)

# driver.execute_script(f"window.scrollBy(0, -100);")
print(phone_x,phone_y,student_id_x,student_id_y ,id_x,id_y)
phone= ActionChains(driver)
phone.move_by_offset(phone_x, phone_y).click().perform()
phone_input = driver.switch_to.active_element 
phone_input.send_keys("17809383728")
time.sleep(1)

student_id= ActionChains(driver)
student_id.move_by_offset(student_id_x, student_id_y).click().perform()
student_id_input = driver.switch_to.active_element 
student_id_input.send_keys("4039204920")

id= ActionChains(driver)
id.move_by_offset(id_x, id_y).click().perform()
id_input = driver.switch_to.active_element 
id_input.send_keys("anduiqh43389420")

"""
campus= ActionChains(driver)
campus.move_by_offset(button_x, button_y).click().perform()

button= ActionChains(driver)
button.move_by_offset(button_x, button_y).click().perform()

"""

#等待提交成功
time.sleep(100)
print("successfully!")

#driver.quit()
