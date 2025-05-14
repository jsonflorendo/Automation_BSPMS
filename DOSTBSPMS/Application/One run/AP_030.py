from selenium.webdriver.common.by import By
import time


def handle_form(driver):
    try:
        print("Starting AP-030 form processing...")

        # Wait for the page to load
        time.sleep(3)

        # Upload BSP Application Form
        bsp_form_input = driver.find_element(By.XPATH, "//input[@id='bsp_forms']")
        bsp_form_input.send_keys(r"C:\Users\Wendell\PycharmProjects\DOSTBPMS\Application\Files\BSP Application Form.pdf")
        print("Uploaded BSP Application Form.")
        time.sleep(2)  # Delay after upload

        # Upload Endorsement Letter
        endorsement_letter_input = driver.find_element(By.XPATH, "//input[@id='endorsement_letter']")
        endorsement_letter_input.send_keys(r"C:\Users\Wendell\PycharmProjects\DOSTBPMS\Application\Files\Eq1.pdf")
        print("Uploaded Endorsement Letter.")
        time.sleep(2)  # Delay after upload

        # Upload Medical Certificate
        medical_certificate_input = driver.find_element(By.XPATH, "//input[@id='medical_certificate']")
        medical_certificate_input.send_keys(r"C:\Users\Wendell\PycharmProjects\DOSTBPMS\Application\Files\sam1.pdf")
        print("Uploaded Medical Certificate.")
        time.sleep(2)  # Delay after upload

        # Upload Passport
        passport_input = driver.find_element(By.XPATH, "//input[@id='passport']")
        passport_input.send_keys(r"C:\Users\Wendell\PycharmProjects\DOSTBPMS\Application\Files\sam2.pdf")
        print("Uploaded Passport.")
        time.sleep(2)  # Delay after upload

        # Upload Diploma
        diploma_input = driver.find_element(By.XPATH, "//input[@id='diploma']")
        diploma_input.send_keys(r"C:\Users\Wendell\PycharmProjects\DOSTBPMS\Application\Files\sam12.pdf")
        print("Uploaded Diploma.")
        time.sleep(2)  # Delay after upload

        # Upload Curriculum Vitae
        curriculum_vitae_input = driver.find_element(By.XPATH, "//input[@id='curriculum_vitae']")
        curriculum_vitae_input.send_keys(r"C:\Users\Wendell\PycharmProjects\DOSTBPMS\Application\Files\sample.pdf")
        print("Uploaded Curriculum Vitae.")
        time.sleep(2)  # Delay after upload

        # Wait for all uploads to complete
        time.sleep(4)

        # Locate and click the final "next" button
        next_button = driver.find_element(By.XPATH, "//button[@id='next']")
        next_button.click()
        print("Clicked 'Next' button.")
        time.sleep(10)

        print("AP-030 form completed successfully.")

    except Exception as e:
        print(f"Error in AP-030 form: {e}")