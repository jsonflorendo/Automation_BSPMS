
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


try:
    modal_name =  driver.find_element(By.ID, " modal_name")
    if modal_name.text.strip() == "Area of Expertise":
        print(" Test Case 1 -  Passed")
    else:
        print(" Test Case 1-  Failed : Incorrect modal name, it should be 'Area of Expertise'")
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

try:
    save_button = driver.find_element(By.ID, "save_button")
    if save_button.text.strip() == "Save":
        print("Test Case 5 - Passed")
    else:
        print("Test Case 5 - Failed : Incorrect button name")
except NoSuchElementException:
    print("Test Case 5 -  Failed : Please display button name")

save_button = driver.find_element(By.ID, "save")
save_button.click()

# error message
try:
    description_error = driver.find_element(By.ID, "description-error")
    if description_error.text.strip() == "This field is required.":
        print("Test Case 6 -  Passed")
    else:
        print("Test case 6 - Failed : Incorrect error message")
except NoSuchElementException:
    print(" Test Case 6 - Failed : Please display the error message")

try:
    concernBSP_error = driver.find_element(By.ID, "concernBSP-error")
    if concernBSP_error.text.strip() == "This field is required.":
        print("Test Case 7 -  Passed")
    else:
        print("Test case 7 - Failed : Incorrect error message")
except NoSuchElementException:
    print(" Test Case 7 - Failed : Please display the error message")
    
