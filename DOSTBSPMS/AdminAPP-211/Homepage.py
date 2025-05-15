from Login import LoginPage
from Trackmodal import TrackModal
from Attachmodal import AttachModal  # Importing the original AttachModal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class Homepage:
    def __init__(self):
        self.login_page = LoginPage()
        self.driver = None

    def login_and_initialize(self):
        """
        Logs in and initializes the WebDriver instance.
        """
        self.login_page.login()
        self.driver = self.login_page.get_driver()

    def click_ellipsis(self):
        """
        Clicks the ellipsis button on the first row of the table.
        """
        try:
            ellipsis_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((
                    By.XPATH, "//tbody/tr[1]/td[6]/div[1]/button[1]//*[name()='svg']"
                ))
            )
            ellipsis_button.click()
            print("Ellipsis button clicked successfully.")
        except Exception as e:
            print(f"An error occurred while clicking the ellipsis button: {e}")

    def click_track_button(self):
        """
        Clicks the 'Track' button after the ellipsis is clicked.
        """
        try:
            track_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='track-menu-item']"))
            )
            track_button.click()
            print("Track button clicked successfully.")
        except Exception as e:
            print(f"An error occurred while clicking the Track button: {e}")

    def handle_track_modal(self):
        """
        Handles the 'Track' modal by filling in details, submitting the form, and handling the success modal.
        """
        try:
            track_modal = TrackModal(self.driver)
            track_modal.click_add_button()
            track_modal.fill_tracking_form(
                concern="Approval",         # Concern to select
                start_date="05/01/2025",     # Start date in MM/DD/YYYY format
                end_date="05/08/2025",       # End date in MM/DD/YYYY format
                forward_to="Technical Evaluator",  # Forward to person/role
                remarks="Approval comment goes here."  # Remarks or comments
            )
            track_modal.submit_form()
            print("Track modal handled successfully.")
        except Exception as e:
            print(f"An error occurred while handling the Track modal: {e}")

    def click_attach_button(self):
        """
        Clicks the 'Attach' button after the ellipsis is clicked.
        """
        try:
            attach_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='attach-menu-item']"))
            )
            attach_button.click()
            print("Attach button clicked successfully.")
        except Exception as e:
            print(f"An error occurred while clicking the Attach button: {e}")

    def upload_attachments(self):
        """
        Uploads the attachments to the AttachModal.
        """
        attach_modal = AttachModal(self.driver)
        pdf_files = {
            "descent_proof": "C:\\Users\\Wendell\\PycharmProjects\\DOSTBPMS\\Admin\\Files\\eq2.pdf",
            "draft_contract": "C:\\Users\\Wendell\\PycharmProjects\\DOSTBPMS\\Admin\\Files\\eq2.pdf",
            "prc_clearance": "C:\\Users\\Wendell\\PycharmProjects\\DOSTBps\\Files\\Eq1.pdf",
            "justification": "C:\\Users\\Wendell\\PycharmProjects\\DOSTBPMS\\Admin\\Files\\sam2.pdf",
            "ias": "C:\\Users\\Wendell\\PycharmProjects\\DOSTBPMS\\Admin\\Files\\sam12.pdf",
            "terminal_report": "C:\\Users\\Wendell\\PycharmProjects\\DOSTBPMS\\Admin\\Files\\sample.pdf",
        }

        # Upload the standard files
        for form_name, file_path in pdf_files.items():
            attach_modal.upload_file(form_name, file_path)

        # Handle "Other Documents" specifically
        attach_modal.fill_other_documents(
            document_name="Custom Document Name",
            file_path="C:\\Users\\Wendell\\PycharmProjects\\DOSTBPMS\\Admin\\Files\\sample.pdf"
        )

        # Close the modal by clicking OK
        attach_modal.close_modal()

    def execute_workflow(self):
        """
        Executes the complete workflow: login, click ellipsis, handle the 'Track' modal,
        click 'Attach', and upload attachments.
        """
        self.login_and_initialize()
        self.click_ellipsis()
        self.click_track_button()
        self.handle_track_modal()
        self.click_ellipsis()  # Click ellipsis again for Attach
        self.click_attach_button()
        self.upload_attachments()
        print("Waiting for 5 seconds before closing the browser...")
        time.sleep(5)
        self.driver.quit()

if __name__ == "__main__":
    homepage = Homepage()
    homepage.execute_workflow()