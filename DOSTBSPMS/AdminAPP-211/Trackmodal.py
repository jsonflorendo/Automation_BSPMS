from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class TrackModal:
    def __init__(self, driver):
        self.driver = driver
        self.concern_xpaths = {
            "Approval": "//body//div//div[@role='dialog']//div//div//div//div//div//div//div[1]//label[1]//div[1]//i[1]",
            # Add other concerns here if needed
        }
        self.start_date_input = (By.XPATH, "//input[@id='start_date']")
        self.end_date_input = (By.XPATH, "//input[@id='end_date']")
        self.forward_dropdown = (By.XPATH, "//select[@id='forward_to']")
        self.remarks_textarea = (By.XPATH, "//textarea[@id='remarks']")
        self.submit_button = (By.XPATH, "//button[@id='track_submit']")  # Updated XPath for the submit button
        self.success_modal = (By.XPATH, "//div[@class='swal2-popup swal2-modal swal2-icon-success swal2-show']")
        self.ok_button = (By.XPATH, "//button[normalize-space()='OK']")
        self.close_button = (By.XPATH, "//button[@class='text-white bg-gray-600 hover:bg-bsp-blue focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium text-sm text-center rounded-lg px-4 py-1 my-2 tracking-modal-close']")

    def click_add_button(self):
        """Clicks the 'Add' button."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='icon-[mdi--caret-down] w-6 h-6']"))
        ).click()

    def fill_tracking_form(self, concern, start_date, end_date, forward_to, remarks):
        """Fills the Action Tracking form with the provided data."""
        # Select the checkbox for the single concern
        if concern in self.concern_xpaths:
            concern_xpath = self.concern_xpaths[concern]
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, concern_xpath))
            ).click()
        else:
            raise ValueError(f"Concern '{concern}' does not have a defined XPath.")

        # Input start date
        start_date_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.start_date_input)
        )
        start_date_field.send_keys(start_date)
        start_date_field.send_keys(Keys.RETURN)  # Press Enter to register the input

        # Input end date
        end_date_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.end_date_input)
        )
        end_date_field.send_keys(end_date)
        end_date_field.send_keys(Keys.RETURN)  # Press Enter to register the input

        # Select "Forward To" from dropdown
        forward_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.forward_dropdown)
        )
        forward_field.send_keys(forward_to)
        forward_field.send_keys(Keys.RETURN)  # Press Enter to register the selection

        # Input remarks
        remarks_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remarks_textarea)
        )
        remarks_field.send_keys(remarks)

    def submit_form(self):
        """Clicks the 'Submit' button to finalize the action."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        ).click()
        print("Submit button clicked. Waiting for success modal...")

        # Wait for the success modal to appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.success_modal)
        )
        print("Success modal appeared.")

        # Click the "OK" button in the success modal
        ok_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ok_button)
        )
        ok_button.click()
        print("OK button clicked in the success modal.")

        # Click the "close" button to close the modal
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_button)
        )
        close_button.click()
        print("Close button clicked. Track modal dismissed.")