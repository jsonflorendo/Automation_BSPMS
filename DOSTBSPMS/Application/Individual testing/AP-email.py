from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# === Setup ===
GMAIL_USER = os.getenv("GMAIL_USER", "automate61@gmail.com")  # Replace or set env var
GMAIL_PASS = os.getenv("GMAIL_PASS", "Automation1221")              # Replace or set env var

# === Initialize Firefox WebDriver ===
driver = webdriver.Firefox()

try:
    print("Opening Gmail...")
    driver.get("https://mail.google.com/")

    # === Step 1: Login with email ===
    email_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    email_field.send_keys(GMAIL_USER)
    email_field.send_keys(Keys.RETURN)
    time.sleep(2)

    # === Step 2: Enter password ===
    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.send_keys(GMAIL_PASS)
    password_field.send_keys(Keys.RETURN)
    print("Logged into Gmail.")
    time.sleep(5)

    # === Step 3: Wait for inbox and click latest email ===
    wait = WebDriverWait(driver, 30)
    try:
        latest_email = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//tr[@role='row'])[1]//div[@role='link']")
        ))
        latest_email.click()
        print("Latest email opened successfully!")
    except:
        print("Unable to locate the latest email.")

    # === Step 4: Click first link in email body ===
    try:
        email_link = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='a3s aiL ']//a[contains(@href, 'http')]")
        ))
        print("Found link:", email_link.get_attribute("href"))
        email_link.click()
        print("Link clicked successfully!")

        # Switch to new tab (if opened)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        print("Switched to new tab.")
        print("Current URL:", driver.current_url)

    except:
        print("No link found in the email body.")

    # Optional: Keep window open for observation
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
    print("Browser closed.")
