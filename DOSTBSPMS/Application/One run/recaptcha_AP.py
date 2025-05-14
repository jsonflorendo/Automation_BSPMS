from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (e.g., for Firefox)
driver = webdriver.Firefox()

try:
    # Navigate to the target URL
    driver.get('http://10.10.99.18:8005/application/')  # Replace with the actual URL

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Fill out the "Last Name" field
    last_name = driver.find_element(By.XPATH, "//input[@id='last_name']")
    last_name.send_keys("Ward")

    # Fill out the "First Name" field
    first_name = driver.find_element(By.XPATH, "//input[@id='first_name']")
    first_name.send_keys("Blue Loyld")

    # Fill out the "Extension" field
    extension = driver.find_element(By.XPATH, "//input[@id='name_extension']")
    extension.send_keys("Jr.")

    # Fill out the "Middle Name" field
    middle_name = driver.find_element(By.XPATH, "//input[@id='middle_name']")
    middle_name.send_keys("N.A.")

    # Fill out the "Maiden Name" field with "N.A." since it is for married women only
    maiden_name = driver.find_element(By.XPATH, "//input[@id='maiden_name']")
    maiden_name.send_keys("N.A.")

    # Select the "Male" checkbox by clicking its parent element
    male_checkbox = driver.find_element(By.XPATH, "//div[@class='flex pe-12']//i[@class='icon-[mdi--check-bold] text-gray-200 text-xs']/..")
    male_checkbox.click()

    # Click the "Other" checkbox
    other_checkbox = driver.find_element(By.XPATH, "//div[@class='flex items-center gap-2']//i[@class='icon-[mdi--check-bold] text-gray-200 text-xs']/..")
    other_checkbox.click()

    # Wait for 1 second to allow the "Other" textbox to appear
    time.sleep(1)

    # Locate the "Other" textbox and type a custom civil status
    other_textbox = driver.find_element(By.XPATH, "//input[@id='civil_status_other']")
    other_textbox.send_keys("Widowed")

    # Fill out the "Email Address" field
    email_address = driver.find_element(By.XPATH, "//input[@id='email_address']")
    email_address.send_keys("automate61@gmail.com")

    # Wait for 15 seconds for the user to manually solve the reCAPTCHA
    print("You have 15 seconds to solve the reCAPTCHA and click Submit manually...")
    time.sleep(15)

    # Optional: Wait to observe the result
    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the browser closes even if there's an error
    driver.quit()
