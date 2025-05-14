from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from AP_email import handle_email
from AP_000 import handle_ap_000_form
from AP_010 import handle_form as handle_ap_010_form
from AP_011 import handle_form as handle_ap_011_form
from AP_100 import handle_form as handle_ap_100_form
from AP_101 import handle_form as handle_ap_101_form
from AP_110 import handle_form as handle_ap_111_form
from AP_111 import handle_form as handle_ap_112_form
from AP_020 import handle_form as handle_ap_020_form
from AP_030 import handle_form as handle_ap_030_form

def main():
    driver = webdriver.Firefox()

    try:
        print("Starting email handling...")
        try:
            handle_email(driver)  # Clicks the email link and switches tab
            print("Email handling completed.")
        except Exception as e:
            print(f"Email handling failed: {e}")
            return

        # Confirm that AP-000 form is loaded
        print("Verifying AP-000 form is loaded...")
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "contact_number"))
        )
        print("AP-000 form loaded successfully.")

        print("Processing AP-000 form...")
        try:
            handle_ap_000_form(driver)
            print("AP-000 form completed.")
        except Exception as e:
            print(f"Error while processing AP-000 form: {e}")
            return

        time.sleep(3)
        print("Processing AP-010 form...")
        handle_ap_010_form(driver)

        print("Processing AP-011 form...")
        handle_ap_011_form(driver)

        print("Processing AP-100 form...")
        handle_ap_100_form(driver)

        print("Processing AP-101 form...")
        handle_ap_101_form(driver)

        print("Processing AP-111 form...")
        handle_ap_111_form(driver)

        print("Processing AP-112 form...")
        handle_ap_112_form(driver)

        print("Processing AP-020 form...")
        handle_ap_020_form(driver)

        print("Processing AP-030 form...")
        handle_ap_030_form(driver)

    finally:
        driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    main()
