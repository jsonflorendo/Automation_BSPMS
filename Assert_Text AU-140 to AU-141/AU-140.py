import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://10.10.99.18:8002/login")
#driver.maximize_window()
#driver.execute_script("document.body.style.zoom='50%'")


wait = WebDriverWait(driver, 15)

username_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
username_input.send_keys("bnjmntumbaga@gmail.com")

password_input = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_input.send_keys("Dost@123")

login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
login_button.click()

time.sleep(3)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])


TARGET_URL = "http://10.10.99.18:8002/auditDetails/82"
driver.get(TARGET_URL)
time.sleep(3)
driver.execute_script("window.scrollBy(0, 500);")
driver.execute_script("document.body.style.zoom='80%'")

auditPlanSelect = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='auditPlanSelect']")))
auditPlanSelect.click()

time.sleep(1)

wait.until(EC.element_to_be_clickable((By.XPATH, "//option[normalize-space()='VIII. Audit Team and Audit Assignment']"))).click()

auditPlanSelect = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='auditPlanSelect']")))
auditPlanSelect.click()

time.sleep(1)
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

try:
    team_leader_label = driver.find_element(By.XPATH, "//label[@for='aud_ldr_aur_id']")
    assert team_leader_label.text.strip() == "Team Leader", "Incorrect spelling"
    print("✅team_leader_label Passed")
except NoSuchElementException:
    print("❌ Test Case 2 Failed: Please display Team Leader label")
except AssertionError as e:
    print(f"T❌ est Case 2 Failed: {e}")

time.sleep(1)

team_leader_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "aud_ldr_aur_id")))
team_leader_dropdown.click()
team_leader_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='4'][normalize-space()='Catherine Enguerra. Bolido, DOST-NCR']")))
team_leader_option.click()

try:
    selected_option = Select(team_leader_dropdown).first_selected_option
    assert selected_option.text.strip() == "Catherine Enguerra. Bolido, DOST-NCR", "Selected option is incorrect"
    print("✅ Test Passed: Correct Team Leader selected and option was clickable!")
except NoSuchElementException:
    print("❌ Test Failed: Dropdown not found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

time.sleep(1)

try:
    Assistant_team_leader_label = driver.find_element(By.XPATH, "(//label[normalize-space()='Assistant Team Leader'])[1]")
    assert Assistant_team_leader_label.text.strip() == "Assistant Team Leader", "Incorrect spelling"
    print("✅Assistant Team Leader Passed")
except NoSuchElementException:
    print("❌ Test Case 2 Failed: Please display Team Leader label")
except AssertionError as e:
    print(f"T❌ est Case 2 Failed: {e}")

time.sleep(1)
Assistant_team_leader_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "aud_asst_aur_id")))
Assistant_team_leader_dropdown.click()
Assistant_team_leader_option = wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[@value='12'][normalize-space()='Juan S. Santos, FNRI'])[2]")))
Assistant_team_leader_option.click()

time.sleep(1)

try:
    selected_option = Select(Assistant_team_leader_dropdown).first_selected_option
    assert selected_option.text.strip() == "Juan S. Santos, FNRI", "Selected option is incorrect"
    print("✅Test Passed: Correct Assistant Team Leader selected and option was clickable!")
except NoSuchElementException:
    print("❌ Test Failed: Dropdown not found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### Audit Team Add Button
time.sleep(1)
try:
    Audit_Team_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='audit-teams-modal-trigger'])[1]")))

    if Audit_Team_add_button.is_enabled():
        Audit_Team_add_button.click()
        print("✅ Button clicked successfully!")
    else:
        print("❌ Button is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(1)
####################### Audit Team Add Button Close
try:
    Audit_Team_add_button_close = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])[5]")))

    if Audit_Team_add_button_close.is_enabled():
        Audit_Team_add_button_close.click()
        print("✅ Close Button clicked successfully!")
    else:
        print("❌ Close Button is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(1)
############### Rate Icon
try:
    Rate_icon_button = driver.find_element(By.XPATH, "(//i[@class='fas fa-plus text-white-100'])[2]")
    assert Rate_icon_button is not None, "❌ Rate Icon Button does not exist!"
    assert Rate_icon_button.is_enabled(), "❌ Rate Icon Button is not clickable!"
    Rate_icon_button.click()
    print("❌ Rate Icon Button does not exist!")

except NoSuchElementException:
    print("✅ Rate Icon Button clicked successfully!")
except AssertionError as e:
    print(f"❌ Assertion failed: {e}")
except Exception as e:
    print(f"❌ Error: {e}")

####################### Audit Team Table
time.sleep(1)
Audit_Team_Table = wait.until(EC.element_to_be_clickable((By.XPATH, "(//table[@id='DataTables_Table_3'])[1]")))
print("✅ Audit Team Table clicked successfully!")


###################### Audit Team Table Close
time.sleep(2)
try:
    Audit_Team_Table_close = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])[5]")))

    if Audit_Team_Table_close.is_enabled():
        Audit_Team_Table_close.click()
        print("✅ Audit Team Table Close clicked successfully!")
    else:
        print("❌ Audit Team Table Close is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(1)

#################### table #################

try:
    Audit_Assignment_label = driver.find_element(By.XPATH, "(//span[normalize-space()='Audit Assignment'])[1]")
    assert Audit_Assignment_label.text.strip() == "Audit Assignment", "Incorrect spelling"
    print("✅Test Passed: Audit Assignment Passed")
except NoSuchElementException:
    print("❌test Failed:Audit Assignment Incorrect spelling")
except AssertionError as e:
    print(f"❌Test Failed: {e}")


try:
    Audit_Team_Members_label = driver.find_element(By.XPATH, "(//span[normalize-space()='Audit Team Members'])[1]")
    assert Audit_Team_Members_label.text.strip() == "Audit Team Members", "Incorrect spelling"
    print("✅Test Passed: Audit Team Members Passed")
except NoSuchElementException:
    print("❌test Failed: Audit Team Members Incorrect spelling")
except AssertionError as e:
    print(f"❌Test Failed: {e}")


try:
    Target_Completion_label = driver.find_element(By.XPATH, "(//span[normalize-space()='Target Completion'])[1]")
    assert Target_Completion_label.text.strip() == "Target Completion", "Incorrect spelling"
    print("✅Test Passed: Target Completion Passed")
except NoSuchElementException:
    print("❌test Failed: Target Completion Incorrect spelling")
except AssertionError as e:
    print(f"❌Test Failed: {e}")


try:
    Office_Division_Section_label = driver.find_element(By.XPATH, "(//span[normalize-space()='Office/Divison/Section'])[1]")
    assert Office_Division_Section_label.text.strip() == "Office/Division/Section", "Office/Division/Section Incorrect spelling"
    print("✅Test Passed: Office/Division/Section Passed")
except NoSuchElementException:
    print("❌test Failed: Office/Division/Section Incorrect spelling")
except AssertionError as e:
    print(f"❌Test Failed: {e}")

####################### Up Down Button
try:
    up_down_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='dt-column-order'])[18]")))

    if up_down_button.is_enabled():
        up_down_button.click()
        print("✅ Up Down Arrow Button clicked successfully!")
    else:
        print("❌ Up Down Arrow Button is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")


time.sleep(2)
driver.quit()
