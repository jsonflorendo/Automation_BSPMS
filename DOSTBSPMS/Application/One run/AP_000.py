from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fill_if_empty(element, value):
    existing_value = element.get_attribute("value")
    if not existing_value.strip():
        element.send_keys(value)
        print(f"Filled with: {value}")
    else:
        print(f"Skipped (already filled with): {existing_value}")

def handle_ap_000_form(driver):
    print("Processing AP-000 form...")
    try:
        # ✅ 1. Upload image
        try:
            file_input = driver.find_element(By.XPATH, "//input[@id='photo']")
            file_path = r"C:\Users\Wendell\PycharmProjects\DOSTBPMS\Application\Files\male.png"
            if not file_input.get_attribute("value").strip():
                file_input.send_keys(file_path)
                print(f"Image uploaded from: {file_path}")
            else:
                print("Image already uploaded. Skipping.")
        except Exception as e:
            print(f"Failed to upload image: {e}")

        # ✅ 2. Enter contact number
        try:
            contact_number_input = driver.find_element(By.ID, "contact_number")
            fill_if_empty(contact_number_input, "9876543210")
        except Exception as e:
            print(f"Failed to enter contact number: {e}")

        # ✅ 3. Postal address
        try:
            postal_address_input = driver.find_element(By.ID, "postal_address")
            fill_if_empty(postal_address_input, "799 Main Street, Anothertown, USA")
        except Exception as e:
            print(f"Failed to enter postal address: {e}")

        # ✅ 4. Dropdown (Country)
        try:
            dropdown = driver.find_element(By.XPATH, "//div[@class='ss-main slimSelect']")
            dropdown.click()
            print("Dropdown opened.")

            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='ss-search']//input[@placeholder=' ']"))
            )
            search_input.send_keys("Phil")
            time.sleep(1)
            search_input.send_keys(Keys.ARROW_DOWN)
            search_input.send_keys(Keys.ENTER)

            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, "//div[@class='ss-main slimSelect']"), "Philippines")
            )
            print("Selected 'Philippines'.")
        except Exception as e:
            print(f"Dropdown interaction failed: {e}")

        # ✅ 5. State/City
        try:
            state_city_input = driver.find_element(By.ID, "state_city")
            fill_if_empty(state_city_input, "Manila")
        except Exception as e:
            print(f"Failed to enter state/city: {e}")

        # ✅ 6. Other fields
        try:
            fill_if_empty(driver.find_element(By.ID, "ph_visa_validity"), "12/31/2025")
            fill_if_empty(driver.find_element(By.ID, "date_of_birth"), "01/02/1995")
            fill_if_empty(driver.find_element(By.ID, "contact_person_name"), "Lin Doe")
            fill_if_empty(driver.find_element(By.ID, "contact_person_address"), "789 Some Street, Othercity, USA")
            fill_if_empty(driver.find_element(By.ID, "contact_person_email_address"), "janedoe@example.com")
            fill_if_empty(driver.find_element(By.ID, "contact_person_contact_no"), "8765432109")
        except Exception as e:
            print(f"Failed to fill one or more additional fields: {e}")

        # ✅ 7. Click Next
        try:
            next_button = driver.find_element(By.ID, "next")
            next_button.click()
            print("Clicked Next.")
        except Exception as e:
            print(f"Failed to click Next: {e}")

        time.sleep(5)
    except Exception as e:
        print(f"An error occurred while handling AP-000: {e}")
