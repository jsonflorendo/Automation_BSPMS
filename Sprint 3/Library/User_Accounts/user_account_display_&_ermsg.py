from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

try:
    modal_name = driver.find_element(By.ID, "accounts")
    if modal_name.text.strip() == "Account Details":
        print("Test Cases 1 - Passed")
    else:
        print("test case 1 -  Failed: Incorrect Modal Name")
except NoSuchElementException:
    print("Test Case 1 -  Failed: Please display modal name")

try:
    name_field = driver.find_element(By.ID,  "name_field")
    if name_field.text.strip() == "Name":
        print("Test Case 2 - Passed")
    else:
        print(" Test Case 2 -  Failed : Incorrect name field")
except NoSuchElementException:
    print("Test Case 2 -  Failed : Please display name field")

try:
    monitoring_field = driver.find_element ( By.ID, "monitoring field" )
    if monitoring_field.text.strip () == "Monitoring Council":
        print ( "Test Case 3 -  Passed" )
    else:
        print ( "Test Case 3 -Failed : Incorrect field name" )
except NoSuchElementException:
    print ( " Test Case 3 - Failed : Please display field name" )
# assert dropdown list
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
    print("\nTest Case 4 -  Passed: The dropdown options match the expected list.")
else:
    print("\n Test Case 4 -  Failed : The dropdown options do NOT match the expected list.")

try: 
    level_field = driver.find_element(By.ID, "level-field")
    if level_field.text.strip() == "Level of Access":
        print(" Test Case 5 - Passed ")
    else:
        print("Test Case 5 -  Failed: Incorrect field label name")
except NoSuchElementException:
    print("Test Case 5 -Failed : Please display field label name")
        
level_access = Select(driver.find_element(By.ID, "level_access"))
dropdown_access = [option.text for option in level_access.options]

expected_dropdown_texts = [
    " System Developer"
    " System Admin "
    " BSP Secretariat "
    " Council Secretariat"
]
print(f"{'Actual Text':<30} {'Expected Text':<30}")
print("="*60)

for actual, expected in zip(dropdown_access, expected_dropdown_texts):
    if dropdown_access == expected_dropdown_texts:
        print ( "\nTest Case 6 -  Passed: The dropdown options match the expected list." )
    else:
        print ( "\nTest Case 6 - Failed: The dropdown options do NOT match the expected list." )
try:
    email_field = driver.find_element(By.ID, "email_field")
    if email_field.text.strip() == "Email Address":
        print("Test Case 5 - Passed")
    else:
        print(" Test Case 5 - Failed : Incorrect field label name")
except NoSuchElementException:
    print("Test Case 5 -  Failed : Please display field label name")

try:
    reset_field = driver.find_element(By.ID, "reset_field")
    if reset_field.text.strip() == "Reset Account"
        print(" Test Case 8 -  Passed")
    else:
        print("test Case 8 -  Failed :  Incorrect display of field label name")
except NoSuchElementException:
    print("Test Case 8 -  Failed : Please display the label name")
    
try:
    active = driver.find.element(By.ID, "active")
    if active.text.strip() == "ACTIVE":
        print("Test Case 9 - Passed")
    else:
        print("Test Case 9 - Failed: Field label name is incorrect")
except NoSuchElementException:
    print("Test Case 9 - Failed: Display Active checkbox field")

try:
    save_button = driver.find.element(By.ID, "save")
    if save_button.text.strip() == "Save":
        print("Test Case 10 -  Passed")
    else:
        print("Test Case 10 -  Failed: Incorrect button name")
except NoSuchElementException:
    print(" Test Case 10 -  Failed: Please display the  button")

save_button = driver.find.element(By.ID, "save")
save_button.click ()

try:
    name_error = driver.find_element(By.ID, "name-error")
    if name_error.text.strip() == "This field is required."
        print("Test Case 11 - Passed")
    else:
        print("Test Case 11 -  Failed : Incorrect error message")
except NoSuchElementException:
    print(" Test Case 11 - Failed : Please display error message")
    
    
try:
    monitoring_error = driver.find_element(By.ID, "monitoring-error")
    if monitoring_error.text.strip() == "This field is required."
        print("Test Case 12 - Passed")
    else:
        print("Test Case 12 -  Failed : Incorrect error message")
except NoSuchElementException:
    print(" Test Case 12 - Failed : Please display error message")

try:
    access_error = driver.find_element ( By.ID, "access-error" )
    if access_error.text.strip () == "This field is required."
        print ( "Test Case 13 - Passed" )
    else:
        print ( "Test Case 13 -  Failed : Incorrect error message" )
except NoSuchElementException:
    print ( " Test Case 13 - Failed : Please display error message" )

try:
    email_error = driver.find_element ( By.ID, "email-error" )
    if email_error.text.strip () == "This field is required."
        print ( "Test Case 11 - Passed" )
    else:
        print ( "Test Case 11 -  Failed : Incorrect error message" )
except NoSuchElementException:
    print ( " Test Case 11 - Failed : Please display error message" )


    
    