from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver for Firefox
driver = webdriver.Firefox()

try:
    # Open the URL
    url = "http://10.10.99.18:8005/application/6UqqLRyj6Q4reyNxQRINmr3tHNll0521gqAVez6mCqBvFgVLlXEEbPXsYIPo/form001p2"
    driver.get(url)

    # Wait for the page to load
    time.sleep(8)

    # Click the edit icon
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "i[class='edit-tor-icon icon-[fa6-solid--pen-to-square] cursor-pointer']"))
    ).click()
    time.sleep(6)

    # --- Handle the Network Section ---
    network_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='part6_network']"))
    )
    driver.execute_script("arguments[0].click();", network_checkbox)  # Click the hidden checkbox
    time.sleep(2)

    network_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_6_add']"))
    )
    network_add_button.click()
    time.sleep(5)

    network_title = driver.find_element(By.XPATH, "//input[@id='network_title']")
    network_title.send_keys("Network Title")  # Example network title

    dropdown = driver.find_element(By.XPATH, "//select[@id='network_specific']")
    driver.execute_script("arguments[0].value = 'Commitment Letter';", dropdown)  # Select dropdown value
    dropdown.click()
    time.sleep(1)

    network_output = driver.find_element(By.XPATH, "//textarea[@id='network_output']")
    network_output.send_keys("Expected network outputs.")  # Example output

    network_save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_6_save']"))
    )
    network_save_button.click()
    time.sleep(5)

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
    )
    ok_button.click()
    time.sleep(3)

    # --- Handle the Publication Section ---
    publication_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='part6_publication']"))
    )
    driver.execute_script("arguments[0].click();", publication_checkbox)  # Click the hidden checkbox
    time.sleep(2)

    publication_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_7_add']"))
    )
    publication_add_button.click()
    time.sleep(5)

    publication_title = driver.find_element(By.XPATH, "//input[@id='publication_title']")
    publication_title.send_keys("Publication Title")

    publication_specific = driver.find_element(By.XPATH, "//input[@id='publication_specific']")
    publication_specific.send_keys("Publication Specific")

    publication_specific2 = driver.find_element(By.XPATH, "//input[@id='publication_specific2']")
    publication_specific2.send_keys("05/06/2025")  # Example date in mm/dd/yyyy format

    publication_save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_7_save']"))
    )
    publication_save_button.click()
    time.sleep(5)

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
    )
    ok_button.click()
    time.sleep(3)

    # --- Handle the Research Section ---
    research_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='part6_research']"))
    )
    driver.execute_script("arguments[0].click();", research_checkbox)  # Click the hidden checkbox
    time.sleep(2)

    research_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_8_add']"))
    )
    research_add_button.click()
    time.sleep(5)

    research_title = driver.find_element(By.XPATH, "//input[@id='research_title']")
    research_title.send_keys("Research Title")

    research_problem = driver.find_element(By.XPATH, "//textarea[@id='research_problem']")
    research_problem.send_keys("Research Problem Description")

    research_impact = driver.find_element(By.XPATH, "//textarea[@id='research_impact']")
    research_impact.send_keys("Research Impact Description")

    research_output = driver.find_element(By.XPATH, "//textarea[@id='research_output']")
    research_output.send_keys("Research Output Description")

    research_save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='part6_8_save']"))
    )
    research_save_button.click()
    time.sleep(5)

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
    )
    ok_button.click()
    time.sleep(3)

    # --- Handle the Support Section ---
    support_add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='part7_add']"))
    )
    support_add_button.click()
    time.sleep(5)

    support_activities = driver.find_element(By.XPATH, "//input[@id='support_activities']")
    support_activities.send_keys("Support Activity Example")  # Example activity

    support_nature = driver.find_element(By.XPATH, "//input[@id='support_nature']")
    support_nature.send_keys("Support Nature Example")  # Example nature

    support_details = driver.find_element(By.XPATH, "//textarea[@id='support_details']")
    support_details.send_keys("Detailed description of the support activities.")  # Example details

    support_save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='part7_save']"))
    )
    support_save_button.click()
    time.sleep(5)

    ok_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']"))
    )
    ok_button.click()
    time.sleep(3)

    # --- Handle the Close Button ---
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='tor_close']"))
    )
    close_button.click()
    time.sleep(3)

    # --- Handle the Next Button ---
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@id='next']"))
    )
    next_button.click()
    time.sleep(6)

finally:
    # Gracefully close the browser
    driver.quit()