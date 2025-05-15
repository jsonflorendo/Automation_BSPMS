from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Define the URL to make it easy to replace
URL = "http://10.10.99.18:8005/application/6UqqLRyj6Q4reyNxQRINmr3tHNll0521gqAVez6mCqBvFgVLlXEEbPXsYIPo/form001p1.2"

def handle_area_of_expertise(driver):
    try:
        area_of_expertise_trigger = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ss-main"))
        )
        area_of_expertise_trigger.click()
        print("Opened the 'Area of Expertise' dropdown.")

        area_of_expertise_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='ss-content slimSelect-add ss-open-below']//input[contains(@placeholder,'')]")
            )
        )
        area_of_expertise_value = "Dentistry"
        area_of_expertise_input.send_keys(area_of_expertise_value)
        print(f"Typed '{area_of_expertise_value}' into the 'Area of Expertise' dropdown.")

        registered_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='ss-content slimSelect-add ss-open-below']//div[@class='ss-addable']")
            )
        )
        registered_option.click()
        print("Selected 'Registered' option in 'Area of Expertise' dropdown.")

        time.sleep(2)

    except Exception as e:
        print(f"Error in 'Area of Expertise': {e}")


def handle_specialization(driver):
    try:
        specialization_trigger = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='form-layout']//div[@class='ss-placeholder']"))
        )
        specialization_trigger.click()
        print("Opened the 'Specialization' dropdown.")

        specialization_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='ss-content slimSelect-add ss-open-below']//input[contains(@placeholder,'')]")
            )
        )
        specialization_value = "Orthodontics"
        specialization_input.send_keys(specialization_value)
        print(f"Typed '{specialization_value}' into the 'Specialization' dropdown.")

        specialization_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='ss-content slimSelect-add ss-open-below']//div[@class='ss-addable']")
            )
        )
        specialization_option.click()
        print(f"Selected '{specialization_value}' from the 'Specialization' dropdown.")

    except Exception as e:
        print(f"Error in 'Specialization': {e}")


def handle_education_level_and_school(driver):
    try:
        education_level_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='temp_education_level']"))
        )
        select = Select(education_level_dropdown)
        select.select_by_visible_text("Doctorate Degree")
        print("Selected 'Doctorate Degree' from the 'Education Level' dropdown.")

        school_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='School']"))
        )
        school_name = "UP DILIMAN"
        school_input.send_keys(school_name)
        print(f"Entered '{school_name}' into the 'School' input field.")
        time.sleep(2)

    except Exception as e:
        print(f"Error in handling 'Education Level' and 'School': {e}")


def handle_country(driver):
    try:
        country_dropdown_trigger = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='education-row-1']/td[2]/div/div"))
        )
        country_dropdown_trigger.click()
        print("Opened the 'Country' dropdown.")

        country_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='ss-content auto-width ss-open-below']//input[contains(@placeholder,'')]")
            )
        )
        country_name = "Philippines"
        country_input.send_keys(country_name)
        print(f"Typed '{country_name}' into the 'Country' dropdown.")
        time.sleep(4)

        country_input.send_keys(Keys.ARROW_DOWN)
        country_input.send_keys(Keys.ENTER)
        print(f"Selected '{country_name}' from the 'Country' dropdown.")

    except Exception as e:
        print(f"Error in handling 'Country': {e}")


def handle_course(driver):
    try:
        course_dropdown_trigger = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Course')]"))
        )
        course_dropdown_trigger.click()
        print("Opened the 'Course' dropdown.")

        course_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='ss-content auto-width ss-open-below']//input[contains(@placeholder,'')]")
            )
        )
        course_name = "Computer Science"
        course_input.send_keys(course_name)
        print(f"Typed '{course_name}' into the 'Course' dropdown.")

        course_register = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//div[@class='ss-content auto-width ss-open-below']//div[@class='ss-addable']//*[name()='svg']//*[name()='path' and contains(@d,'M50,10 L50')]")
            )
        )
        course_register.click()
        print(f"Selected '{course_name}' from the 'Course' dropdown.")
        time.sleep(2)

    except Exception as e:
        print(f"Error in handling 'Course': {e}")


