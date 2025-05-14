from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def fill_if_empty(element, value):
    """Check if the input element is empty, and if so, fill it with the specified value."""
    existing_value = element.get_attribute("value")
    if not existing_value.strip():  # Fill only if empty
        element.send_keys(value)
        print(f"Filled with: {value}")
    else:
        print(f"Skipped (already filled with): {existing_value}")


def handle_ap_000_form(driver):
    """Process and fill out the AP-000 form."""
    print("Processing AP-000 form...")

    # Locate the file input element for image upload
    file_input = driver.find_element(By.XPATH, "//input[@id='photo']")
    file_path = r"C:\Users\Wendell\PycharmProjects\DOSTBPMS\Application\Files\male.png"
    if not file_input.get_attribute("value").strip():  # Only upload if empty
        file_input.send_keys(file_path)
        print(f"Image successfully uploaded from: {file_path}")
    else:
        print("Image upload skipped (already uploaded).")

    # Assert that the image was uploaded (check if a value exists in the input)
    assert file_input.get_attribute("value").strip(), "Image upload failed."

    # Locate and enter the contact number
    contact_number_input = driver.find_element(By.XPATH, "//input[@id='contact_number']")
    fill_if_empty(contact_number_input, "9876543210")
    assert contact_number_input.get_attribute("value").strip() == "9876543210", "Contact number not filled correctly."

    # Locate and enter the postal address
    postal_address_input = driver.find_element(By.XPATH, "//input[@id='postal_address']")
    fill_if_empty(postal_address_input, "799 Main Street, Anothertown, USA")
    assert postal_address_input.get_attribute("value").strip() == "799 Main Street, Anothertown, USA", "Postal address not filled correctly."

    # Interact with the dropdown and wait for it to load
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
    print("Selected 'Philippines' from the dropdown.")

    # Assert that the dropdown selection is correct
    assert "Philippines" in dropdown.text, "Dropdown selection failed."

    # Locate and enter the state/city
    state_city_input = driver.find_element(By.XPATH, "//input[@id='state_city']")
    fill_if_empty(state_city_input, "Manila")
    assert state_city_input.get_attribute("value").strip() == "Manila", "State/City not filled correctly."

    # Fill out additional input fields with checks
    visa_validity_input = driver.find_element(By.XPATH, "//input[@id='ph_visa_validity']")
    fill_if_empty(visa_validity_input, "12/31/2025")
    assert visa_validity_input.get_attribute("value").strip() == "12/31/2025", "Visa validity not filled correctly."

    dob_input = driver.find_element(By.XPATH, "//input[@id='date_of_birth']")
    fill_if_empty(dob_input, "01/02/1995")
    assert dob_input.get_attribute("value").strip() == "01/02/1995", "Date of birth not filled correctly."

    contact_person_name_input = driver.find_element(By.XPATH, "//input[@id='contact_person_name']")
    fill_if_empty(contact_person_name_input, "Lin Doe")
    assert contact_person_name_input.get_attribute("value").strip() == "Lin Doe", "Contact person name not filled correctly."

    contact_person_address_input = driver.find_element(By.XPATH, "//input[@id='contact_person_address']")
    fill_if_empty(contact_person_address_input, "789 Some Street, Othercity, USA")
    assert contact_person_address_input.get_attribute("value").strip() == "789 Some Street, Othercity, USA", "Contact person address not filled correctly."

    contact_person_email_input = driver.find_element(By.XPATH, "//input[@id='contact_person_email_address']")
    fill_if_empty(contact_person_email_input, "janedoe@example.com")
    assert contact_person_email_input.get_attribute("value").strip() == "janedoe@example.com", "Contact person email address not filled correctly."

    contact_person_contact_no_input = driver.find_element(By.XPATH, "//input[@id='contact_person_contact_no']")
    fill_if_empty(contact_person_contact_no_input, "8765432109")
    assert contact_person_contact_no_input.get_attribute("value").strip() == "8765432109", "Contact person contact number not filled correctly."

    # Click the "Next" button
    next_button = driver.find_element(By.XPATH, "//button[@id='next']")
    next_button.click()
    print("Next button clicked successfully.")

    # Assert that the form navigates to the next page
    time.sleep(5)  # Wait for navigation
    assert "form001p2" in driver.current_url, "Failed to navigate to the next page."


def main():
    driver = webdriver.Firefox()
    try:
        # Navigate to AP-000 form
        driver.get(
            'http://10.10.99.18:8005/application/6UqqLRyj6Q4reyNxQRINmr3tHNll0521gqAVez6mCqBvFgVLlXEEbPXsYIPo/form001p1.1')

        # Handle AP-000 form
        handle_ap_000_form(driver)
    finally:
        # Ensure the browser closes even if there's an error
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    main()