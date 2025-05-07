from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

try:
    modal_name = driver.find_element ( By.ID, "Local Province" )
    if modal_name.text.strip () == "Local Province":
        print ( "Test Cases 1 - Passed" )
    else:
        print ( "Test case 1 -  Failed: Incorrect Modal Name" )
except NoSuchElementException:
    print ( "Test Case 1 -  Failed: Please display modal name" )

try:
    region_field = driver.find_element ( By.ID, "region_field" )
    if region_field.text.strip () == "Region":
        print ( "Test Case 2 - Passed" )
    else:
        print ( " Test Case 2 -  Failed : Incorrect name field" )
except NoSuchElementException:
    print ( "Test Case 2 -  Failed : Please display name field" )

try:
    nameprovince_field = driver.find_element ( By.ID, "nameprovince field" )
    if nameprovince_field.text.strip () == "Name of Province":
        print ( "Test Case 3 -  Passed" )
    else:
        print ( "Test Case 3 -Failed : Incorrect field name" )
except NoSuchElementException:
    print ( " Test Case 3 - Failed : Please display field name" )
# assert dropdown list
region_dropdown = Select ( driver.find_element ( By.ID, "region" ) )
dropdown_texts = [option.text for option in region_dropdown.options]

# Define the expected dropdown list as Joven
expected_dropdown_texts = [
    "DOST-CO",
    "PCAARRD",
    "PCHRD",
    "PCIEERD",
]

# Use zip() to iterate over both lists and display them side by side
for actual, expected in zip ( dropdown_texts, expected_dropdown_texts ):


# Assert that the actual and expected lists match
if dropdown_texts == expected_dropdown_texts:
    print ( "\nTest Case 4 -  Passed: The dropdown options match the expected list." )
else:
    print ( "\n Test Case 4 -  Failed : The dropdown options do NOT match the expected list." )

try:
    level_field = driver.find_element ( By.ID, "level-field" )
    if level_field.text.strip () == "Level of Access":
        print ( " Test Case 5 - Passed " )
    else:
        print ( "Test Case 5 -  Failed: Incorrect field label name" )
except NoSuchElementException:
    print ( "Test Case 5 -Failed : Please display field label name" )

level_access = Select ( driver.find_element ( By.ID, "level_access" ) )
dropdown_access = [option.text for option in level_access.options]

expected_dropdown_texts = [
    " System Developer"
    " System Admin "
    " BSP Secretariat "
    " Council Secretariat"
]
print ( f"{'Actual Text':<30} {'Expected Text':<30}" )
print ( "=" * 60 )

for actual, expected in zip ( dropdown_access, expected_dropdown_texts ):
    if dropdown_access == expected_dropdown_texts:
        print ( "\nTest Case 6 -  Passed: The dropdown options match the expected list." )
    else:
        print ( "\nTest Case 6 - Failed: The dropdown options do NOT match the expected list." )

try:
    active = driver.find.element ( By.ID, "active" )
    if active.text.strip () == "ACTIVE":
        print ( "Test Case 7 - Passed" )
    else:
        print ( "Test Case 7 - Failed: Field label name is incorrect" )
except NoSuchElementException:
    print ( "Test Case 7 - Failed: Display Active checkbox field" )

try:
    save_button = driver.find.element ( By.ID, "save" )
    if save_button.text.strip () == "Save":
        print ( "Test Case 8 -  Passed" )
    else:
        print ( "Test Case 8 -  Failed: Incorrect button name" )
except NoSuchElementException:
    print ( " Test Case 8 -  Failed: Please display the  button" )

save_button = driver.find.element ( By.ID, "save" )
save_button.click ()

try:
    region_error = driver.find_element ( By.ID, "region-error" )
    if region_error.text.strip () == "This field is required."
        print ( "Test Case 9 - Passed" )
    else:
        print ( "Test Case 9 -  Failed : Incorrect error message" )
except NoSuchElementException:
    print ( " Test Case 9 - Failed : Please display error message" )

try:
    nameofprovince_error = driver.find_element ( By.ID, "nameofprovince-error" )
    if nameofprovince_error.text.strip () == "This field is required."
        print ( "Test Case 10 - Passed" )
    else:
        print ( "Test Case 10 -  Failed : Incorrect error message" )
except NoSuchElementException:
    print ( " Test Case 10 - Failed : Please display error message" )





