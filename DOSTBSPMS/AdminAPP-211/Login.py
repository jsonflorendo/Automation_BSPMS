from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    def __init__(self):
        # Initialize WebDriver (using Firefox in this case)
        self.driver = webdriver.Firefox()

        # Login credentials (stored here for exclusive use)
        self.username = "sjjinahon@gmail.com"
        self.password = "Dost@123"

    def login(self):
        """
        Logs into the system using the stored username and password.
        """
        self.driver.get("http://10.10.99.18:8004/login")
        self.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(self.username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(self.password)

        # Click the login button using WebDriver and the provided XPath
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='login']"))
        )
        login_button.click()

        # Wait for a few seconds to allow the login process to complete
        time.sleep(5)

        # Conditional check: Determine if login was successful
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
            )
            print("Login failed. Login form is still visible.")
        except Exception:
            print("Successfully logged in. Login form is no longer visible.")

    def get_driver(self):
        """
        Returns the WebDriver instance for further use.
        """
        return self.driver