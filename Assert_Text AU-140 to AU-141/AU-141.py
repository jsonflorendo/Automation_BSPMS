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
driver.maximize_window()
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
####################### Audit Team label
try:
    Audit_Team_label = driver.find_element(By.XPATH, "//h2[normalize-space(text())='Audit Team']")
    actual_text = Audit_Team_label.text.strip()

    assert actual_text == "Audit Team", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Audit Team Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Audit Team Label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

############### select audit area

time.sleep(1)
select_audit_area_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "select-audit-area")))
select_audit_area_dropdown.click()
select_audit_area_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='select-audit-area']//option[@value='2'][normalize-space()='Financial']")))
select_audit_area_option.click()

time.sleep(1)

try:
    selected_option = Select(select_audit_area_dropdown).first_selected_option
    assert selected_option.text.strip() == "Financial", "Selected option is incorrect"
    print("✅Test Passed: Select Audit Area and select was clickable!")
except NoSuchElementException:
    print("❌ Test Failed: Select Audit Area and select is not clickable!")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### select audit area Add Button
time.sleep(1)
try:
    Select_Audit_area_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus text-white-100'])[4]")))

    if Select_Audit_area_add_button.is_enabled():
        Select_Audit_area_add_button.click()
        print("✅ select audit area Add Button clicked successfully!")
    else:
        print("❌ select audit area Add Button is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(1)
####################### select audit areaAdd Button Close
try:
    Select_Audit_area_add_button_close = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Close'])[11]")))

    if Select_Audit_area_add_button_close.is_enabled():
        Select_Audit_area_add_button_close.click()
        print("✅ select audit area Add Close Button clicked successfully!")
    else:
        print("❌ select audit area Add Close Button is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")

####################### ASSIGNED AUDITORS Label

try:
    ASSIGNED_AUDITORS_label = driver.find_element(By.XPATH, "(//label[normalize-space()='ASSIGNED AUDITORS'])[1]")
    actual_text = ASSIGNED_AUDITORS_label.text.strip()

    # Assert that the cleaned-up text is exactly what we expect
    assert actual_text == "ASSIGNED AUDITORS", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: ASSIGNED AUDITORS Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: ASSIGNED AUDITORS Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")


####################### Lead label

try:
    Lead_label = driver.find_element(By.XPATH, "(//label[normalize-space()='Lead'])[1]")
    actual_text = Lead_label.text.strip()

    # Assert that the cleaned-up text is exactly what we expect
    assert actual_text == "Lead", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Lead Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: lead Label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### Lead Selection

time.sleep(1)
Lead_value_dropdown =wait.until(EC.element_to_be_clickable((By.XPATH, "(//select[@id='tm_lead'])[1]")))
Lead_value_dropdown.click()
Lead_value_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='tm_lead']//option[@value='7'][normalize-space()='Jayson Barbara. Florendo, SEI']")))
Lead_value_option.click()
try:
    selected_option = Select(Lead_value_dropdown).first_selected_option
    assert selected_option.text.strip() == "Jayson Barbara. Florendo, SEI", "Selected option is incorrect"
    print("✅Test Passed: Select Audit Area and select was clickable!")
except NoSuchElementException:
    print("❌ Test Failed: Select Audit Area and select is not clickable!")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### External Auditors label

try:
    External_Auditors_label = driver.find_element(By.XPATH, "(//label[normalize-space()='External Auditors'])[1]")
    actual_text = External_Auditors_label.text.strip()

    assert actual_text == "External Auditors", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: External Auditors Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: External Auditors Label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### select External Auditors
# Click the custom dropdown
external_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@role='combobox'])[2]")))
driver.execute_script("arguments[0].click();", external_dropdown)
time.sleep(1)
external_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Juan S. Santos, FNRI')]")))
external_option.click()
print("✅Test Passed: Select Audit Area and select was clickable!")

####################### Internal Auditors label

try:
    internal_Auditors_label = driver.find_element(By.XPATH, "(//label[normalize-space()='Internal Auditors'])[1]")
    actual_text = internal_Auditors_label.text.strip()

    assert actual_text == "Internal Auditors", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Internal Auditors Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Internal Auditors Label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### select Internal Auditors
