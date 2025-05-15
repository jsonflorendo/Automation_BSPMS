from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AttachModal:
    def __init__(self, driver):
        self.driver = driver

    def handle_existing_file(self, file_input_id):
        """
        Handles the case where a file is already uploaded.
        Clicks the input ID to trigger the Remove modal and confirms removal.

        :param file_input_id: The ID of the file input element.
        """
        try:
            # Click the file input ID to trigger the Remove modal
            file_input = self.driver.find_element(By.ID, file_input_id)
            file_input.click()
            print(f"Clicked file input with ID: {file_input_id} to trigger Remove modal.")

            # Click the "Remove" button in the modal
            remove_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Remove']"))
            )
            remove_button.click()
            print(f"'Remove' button clicked for file input with ID: {file_input_id}.")

            # Confirm the removal by clicking the "OK" button
            ok_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
            )
            ok_button.click()
            print(f"'OK' button clicked to confirm removal for file input with ID: {file_input_id}.")
        except Exception as e:
            print(f"An error occurred while handling existing file for input {file_input_id}: {e}")

    def upload_file(self, file_input_id, file_path):
        """
        Uploads a file to the specified file input element by ID.
        If a file is already present, handles its removal first.

        :param file_input_id: The ID of the file input element.
        :param file_path: The path of the file to upload.
        """
        try:
            # Handle existing file if present
            self.handle_existing_file(file_input_id)

            # Find the hidden file input element by ID and send the file path
            file_input = self.driver.find_element(By.ID, file_input_id)
            file_input.send_keys(file_path)
            print(f"File uploaded successfully to input with ID: {file_input_id}")
        except Exception as e:
            print(f"An error occurred while uploading the file to input {file_input_id}: {e}")

    def fill_other_documents(self, document_name, file_path):
        """
        Fills the "Other Documents" name and uploads the corresponding file.
        If a file is already present, handles its removal first.

        :param document_name: Name for the "Other Documents" input field.
        :param file_path: The path of the file to upload.
        """
        try:
            # Find the "Other Documents Specific" text input and enter the document name
            other_documents_input = self.driver.find_element(By.ID, "other_documents_specific")
            other_documents_input.send_keys(document_name)
            print(f"Other Documents name set to: {document_name}")

            # Upload the file for "Other Documents"
            self.upload_file("other_documents", file_path)
        except Exception as e:
            print(f"An error occurred while handling other documents: {e}")

    def close_modal(self):
        """
        Clicks the 'OK' button to close the modal.
        """
        try:
            ok_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
            )
            ok_button.click()
            print("OK button clicked, modal closed successfully.")
        except Exception as e:
            print(f"An error occurred while closing the Attach Modal: {e}")