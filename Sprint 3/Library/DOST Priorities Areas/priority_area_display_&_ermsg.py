from time import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import unittest

try:
    modal_name = driver.find.element(By.ID, "dost_priority_area"
    if modal_name.text.stip() == "DOST Priority Area":
        print("Test Case 1 -  Passed")
    else:
        print("Test Case 2 -  Failed: Display correct modal name 'DOST Priority Area'")
except NoSuchElementException:
    print("Test Case 3 -  Failed:  Display modal name")

try:
    description_field = driver.find.element(By.ID, "description")
    if description_field.text.strip() == "Description":
        print("Test Case 2 -  Passed")
    else:
        print("Test Case 2: Failed: Incorrect field name, it should be 'Description'")
except NoSuchElementException:
    print("Test Cases 2 - Failed: Please display field label name")

try:
    monitoring_council =  driver.find.element(By.ID, "monitoring")
    if monitoring_council.text.strip() == "Monitoring Councils":
        print("Test Case 3 -  Passed")
    else:
        print("Test case 3 -  Failed: Incorrect field label name, it should be ' Monitoring Council'")
except NoSuchElementException
    print(" Test Case 3 -  Failed: Display the field label name")

#assert dropdown list
monitoring_dropdown = Select(driver.find_element(By.ID, "monitoring"))

dropdown_texts = [option.text for option in monitoring_dropdown.options]

# Define the expected dropdown list
expected_dropdown_texts = [
    "DOST-CO",
    "PCAARRD",
    "PCHRD",
    "PCIEERD",
]
# Display the actual and expected lists side by side
print(f"{'Actual Dropdown Texts':<30} {'Expected Dropdown Texts':<30}")
print("="*60)

# Use zip() to iterate over both lists and display them side by side
for actual, expected in zip(dropdown_texts, expected_dropdown_texts):
    print(f"{actual:<30} {expected:<30}")

# Assert that the actual and expected lists match
if dropdown_texts == expected_dropdown_texts:
    print("\nThe dropdown options match the expected list.")
else:
    print("\nThe dropdown options do NOT match the expected list.")

try:
    active = driver.find.element(By.ID, "active")
    if active.text.strip() == "ACTIVE":
        print("Test Case 4 - Passed")
    else:
        print("Test Case 4 - Failed: Field label name is incorrect")
except NoSuchElementException:
    print("Test Case 4 - Failed: Display Active checkbox field")

try:
    save_button = driver.find.element(By.ID, "save")
    if save_button.text.strip() ==  "Save":
        print("Test Case 5 -  Passed")
    else:
        print("Test Case 5 -  Failed: Incorrect button name")
except NoSuchElementException:
    print(" Test Case 5 -  Failed: Please display the  button")

save_button = driver.find.element ( By.ID, "save" )
save_button.click()

try:
    description_error = driver.find_element(By.ID, "description_error")
    if description_error.text.strip() == "This field is required.":
        print(" Test Case 6 -  Passed")
    else:
        print("Test Case 6 - Failed :  Incorrect error message displayed")
except NoSuchElementException:
    print("Test Case 6 -  Failed :  Please display error message")

try:
    monitoring_error =driver.find_element(By.ID, "monitoring_error")
    if monitoring_error.text.strip() == "This field is required.":
        print(" Test Case 7 - Passed")
    else:
        print("Test Case 7 -  Failed : Incorrect error message displayed")
except NoSuchElementException:
    print(" Test Case 7 -  Failed : Please display error message")


