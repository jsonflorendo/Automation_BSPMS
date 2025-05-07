from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

region = "Asia"
country = "Philippines"

region_dropdown = driver.find_element(By.ID, "region_dropdown")
region_select = Select(region_dropdown)
region_select.select_by_visible_text("f'{region}'")

name_country = driver.find_element(By.ID, "name_country")

active_checkbox = driver.find_element(By.ID, "checkbox")
if not active_checkbox.is_slected():
    active_checkbox.click()
    print("Active checkbox is selected")