time.sleep(1)
internal_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@role='combobox'])[3]")))
driver.execute_script("arguments[0].click();", internal_dropdown)
time.sleep(1)
internal_option = wait.until(
EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Shiela Jeane Jinahon. Caraan1, SEI')]")))
internal_option.click()
print("✅Test Passed: Internal Auditors and select was clickable!")

####################### Assignment label
try:
    Assignment_label = driver.find_element(By.XPATH, "(//label[normalize-space()='ASSIGNMENT'])[1]")
    actual_text = Assignment_label.text.strip()

    assert actual_text == "ASSIGNMENT", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Assignment Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Assignment label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    Office_Division_Section_label = driver.find_element(By.XPATH, "(//label[normalize-space()='Office/Division/Section'])[1]")
    actual_text = Office_Division_Section_label .text.strip()

    assert actual_text == "Office/Division/Section", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Office/Division/Section Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Office/Division/Section label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    Internal_Auditors_label = driver.find_element(By.XPATH, "(//label[normalize-space()='Target Completion'])[1]")
    actual_text = Internal_Auditors_label .text.strip()

    assert actual_text == "Target Completion", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Internal Auditors Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Internal Auditors label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### Assignment office

try:
    office = wait.until(EC.presence_of_element_located((By.ID, "office")))
    office.send_keys("TEST")
    assert office.get_attribute(
        "value") == "TEST", f"❌ Test Failed: Expected 'TEST' but got '{office.get_attribute('value')}'"
    print("✅ Test Passed: office was clickable! and 'TEST' was correctly entered into the office field.")

except AssertionError as e:
    print(f"❌ Test Failed: {e}")
except Exception as e:
    print(f"❌ Error: {e}")

####################### Assignment Target Completion

try:
    target_completion = wait.until(EC.presence_of_element_located((By.ID, "target-completion")))
    target_completion.send_keys("5")
    assert target_completion.get_attribute(
        "value") == "5", f"❌ Test Failed: Expected '5' but got '{target_completion.get_attribute('value')}'"
    print("✅ Test Passed: Target Completion was clickable! and '5' was correctly entered into the office field.")

except AssertionError as e:
    print(f"❌ Test Failed: {e}")
except Exception as e:
    print(f"❌ Error: {e}")

####################### Activities Label
try:
    Activities_label = driver.find_element(By.XPATH, "(//label[normalize-space()='ACTIVITIES'])[1]")
    actual_text = Activities_label.text.strip()

    assert actual_text == "ACTIVITIES", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Activities Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Activities label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### WD label
try:
    total_wd_element = driver.find_element(By.XPATH, "(//label[contains(text(),'Total:')])[1]")
    actual_text = total_wd_element.text.strip()

    assert "Total:" in actual_text, f"Incorrect spelling or missing: Found '{actual_text}'"
    print("✅ Test Passed: total_wd Label Found and Correctly Contains 'Total:'")
except NoSuchElementException:
    print("❌ Test Failed: total_wd label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### ACTIVITIES Column
try:
    Activity_Label = driver.find_element(By.XPATH, "(//label[normalize-space()='Activity'])[1]")
    actual_text = Activity_Label.text.strip()

    assert actual_text == "Activity", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Activity Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Activity label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    Methodology_Label = driver.find_element(By.XPATH, "(//label[normalize-space()='Methodology'])[1]")
    actual_text = Methodology_Label.text.strip()
    assert actual_text == "Methodology", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Methodology Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Methodology label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    Documents_Label = driver.find_element(By.XPATH, "(//label[normalize-space()='Documents'])[1]")
    actual_text = Documents_Label.text.strip()
    assert actual_text == "Documents", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Documents Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Documents label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    Auditee_Respondents_Label = driver.find_element(By.XPATH, "(//label[normalize-space()='Auditee/ Respondents'])[1]")
    actual_text = Auditee_Respondents_Label.text.strip()
    assert actual_text == "Auditee/ Respondents", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Auditee/ Respondents Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Auditee/ Respondents label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    No_Hours_Label = driver.find_element(By.XPATH, "(//label[normalize-space()='No. of Hours'])[1]")
    actual_text = No_Hours_Label.text.strip()
    assert actual_text == "No. of Hours", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: No. of Hours Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: No. of Hours label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

####################### Plus and Minus

time.sleep(1)
try:
    Activity_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//i[@class='fas fa-plus'])[8]")))

    if Activity_add_button.is_enabled():
        Activity_add_button.click()
        print("✅ Add Button clicked successfully!")
    else:
        print("❌ Add Button is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(1)

try:
    Activity_Remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@data-btntype='remove-btn'])[1]")))

    if Activity_Remove_button.is_enabled():
        Activity_Remove_button.click()
        print("✅  RemoveButton clicked successfully!")
    else:
        print("❌ Remove Button is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(1)

#################### Remove button label
try:
    Remove_alert_Label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Are you sure you want to delete this item?'])[1]")
    actual_text = Remove_alert_Label.text.strip()

    assert actual_text == "Are you sure you want to delete this item?", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Remove_alert Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Remove_alert label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

time.sleep(1)

ok = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Ok'])[1]")))
ok.click()
print("✅ Test Passed: Ok Found and Correctly Spelled and clickable")


time.sleep(1)

try:
    deleted_successfully = driver.find_element(By.XPATH, "(//h2[normalize-space()='Activity deleted successfully'])[1]")
    actual_text = deleted_successfully.text.strip()

    assert actual_text == "Activity deleted successfully", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Activity deleted successfully  Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Activity deleted successfully label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")
    time.sleep(1)

ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='swal2-actions'])[1]")))
ok_button.click()
time.sleep(1)
print("✅ Test Passed: ok button Found ")

