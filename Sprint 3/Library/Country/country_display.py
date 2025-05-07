import binascii

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

save_button =  driver.find_element(By.ID, "save")
save_button.click()

try:
    modal_name = driver.find_element(By.ID, " modal_name")
    if modal_name.text.strip( ) == "Country"
        print(" Test Case 1 -  Passed")
    else:
        print(" Test Case 1 - Failed : Incorrect modal name")
except NoSuchElementException:
    print("Test Case 1- Failed : Please display modal name")

try:
    region_field = driver.find_element(By.ID, "region")
    if region_field.text.strip() == "Region/Continent"
        print("Test Case 2 -  Passed")
    else:
        print("Test Case 2 - Failed : Incorrect field label name")
except NoSuchElementException:
    print(" Test case 2 -  Failed : Please display field label name")

region_dropdown =  driver.find_element(By.ID, "region")
region_list =[option.text for option in region_dropdown.options]

expected_list = ["a","b","c"]
print(f"{'Actual dropdown list:<40'} {'Expected dropdown list':<40}")
print("="*60)

for actual, expected in zip(region_list, expected_list)
    print(f"{'actual:<40'} {'expected:<40'}")
    if region_list == expected_list:
        print("Test Case 3 - Passed")
    else:
        print("Test Case 3 - Failed : dropdown list DO not match")

try:
    name_country_field = driver.find_element(By.ID, "name_country")
    if name_country_field.text.strip() == "Name of Country"
        print(" Test Case 4 - Passed")
    else:
        print(" Test Case 4 - Failed : Incorrect field label name")
except NoSuchElementException:
    print(" Test Case 4 - Failed : Please display field label name")

try:
    active = driver.find_element(By.ID, "active")
    if active.text.strip() == "ACTIVE":
        print(" Test Case 5 -  Passed")
    else:
        print(" Test Case 5 - Failed : Incorrect field label name")
except NoSuchElementException:
    print(" Test Case 5 - Failed :  Please display field label name")

try:
    save = driver.find_element(By.ID, " save")
    if save.text.strip() == "Save":
        print("Test Case 6 -  Passed")        
    else:
        print(" Test Case 6 - Failed : Incorrect button name")
except NoSuchElementException:
    print(" Test Case 6 - Failed : Please display button name")
    
# error message display
try:
    region_error = driver.find_element(By.I, "region_error")
    if region_error.text.stip() == "This field is required."
        print("Test Case 7 - Passed")
    else:
        print(" Test Case 7 -  Failed : Incorrect error message")
except NoSuchElementException:
    print("Test Case 7 - Failed : Please display error message")

try:
    country_error = driver.find_element(By.ID, "country_error")
    if country_error.text.strip() == " This field is required."
        print(" Test Case 8 -  Passed")
    else:
        print(" Test Case 8 -  Failed : Incorrect error message")
except NoSuchElementException:
    print(" Test Case 8 -  Failed : Please display error message")
