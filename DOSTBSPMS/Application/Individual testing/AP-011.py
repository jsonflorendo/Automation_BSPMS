from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize WebDriver
driver = webdriver.Firefox()

# Navigate to the target URL
driver.get("http://10.10.99.18:8005/application/6UqqLRyj6Q4reyNxQRINmr3tHNll0521gqAVez6mCqBvFgVLlXEEbPXsYIPo/form001p2")

# Wait for the page to load
time.sleep(5)

# Click the "Add" button to open the modal
add_host_button = driver.find_element(By.XPATH, "//button[@id='add_host_institution']")
add_host_button.click()

# Wait for the modal to appear
time.sleep(2)

# Helper function to check if a field is pre-filled
def fill_if_empty(field, value):
    if field.get_attribute("value") == "":
        field.send_keys(value)

# Fill in the "Full Name of Institution" field if empty
full_name_field = driver.find_element(By.XPATH, "//input[@id='full_name_of_institution']")
fill_if_empty(full_name_field, "Example Institution Name")

# Fill in the "Acronym" field if empty
acronym_field = driver.find_element(By.XPATH, "//input[@id='acronym']")
fill_if_empty(acronym_field, "EIN")
time.sleep(3)
# Select "Industry/NGO" or "Academe" from the Institution Type dropdown if not already selected
institution_type_dropdown = Select(driver.find_element(By.ID, "type_of_institution"))

# Check if no valid option is selected
if institution_type_dropdown.first_selected_option.get_attribute("value") == "":
    # Select the desired option by its visible text
    institution_type_dropdown.select_by_visible_text("Industry/NGO")  # Change to "Academe" if nneeded

# Fill in the "Postal Address" field if empty
postal_address_field = driver.find_element(By.XPATH, "//input[@id='postal_address']")
fill_if_empty(postal_address_field, "123 Example Street, Example City")

# Select "NCR" from the region dropdown if not already selected
region_dropdown = Select(driver.find_element(By.ID, "region"))
if region_dropdown.first_selected_option.text.strip() == "Region":
    region_dropdown.select_by_visible_text("NCR")

# Wait for the province dropdown to load
time.sleep(3)

# Select "Quezon City" from the province dropdown if not already selected
province_dropdown = Select(driver.find_element(By.ID, "province"))
if province_dropdown.first_selected_option.text.strip() == "Province/City":
    province_dropdown.select_by_visible_text("Quezon City")

# Fill in the "Contact Numbers" field if empty
contact_numbers_field = driver.find_element(By.XPATH, "//input[@id='contact_numbers']")
fill_if_empty(contact_numbers_field, "123-456-7890")

# Fill in the "Email Addresses" field if empty
email_addresses_field = driver.find_element(By.XPATH, "//input[@id='email_addresses']")
fill_if_empty(email_addresses_field, "example@example.com")

# Fill in the "Contact Person Name" field if empty
contact_person_name_field = driver.find_element(By.XPATH, "//input[@id='contact_person_name']")
fill_if_empty(contact_person_name_field, "John Doe")

# Fill in the "Designation" field if empty
designation_field = driver.find_element(By.XPATH, "//input[@id='designation']")
fill_if_empty(designation_field, "Director")

# Fill in the "Website" field if empty
website_field = driver.find_element(By.XPATH, "//input[@id='website']")
fill_if_empty(website_field, "https://www.example.com")

# Click the "Save" button
save_button = driver.find_element(By.XPATH, "//button[@id='save']")
save_button.click()

# Wait for the modal popup to appear
time.sleep(2)

# Click the "OK" button on the popup modal
ok_button = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
ok_button.click()

# Wait to observe the actions (optional)
time.sleep(5)

# Close the WebDriver
driver.quit()