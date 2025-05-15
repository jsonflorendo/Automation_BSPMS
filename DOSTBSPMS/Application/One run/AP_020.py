from selenium.webdriver.common.by import By
import time


def handle_form(driver):
    try:
        print("Starting AP-20 form processing...")

        # Wait for the page to load
        time.sleep(3)

        # Locate and interact with the 'temp_support_needed' text area
        support_needed = driver.find_element(By.XPATH, "//textarea[@name='temp_support_needed']")
        support_needed.send_keys("Sample support information")
        print("Filled 'Support Needed' section.")

        # Locate and interact with the 'temp_details' text area
        details = driver.find_element(By.XPATH, "//textarea[@name='temp_details']")
        details.send_keys("Additional details here")
        print("Filled 'Details' section.")

        # Locate and click the save button
        save_button = driver.find_element(By.XPATH, "//i[@class='save-icon tippy icon-[mdi--check-circle-outline] text-xl text-center text-green-500 cursor-pointer px-2']")
        save_button.click()
        print("Clicked 'Save' button.")
        time.sleep(2)

        # Locate and click the arrow-right button for navigation
        next_button = driver.find_element(By.XPATH, "//i[@class='icon-[mdi--arrow-right] w-5 h-5 ml-2']")
        next_button.click()
        print("Navigated to the next section.")
        time.sleep(3)

        # Helper function to check a checkbox if it is not already checked
        def check_checkbox(xpath):
            checkbox = driver.find_element(By.XPATH, xpath)
            is_checked = checkbox.is_selected()
            if not is_checked:
                driver.execute_script("arguments[0].click();", checkbox)

        # Check the required checkboxes
        check_checkbox("//input[@id='unfulfilled_service_obligation']")
        print("Checked 'Unfulfilled Service Obligation' checkbox.")

        check_checkbox("//input[@id='data_privacy_consent_1']")
        print("Checked 'Data Privacy Consent 1' checkbox.")

        check_checkbox("//input[@id='data_privacy_consent_2']")
        print("Checked 'Data Privacy Consent 2' checkbox.")

        check_checkbox("//input[@id='certification']")
        print("Checked 'Certification' checkbox.")
        time.sleep(2)

        # Locate and click the "next" button
        final_next_button = driver.find_element(By.XPATH, "//button[@id='next']")
        final_next_button.click()
        print("Clicked 'Next' button.")
        time.sleep(5)

        # Handle the modal and click the "OK" button
        try:
            ok_button = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
            ok_button.click()
            print("Modal handled and 'OK' button clicked.")
        except:
            print("No modal appeared or 'OK' button not found.")
        time.sleep(2)

        print("AP-20 form completed successfully.")

    except Exception as e:
        print(f"Error in AP-20 form: {e}")