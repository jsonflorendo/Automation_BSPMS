import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://10.10.99.18:8005/application")
driver.maximize_window()
wait = WebDriverWait(driver, 15)

wait.until(EC.element_to_be_clickable((By.ID, "Medium-term_section"))).click()

repatriate_option = wait.until(EC.presence_of_element_located((By.ID, "repatriate_1")))
driver.execute_script("arguments[0].click();", repatriate_option)

wait.until(EC.presence_of_element_located((By.NAME, "last_name"))).send_keys("test, test ,tes")
driver.find_element(By.NAME, "first_name").send_keys("test")
driver.find_element(By.NAME, "name_extension").send_keys("Jr.")
driver.find_element(By.NAME, "middle_name").send_keys("test")
driver.find_element(By.NAME, "maiden_name").send_keys("N/A")

male_option = wait.until(EC.presence_of_element_located((By.ID, "sex_M")))
driver.execute_script("arguments[0].click();", male_option)

civil_status_option = wait.until(EC.presence_of_element_located((By.ID, "civil_status_S")))
driver.execute_script("arguments[0].click();", civil_status_option)

driver.find_element(By.NAME, "email_address").send_keys("d8a6qv3nsk@tidissajiiu.com")


old_url = driver.current_url
new_url = old_url

max_wait_time = 120 # seconds
start_time = time.time()

while time.time() - start_time < max_wait_time:
    current_url = driver.current_url
    if current_url != old_url:
        new_url = current_url
        break
    time.sleep(1)
else:
    driver.quit()
    exit()

