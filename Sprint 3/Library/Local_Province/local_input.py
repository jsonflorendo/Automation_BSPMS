from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

region = "Region IV-A"
name_of_province = "Laguna"

name_of_province_field = driver.find_element(By.ID, "region")
name_of_province_field.send_keys(f"{name_of_province}")

region_dropdown= driver.find_element(By.ID, "region")
select = Select(region_dropdown)
select.select_by_visible_text(f'{region}')

active_checkbox =  driver.find_element(By.ID, "checkbox")
if not active_checkbox.is_selected():
    active_checkbox.click()
    print(" Checkbox is ticked")

save_button = driver.find_element(By.ID, "save")
save_button.click()

