from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

GMAIL_USER = "automate61@gmail.com"
GMAIL_PASS = "Automation1221"

def handle_email(driver):
    try:
        print("Opening Gmail...")
        driver.get("https://mail.google.com/")

        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        email_field.send_keys(GMAIL_USER)
        email_field.send_keys(Keys.RETURN)
        time.sleep(3)

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_field.send_keys(GMAIL_PASS)
        password_field.send_keys(Keys.RETURN)
        print("Logged into Gmail.")
        time.sleep(8)

        latest_email = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//tr[@role='row'])[1]//div[@role='link']"))
        )
        latest_email.click()
        time.sleep(3)
        print("Latest email opened.")

        email_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Continue with application']"))
        )
        print("Found application link:", email_link.get_attribute("href"))
        email_link.click()
        print("Clicked application link.")
        time.sleep(3)

        # 🔥 The missing critical step:
        driver.switch_to.window(driver.window_handles[-1])
        print("Switched to new tab.")
        print("Current URL:", driver.current_url)
        print("Page Title:", driver.title)

        # Wait for AP-000 form to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "contact_number"))
        )
        print("AP-000 form detected and ready.")

    except Exception as e:
        print(f"Error in handle_email: {e}")
        raise
