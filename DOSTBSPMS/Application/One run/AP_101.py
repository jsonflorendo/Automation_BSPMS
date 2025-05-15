from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def handle_form(driver):
    try:
        print("Starting AP-101 form processing...")

        # Wait for the page to load
        time.sleep(8)

        # Click the Part 5 button to open the modal
        part5_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part5_add']"))
        )
        part5_button.click()
        print("Opened Part 5 modal.")

        # Open the dropdown for activity selection
        activity_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='activity']"))
        )
        activity_dropdown.click()
        time.sleep(2)  # Pause for the dropdown to appear

        # Select the second option from the dropdown
        option_to_select = driver.find_element(By.XPATH, "//select[@id='activity']/option[2]")  # Adjust [2] for the desired option index
        option_to_select.click()
        print("Selected activity from the dropdown.")

        # Fill in the activity start and end dates
        activity_start = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='activity_start']"))
        )
        activity_start.click()
        activity_start.send_keys("05/07/2025")  # Enter start date in mm/dd/yyyy format
        time.sleep(2)

        activity_end = driver.find_element(By.XPATH, "//input[@id='activity_end']")
        activity_end.click()
        activity_end.send_keys("05/10/2025")  # Enter end date in mm/dd/yyyy format
        time.sleep(2)

        # Fill in the deliverables
        activity_deliverable = driver.find_element(By.XPATH, "//textarea[@id='activity_deliverable']")
        activity_deliverable.send_keys("This activity aims to accomplish specific deliverables outlined in this section.")
        print("Filled activity details.")

        # Save the activity modal
        part5_save = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part5_save']"))
        )
        part5_save.click()
        print("Saved activity details.")
        time.sleep(4)

        # Confirm success modal and click the OK button
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
        )
        ok_button.click()
        print("Confirmed success modal.")
        time.sleep(6)

        # Handle the seminar section
        seminar_checkbox = driver.find_element(By.XPATH, "//input[@id='part6_seminar']")
        driver.execute_script("arguments[0].click();", seminar_checkbox)
        print("Checked seminar section.")
        time.sleep(2)

        seminar_add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_1_add']"))
        )
        seminar_add_button.click()
        time.sleep(2)

        seminar_title = driver.find_element(By.XPATH, "//input[@id='seminar_title']")
        seminar_title.send_keys("The Future of Technology")

        seminar_specific = driver.find_element(By.XPATH, "//input[@id='seminar_specific']")
        seminar_specific.send_keys("Specific Topic 1")

        seminar_specific2 = driver.find_element(By.XPATH, "//input[@id='seminar_specific2']")
        seminar_specific2.send_keys("Specific Topic 2")

        seminar_output = driver.find_element(By.XPATH, "//textarea[@id='seminar_output']")
        seminar_output.send_keys("This seminar will focus on future trends in technology and innovation.")
        print("Filled seminar details.")

        seminar_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_1_save']"))
        )
        seminar_save_button.click()
        print("Saved seminar details.")
        time.sleep(5)

        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
        )
        ok_button.click()
        print("Confirmed seminar success modal.")
        time.sleep(7)

        # Handle the training section
        training_checkbox = driver.find_element(By.XPATH, "//input[@id='part6_training']")
        driver.execute_script("arguments[0].click();", training_checkbox)
        print("Checked training section.")
        time.sleep(2)

        training_add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_2_add']"))
        )
        training_add_button.click()
        time.sleep(2)

        training_title = driver.find_element(By.XPATH, "//input[@id='training_title']")
        training_title.send_keys("Advanced Python Training")

        training_specific = driver.find_element(By.XPATH, "//input[@id='training_specific']")
        training_specific.send_keys("Python Best Practices")

        training_specific2 = driver.find_element(By.XPATH, "//input[@id='training_specific2']")
        training_specific2.send_keys("Python for Automation")

        training_output = driver.find_element(By.XPATH, "//textarea[@id='training_output']")
        training_output.send_keys("This training focuses on advanced Python techniques for automation.")
        print("Filled training details.")

        training_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_2_save']"))
        )
        training_save_button.click()
        print("Saved training details.")
        time.sleep(5)

        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
        )
        ok_button.click()
        print("Confirmed training success modal.")

        print("AP-101 form completed successfully.")

    except Exception as e:
        print(f"Error in AP-101 form: {e}")