def handle_graduated_year(driver, year):
    try:
        graduated_year_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Ongoing']"))
        )
        graduated_year_input.clear()
        graduated_year_input.send_keys(year)
        print(f"Entered '{year}' into the 'Graduated Year' input field.")
        time.sleep(2)

    except Exception as e:
        print(f"Error in handling 'Graduated Year': {e}")


def handle_save_education(driver):
    try:
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//tr[@id='education-row-1']//i[@class='save-icon tippy icon-[mdi--check-circle-outline] text-xl text-center text-green-500 cursor-pointer px-2']")
            )
        )
        save_button.click()
        print("Clicked the 'Save' button for education.")
        time.sleep(2)

    except Exception as e:
        print(f"Error in handling 'Save Education': {e}")


def handle_work_experience(driver, company, country, position, from_year, present_year):
    try:
        # Step 1: Pick a company
        company_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Company']"))
        )
        company_input.send_keys(company)
        print(f"Entered company: {company}")

        # Step 2: Select a country
        country_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tr[@id='work-row-1']//div[@class='ss-placeholder'][normalize-space()='Country']"))
        )
        country_dropdown.click()
        print("Opened the 'Country' dropdown for work experience.")

        country_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='ss-content auto-width ss-open-below']//input[contains(@placeholder,'')]")
            )
        )
        country_input.send_keys(country)
        print(f"Typing country: {country}")

        # Add a slight delay to ensure the dropdown processes the input
        time.sleep(2)

        # Simulate selecting the dropdown option
        country_input.send_keys(Keys.ARROW_DOWN)
        country_input.send_keys(Keys.ENTER)
        print(f"Selected country: {country}")

        # Add another delay before moving to the next step to avoid racing conditions
        time.sleep(2)

        # Step 3: Pick a position
        position_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Position']"))
        )
        position_input.send_keys(position)
        print(f"Entered position: {position}")

        # Step 4: Enter the start year (From)
        from_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='From']"))
        )
        from_input.send_keys(from_year)
        print(f"Entered start year (From): {from_year}")

        # Press Enter to save the "From" year
        from_input.send_keys(Keys.ENTER)
        print("Saved the 'From' year by pressing Enter.")

        # Wait 5 seconds to ensure the "From" field saves properly
        time.sleep(5)

        # Step 5: Enter the end year (Present)
        present_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Present']"))
        )
        present_input.send_keys(present_year)
        print(f"Entered end year (Present): {present_year}")

        # Step 6: Save the work experience
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//tr[@id='work-row-1']//i[@class='save-icon tippy icon-[mdi--check-circle-outline] text-xl text-center text-green-500 cursor-pointer px-2']")
            )
        )
        save_button.click()
        print("Clicked the 'Save' button for work experience.")
        time.sleep(2)

    except Exception as e:
        print(f"Error in handling work experience: {e}")


def handle_next_button(driver):
    try:
        # Wait for the "Next" button to be clickable
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='next']"))
        )
        next_button.click()
        print("Clicked the 'Next' button to proceed to the next page.")
        time.sleep(3)  # Wait for the next page to load
    except Exception as e:
        print(f"Error in handling the 'Next' button: {e}")


def main():
    driver = webdriver.Firefox()

    try:
        driver.get(URL)
        print(f"Page loaded successfully: {URL}")

        # Fill out each section step by step
        handle_area_of_expertise(driver)
        handle_specialization(driver)
        handle_education_level_and_school(driver)
        handle_country(driver)
        handle_course(driver)
        handle_graduated_year(driver, "2025")  # Pass the graduated year here
        handle_save_education(driver)

        # Handle work experience section
        handle_work_experience(
            driver,
            company="Example Company",
            country="United States",
            position="Software Engineer",
            from_year="2020",
            present_year="2025"
        )

        # Click the "Next" button to proceed
        handle_next_button(driver)

        # Placeholder for additional steps on the next page
        print("You can now proceed with the next page's automation.")

    finally:
        time.sleep(5)
        driver.quit()
        print("Browser closed.")


if __name__ == "__main__":
    main()