#################### Activities input

time.sleep(1)

activity = wait.until(EC.presence_of_element_located((By.NAME, "activity[]")))
activity.send_keys("test activity")
assert activity.get_attribute("value") == "test activity", "Expected 'test activity' in activity textarea."
print("✅ Test Passed: activity input ")

time.sleep(1)
methodology = wait.until(EC.presence_of_element_located((By.NAME, "methodology[]")))
methodology.send_keys("test methodology")
assert methodology.get_attribute("value") == "test methodology", "Expected 'test methodology' in methodology input."
print("✅ Test Passed: methodology input ")

time.sleep(1)
documents = wait.until(EC.presence_of_element_located((By.NAME, "documents[]")))
documents.send_keys("test documents")
assert documents.get_attribute("value") == "test documents", "Expected 'test documents' in documents textarea."
print("✅ Test Passed: documents input ")

time.sleep(1)
auditee = wait.until(EC.presence_of_element_located((By.NAME, "auditee[]")))
auditee.send_keys("test auditee")
assert auditee.get_attribute("value") == "test auditee", "Expected 'test auditee' in auditee textarea."
print("✅ Test Passed: auditee input ")

time.sleep(1)
no_of_hours = wait.until(EC.presence_of_element_located((By.NAME, "no-of-hours[]")))
no_of_hours.send_keys("10")
assert no_of_hours.get_attribute("value") == "10", "Expected '10' in no-of-hours input."
print("✅ Test Passed: no_of_hours input ")

#################### Save button
try:
    save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addAuditTeam'])[1]")))

    if save_button.is_enabled():
        save_button.click()
        print("✅  save Button clicked successfully!")
    else:
        print("❌ save Button is not clickable!")
except Exception as e:
    print(f"❌ Error: {e}")
time.sleep(1)

#################### Save button label and ok
try:
    Save_notify_Label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Audit Team added successfully'])[1]")
    actual_text = Save_notify_Label.text.strip()

    assert actual_text == "Audit Team added successfully", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Remove_alert Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Remove_alert label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

time.sleep(1)
save_ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]")))
save_ok_button.click()
time.sleep(1)
print("✅ Test Passed: Save ok button Found ")

#################### IX. Line-Item Budget
nextSection = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='nextSectionBtn'])[1]")))
nextSection.click()

