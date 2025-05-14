from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def handle_form(driver):
    try:
        print("Starting AP-111 form processing...")

        # Wait for the page to load fully
        time.sleep(8)

        # Handle the project section
        project_checkbox = driver.find_element(By.XPATH, "//input[@id='part6_project']")
        driver.execute_script("arguments[0].click();", project_checkbox)  # Interact with the project checkbox
        time.sleep(2)  # Wait for the table to appear

        project_add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_3_add']"))
        )
        project_add_button.click()
        time.sleep(5)  # Wait for the modal to appear

        project_title = driver.find_element(By.XPATH, "//input[@id='project_title']")
        project_title.send_keys("Sample Project Title")

        project_problem = driver.find_element(By.XPATH, "//textarea[@id='project_problem']")
        project_problem.send_keys("Sample problem description.")

        project_impact = driver.find_element(By.XPATH, "//textarea[@id='project_impact']")
        project_impact.send_keys("Sample impact details.")

        project_specific = driver.find_element(By.XPATH, "//input[@id='project_specific']")
        project_specific.send_keys("Specific details for the project.")

        project_output = driver.find_element(By.XPATH, "//textarea[@id='project_output']")
        project_output.send_keys("Expected project outputs.")

        project_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_3_save']"))
        )
        project_save_button.click()
        time.sleep(5)

        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
        )
        ok_button.click()
        time.sleep(3)

        # Handle the student section
        student_checkbox = driver.find_element(By.XPATH, "//input[@id='part6_student']")
        driver.execute_script("arguments[0].click();", student_checkbox)
        time.sleep(2)

        student_add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_4_add']"))
        )
        student_add_button.click()
        time.sleep(5)

        student_title = driver.find_element(By.XPATH, "//input[@id='student_title']")
        student_title.send_keys("Student Name")

        student_specific = driver.find_element(By.XPATH, "//input[@id='student_specific2']")
        student_specific.send_keys("Specific details for the student.")

        student_output = driver.find_element(By.XPATH, "//textarea[@id='student_output']")
        student_output.send_keys("Expected student outputs.")

        student_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_4_save']"))
        )
        student_save_button.click()
        time.sleep(5)

        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
        )
        ok_button.click()
        time.sleep(3)

        # Handle the curriculum section
        curriculum_checkbox = driver.find_element(By.XPATH, "//input[@id='part6_course']")
        driver.execute_script("arguments[0].click();", curriculum_checkbox)
        time.sleep(2)

        curriculum_add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_5_add']"))
        )
        curriculum_add_button.click()
        time.sleep(5)

        curriculum_title = driver.find_element(By.XPATH, "//input[@id='course_title']")
        curriculum_title.send_keys("Curriculum Title")

        curriculum_problem = driver.find_element(By.XPATH, "//textarea[@id='course_problem']")
        curriculum_problem.send_keys("Curriculum problem description.")

        curriculum_output = driver.find_element(By.XPATH, "//textarea[@id='course_output']")
        curriculum_output.send_keys("Expected curriculum outputs.")

        curriculum_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_5_save']"))
        )
        curriculum_save_button.click()
        time.sleep(5)

        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
        )
        ok_button.click()
        time.sleep(3)

        print("AP-111 form completed successfully")

    except Exception as e:
        print(f"Error in AP-111 form: {e}")