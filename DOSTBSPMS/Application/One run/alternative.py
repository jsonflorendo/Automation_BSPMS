from selenium import webdriver
from AP_000 import handle_ap_000_form
from AP_010 import handle_form as handle_ap_010_form
from AP_011 import handle_form as handle_ap_011_form
from AP_100 import handle_form as handle_ap_100_form
from AP_101 import handle_form as handle_ap_101_form
from AP_110 import handle_form as handle_ap_111_form
from AP_111 import handle_form as handle_ap_112_form
from AP_020 import handle_form as handle_ap_20_form
from AP_030 import handle_form as handle_ap_030_form
import time


def main():
    # Initialize the Firefox WebDriver
    driver = webdriver.Firefox()

    try:
        
        # First form - AP-000 (Continnue with the URL of the first form)
        driver.get(
            'http://10.10.99.18:8005/application/wQ8wUD4Zs6k5mN0NcrprdyEwlLld2558jj3TyZKsU0LleKMLB1Uv7DT9dgae/form001p1.1')

        handle_ap_000_form(driver)
        time.sleep(3)  # 3 second delay after AP-000

        # Second form - AP-010 (automatically navigated from AP-000)
        handle_ap_010_form(driver)
        time.sleep(3)  # 3 second delay after AP-010

        # Third form - AP-011 (automatically navigated from AP-010)
        handle_ap_011_form(driver)
        time.sleep(3)  # 3 second delay after AP-011

        # Fourth form - AP-100 (automatically navigated from AP-011)
        handle_ap_100_form(driver)
        time.sleep(3)  # 3 second delay after AP-100

        # Fifth form - AP-101 (automatically navigated from AP-100)
        handle_ap_101_form(driver)
        time.sleep(3)  # 3 second delay after AP-101

        # Sixth form - AP-111 (automatically navigated from AP-101)
        handle_ap_111_form(driver)
        time.sleep(3)  # 3 second delay after AP-111

        # Seventh form - AP-112 (automatically navigated from AP-111)
        handle_ap_112_form(driver)
        time.sleep(3)  # 3 second delay after AP-112

        # Eighth form - AP-20 (automatically navigated from AP-112)
        handle_ap_20_form(driver)
        time.sleep(3)  # 3 second delay after AP-20

        # Ninth form - AP-030 (automatically navigated from AP-20)
        handle_ap_030_form(driver)
        time.sleep(3)  # 3 second delay after AP-030

    finally:
        # Close the browser
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    main()