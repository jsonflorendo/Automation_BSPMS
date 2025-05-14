from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver for Firefox
driver = webdriver.Firefox()

try:
    # Open the target URL
    url = "http://10.10.99.18:8005/application/6UqqLRyj6Q4reyNxQRINmr3tHNll0521gqAVez6mCqBvFgVLlXEEbPXsYIPo/form001p3"
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Locate and interact with the 'temp_support_needed' text area
    support_needed = driver.find_element(By.XPATH, "//textarea[@name='temp_support_needed']")
    support_needed.send_keys("Sample support information")

    # Locate and interact with the 'temp_details' text area
    details = driver.find_element(By.XPATH, "//textarea[@name='temp_details']")
    details.send_keys("Additional details here")

    # Locate and click the save button
    save_button = driver.find_element(By.XPATH, "//i[@class='save-icon tippy icon-[mdi--check-circle-outline] text-xl text-center text-green-500 cursor-pointer px-2']")
    save_button.click()

    # Wait for save action to complete
    time.sleep(2)

    # Locate and click the arrow-right button for navigation
    next_button = driver.find_element(By.XPATH, "//i[@class='icon-[mdi--arrow-right] w-5 h-5 ml-2']")
    next_button.click()

    # Wait for the navigation action to complete
    time.sleep(3)

    # Helper function to check a checkbox if it is not already checked
    def check_checkbox(xpath):
        checkbox = driver.find_element(By.XPATH, xpath)
        is_checked = checkbox.is_selected()
        if not is_checked:
            driver.execute_script("arguments[0].click();", checkbox)

    # Check 'unfulfilled_service_obligation' checkbox (renamed as checkbox1)
    check_checkbox("//input[@id='unfulfilled_service_obligation']")

    # Check 'data_privacy_consent_1' checkbox (renamed as checkbox2)
    check_checkbox("//input[@id='data_privacy_consent_1']")

    # Check 'data_privacy_consent_2' checkbox (renamed as checkbox3)
    check_checkbox("//input[@id='data_privacy_consent_2']")

    # Check 'certification' checkbox
    check_checkbox("//input[@id='certification']")

    # Wait for the checkbox interactions to complete
    time.sleep(2)

    # Locate and click the "next" button
    final_next_button = driver.find_element(By.XPATH, "//button[@id='next']")
    final_next_button.click()

    # Wait for the next action to complete
    time.sleep(5)

    # Handle the modal and click the "OK" button
    try:
        ok_button = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
        ok_button.click()
        print("Modal handled and 'OK' button clicked.")
    except:
        print("No modal appeared or 'OK' button not found.")

    # Wait for the modal action to complete
    time.sleep(2)

finally:
    # Close the browser
    driver.quit()