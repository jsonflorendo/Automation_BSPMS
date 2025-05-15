from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver for Firefox
driver = webdriver.Firefox()
try:
    # Open the target URL (replace with your actual application URL)
    url = "http://10.10.99.18:8005/application/udzmANHVDrqGAPlNCaK9Up5OlptFjGyN4WiLSMi0v0PJ3h0keaAJtkSFt8od/docs"
    driver.get(url)

    # Wait for the page to load
    time.sleep(3)

    # Upload BSP Application Form
    bsp_form_input = driver.find_element(By.XPATH, "//input[@id='bsp_forms']")
    bsp_form_input.send_keys(r"C:\xampp\htdocs\BSPMS\DOSTBSPMS\Application\Files\BSP Application Form.pdf")
    time.sleep(3)  # Delay after upload

    # Upload Endorsement Letter
    endorsement_letter_input = driver.find_element(By.XPATH, "//input[@id='endorsement_letter']")
    endorsement_letter_input.send_keys(r"C:\xampp\htdocs\BSPMS\DOSTBSPMS\Application\Files\Eq1.pdf")
    time.sleep(3)  # Delay after upload

    # Upload Medical Certificate
    medical_certificate_input = driver.find_element(By.XPATH, "//input[@id='medical_certificate']")
    medical_certificate_input.send_keys(r"C:\xampp\htdocs\BSPMS\DOSTBSPMS\Application\Files\sam1.pdf")
    time.sleep(3)  # Delay after upload

    # Upload Passport
    passport_input = driver.find_element(By.XPATH, "//input[@id='passport']")
    passport_input.send_keys(r"C:\xampp\htdocs\BSPMS\DOSTBSPMS\Application\Files\sam2.pdf")
    time.sleep(3)  # Delay after upload

    # Upload Diploma
    diploma_input = driver.find_element(By.XPATH, "//input[@id='diploma']")
    diploma_input.send_keys(r"C:\xampp\htdocs\BSPMS\DOSTBSPMS\Application\Files\sam12.pdf")
    time.sleep(3)  # Delay after upload

    # Upload Curriculum Vitae
    curriculum_vitae_input = driver.find_element(By.XPATH, "//input[@id='curriculum_vitae']")
    curriculum_vitae_input.send_keys(r"C:\xampp\htdocs\BSPMS\DOSTBSPMS\Application\Files\sample.pdf")
    time.sleep(3)  # Delay after upload

    # Wait for all uploads to complete
    time.sleep(3)

    # Locate and click the final "next" button
    next_button = driver.find_element(By.XPATH, "//button[@id='next']")
    next_button.click()

    # Wait after clicking the "next" button
    time.sleep(2)

finally:

    # Close the browser
    driver.quit()