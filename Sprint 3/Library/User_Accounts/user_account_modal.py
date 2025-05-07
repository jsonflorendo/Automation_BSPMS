
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

Name = "Shiela Jeane J Caraan"
monitoring_council = "PCAARRD"
Level_of_Access = "System Admin"
Email_add= "sjjinahon@gmail.com"

name = driver.find_element(By.ID, "name")
name.send_keys(f"{Name}")

monitoring_dropdown= driver.find_element(By.ID, "monitoring_council")
select = Select(monitoring_dropdown)
select.select_by_visible_text(f'{monitoring_council}')

level_dropdown = driver.find_element(By, "access")
select = Select(level_dropdown)
select.select_by_visible_text(f'{Level_of_Access}')

email = driver.find_element(By.ID, "email")
email.send_keys(f'{Email_add}')

active_checkbox = driver.find_element(By.ID, "active")
if not active_checkbox.is_selected():
    active_checkbox.click()

save_button = driver.find_element(By.ID, "save")
save_button.click()





