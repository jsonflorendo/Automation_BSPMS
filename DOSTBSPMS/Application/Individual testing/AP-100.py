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

    # Wait for the page to load fully
    time.sleep(8)

    # Click the edit icon before filling the forms
    edit_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "i[class='edit-tor-icon icon-[fa6-solid--pen-to-square] cursor-pointer']"))
    )
    edit_icon.click()
    time.sleep(6)

    # Fill the text areas for parts 1, 2, and 3
    driver.find_element(By.ID, "part1").send_keys("Detailed information for part1")
    driver.find_element(By.ID, "part2").send_keys("Detailed information for part2")
    driver.find_element(By.ID, "part3").send_keys("Detailed information for part3")

    # Click the continuous start input
    continuous_start = driver.find_element(By.ID, "continuous_start")
    continuous_start.click()

    # Wait for the calendar to open and select the start date (May 6, 2025)
    start_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'flatpickr-calendar') and contains(@class,'open')]//span[@aria-label='May 6, 2025' and normalize-space()='6']"))
    )
    start_date.click()

    # Wait for the calendar to process the input
    time.sleep(2)

    # Click the continuous end input
    continuous_end = driver.find_element(By.ID, "continuous_end")
    continuous_end.click()

    # Wait for the calendar to open and select the end date (May 30, 2025)
    end_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'flatpickr-calendar') and contains(@class,'open')]//span[@aria-label='May 30, 2025' and normalize-space()='30']"))
    )
    end_date.click()





finally:
    time.sleep(10)
    # Close the browser
    driver.quit()