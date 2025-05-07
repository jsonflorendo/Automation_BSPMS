
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


try:
    modal_name =  driver.find_element(By.ID, " modal_name")
    if modal_name.text.strip() == "Specialization":
        print(" Test Case 1 -  Passed")
    else:
        print(" Test Case 1-  Failed : Incorrect modal name, it should be 'Specialization'")
except NoSuchElementException:
    print(" Test Case 1 - Failed : Please display modal name ")

try:
    description =  driver.find_element(By.ID, "description")
    if description.text.strip() == "Description":
        print(" Test Case 2 - Passed")
    else:
        print("Test Cases 2 - Failed :  Incorrect field label name")
except NoSuchElementException:
    print("Test Case 2 - Failed : Please display field label name")

try:
    concern_bsp = driver.find_element (By.ID, " concern")
    if concern_bsp.text.strip() == "Concerned BSP Secretariat":
        print(" test Case 3 - Passed")
    else:
        print("Test Case 3  - Failed : Incorrect field label name")
except NoSuchElementException
    print(" Test Case 33 -  Failed : Please display the field label name")

try:
    active = driver.find_element(By.ID, "active")
    if active.text.strip() == "ACTIVE":
        print("Test Case 4 - Passed")
    else:
        print("Test Case 4 - Failed : Incorrect checkbox name")
except NoSuchElementException:
    print("Test Case 4 -  Failed : Please display checkbox name")

# error message