time.sleep(1)
driver.execute_script("document.body.style.zoom='80%'")
driver.execute_script("window.scrollBy(0, 1000);")

time.sleep(1)
SelectExpenseCategory = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='line-item-budget-trigger'])[1]")))
SelectExpenseCategory.click()

#################### IX. Line-Item Budget label
try:
    Line_Item_Budget_Label = wait.until(EC.visibility_of_element_located((By.XPATH, "(//h2[normalize-space()='Line-Item Budget'])[1]")))
    actual_text = Line_Item_Budget_Label.text.strip()

    assert actual_text == "Line-Item Budget", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Line-Item Budget Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Line-Item Budget label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")


try:
    Expense_Category_Label = driver.find_element(By.XPATH, "(//label[normalize-space()='Expense Category'])[1]")
    actual_text = Expense_Category_Label.text.strip()
    assert actual_text == "Expense Category", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Expense Category Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Expense Category label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    Line_Item_Label = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div/div/div[2]/form/div[2]/label")
    actual_text = Line_Item_Label.text.strip()

    assert actual_text == "Line Item", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Line Item Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Line Item label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    Details_Label = driver.find_element(By.XPATH, "(//label[normalize-space()='Details'])[1]")
    actual_text = Details_Label.text.strip()

    assert actual_text == "Details", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Details Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Details label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

try:
    Amount_Label = driver.find_element(By.XPATH, "(//label[normalize-space()='Amount'])[1]")
    actual_text = Amount_Label.text.strip()

    assert actual_text == "Amount", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: Amount Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: Amount label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")

################################ input
time.sleep(2)
SelectExpenseCategorySelection = wait.until(EC.element_to_be_clickable((By.XPATH, "(//option[normalize-space()='Representation Expense'])[1]")))
SelectExpenseCategorySelection.click()
selected_value = driver.find_element(By.XPATH, "(//option[normalize-space()='Representation Expense'])[1]").get_attribute("value")
assert selected_value == "3", f"Expected Select Expense Category value to be '3', got '{selected_value}'"

time.sleep(1)
lineItem = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='line-item'])[1]")))
lineItem.send_keys("Test line-item")
assert lineItem.get_attribute("value") == "Test line-item", "Expected 'Test line-item' in line-item textbox."
print("✅ Test Passed: lineItem  input ")

time.sleep(1)
details = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='details'])[1]")))
details.send_keys("Test details")
assert details.get_attribute("value") == "Test details", "Expected 'Test details' in details textbox."
print("✅ Test Passed: details  input ")

time.sleep(1)
calculator = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='calculator-popover'])[1]")))
calculator.click()

time.sleep(1)
calculator7 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='7'])[1]")))
calculator7.click()

time.sleep(1)
CalculatorPlus = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='+'])[1]")))
CalculatorPlus.click()

time.sleep(1)
Calculator5 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='5'])[1]")))
Calculator5.click()

time.sleep(1)
CalculatorEqual = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='='])[1]")))
CalculatorEqual.click()

time.sleep(1)
CopyResult = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Copy Result'])[1]")))
CopyResult.click()

amount_field = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='lib-amount'])[1]")))
amount_value = amount_field.get_attribute("value")
assert amount_value.strip() == "12", f" Expected '12' but got '{amount_value}'"

########################### save

time.sleep(1)
addLineItemBudgetsave_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='addLineItemBudget'])[1]")))
addLineItemBudgetsave_button.click()
time.sleep(1)
try:
    successfully_Label = driver.find_element(By.XPATH, "(//h2[normalize-space()='Line-Item Budget added successfully'])[1]")
    actual_text = successfully_Label.text.strip()
    assert actual_text == "Line-Item Budget added successfully", f"Incorrect spelling: Found '{actual_text}'"
    print("✅ Test Passed: successfully Label Found and Correctly Spelled")
except NoSuchElementException:
    print("❌ Test Failed: successfully label Not Found")
except AssertionError as e:
    print(f"❌ Test Failed: {e}")


time.sleep(1)
addLineItem_Budget_save_ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]")))
addLineItem_Budget_save_ok_button.click()

time.sleep(2)
driver.quit()
