import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("http://10.10.99.18:8005/application/A3001Vyscf4xXGKeyZMINB8PgkYQMs7eYjCF9hGFRZEPgiJea5tNBvxeKXOV/form001p1.1")

# Initialize WebDriverWait
wait = WebDriverWait(driver, 20)
driver.maximize_window()

try:
    ################### p 1️⃣.1️⃣ ###############
    contact_number_field = wait.until(EC.presence_of_element_located((By.ID, "contact_number")))
    contact_number_field.send_keys("09123456789")

    postal_address_field = wait.until(EC.presence_of_element_located((By.ID, "postal_address")))
    postal_address_field.send_keys("123 Kalinga St., Tabuk City, Kalinga")

    country_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ss-main')]")))
    driver.execute_script("arguments[0].click();", country_box)
    time.sleep(1)

    dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ss-content")))
    driver.execute_script("arguments[0].click();", dropdown)
    time.sleep(1)

    try:
        philippines_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ss-option') and text()='Philippines']")))
        driver.execute_script("arguments[0].click();", philippines_option)
    except Exception as e:
        print("", e)
    try:
        selected_value = driver.execute_script("return document.querySelector('.ss-main .ss-single').textContent;")
    except Exception as e:
        print("", e)

    state_city_field = wait.until(EC.presence_of_element_located((By.ID, "state_city")))

    state_city_field.send_keys("Tabuk City")

    ph_visa_validity_field = wait.until(EC.presence_of_element_located((By.ID, "ph_visa_validity")))
    ph_visa_validity_field.send_keys("12/31/2025")

    dob_field = wait.until(EC.presence_of_element_located((By.ID, "date_of_birth")))
    dob_field.send_keys("01/01/1995")

    contact_person_name = wait.until(EC.presence_of_element_located((By.ID, "contact_person_name")))
    contact_person_name.send_keys("Juan Dela Cruz")

    contact_person_address = wait.until(EC.presence_of_element_located((By.ID, "contact_person_address")))
    contact_person_address.send_keys("456 Rizal St., Tabuk City, Kalinga")

    contact_person_email = wait.until(EC.presence_of_element_located((By.ID, "contact_person_email_address")))
    contact_person_email.send_keys("juan.delacruz@example.com")

    contact_person_contact_no = wait.until(EC.presence_of_element_located((By.ID, "contact_person_contact_no")))
    contact_person_contact_no.send_keys("09123456789")

    upload_photo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    photo_path = r"C:\Users\KalingaInnovationHub\Desktop\screenshot\Screenshot 2025-03-24 140600.png"
    upload_photo.send_keys(photo_path)

    ######################### CLICK NEXT BUTTON 1
    next_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/form/div/div[2]/div/button[2]")
    ))
    next_button.click()
    time.sleep(3)
################### p 1️⃣.2️⃣ ###############

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ss-main'))
    ).click()

    humanities_option = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Humanities']"))
    )
    driver.execute_script("arguments[0].click();", humanities_option)

    aeronautical_option = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Aeronautical Engineering']"))
    )
    driver.execute_script("arguments[0].click();", aeronautical_option)


    level_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "temp_education_level"))
    )
    driver.execute_script("arguments[0].click();", level_dropdown)
    time.sleep(1)

    driver.execute_script("""
            let selectElement = arguments[0];
            selectElement.value = '1';
            selectElement.dispatchEvent(new Event('change', { bubbles: true }));
        """, level_dropdown)

    school_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.NAME, "temp_education_school"))
    )
    school_input.send_keys("Kalinga State University")

    placeholder = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//tr[@id='education-row-1']//div[@aria-label='Combobox']"))
    )
    driver.execute_script("arguments[0].click();", placeholder)

    option_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//div[@class='ss-content auto-width ss-open-below']//div[@role='option'][normalize-space()='Philippines']"))
    )
    driver.execute_script("arguments[0].click();", option_element)

    placeholder = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Course')]"))
    )
    driver.execute_script("arguments[0].click();", placeholder)

    option_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Doctor of Dental Medicine']"))
    )
    driver.execute_script("arguments[0].click();", option_element)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "temp_education_year_graduated"))
    ).send_keys("2001")

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//tr[@id='education-row-1']//i[contains(@class, 'save-icon')]"))
    ).click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "temp_work_company"))
    ).send_keys("PSTO-KALINGA")

    placeholder = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//tr[@id='work-row-1']//div[@class='ss-placeholder'][normalize-space()='Country']"))
    )
    driver.execute_script("arguments[0].click();", placeholder)

    option_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//div[@class='ss-content auto-width ss-open-below']//div[@role='option'][normalize-space()='Philippines']"))
    )
    driver.execute_script("arguments[0].click();", option_element)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "temp_work_position"))
    ).send_keys("Intern")

####################################
    year_From = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='From'])[1]")))
    year_From.click()

    year_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[@class='datepicker-cell hover:bg-gray-100 dark:hover:bg-gray-600 block flex-1 leading-9 border-0 rounded-lg cursor-pointer text-center text-gray-900 dark:text-white font-semibold text-sm year'][normalize-space()='2023'])[1]")
    ))
    driver.execute_script("arguments[0].click();", year_button)


    year_present = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='Present'])[1]")))
    year_present.click()

    from_time = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='datepicker-cell hover:bg-gray-100 dark:hover:bg-gray-600 block flex-1 leading-9 border-0 rounded-lg cursor-pointer text-center text-gray-900 dark:text-white font-semibold text-sm year focused'][normalize-space()='2025'])[2]")))
    from_time.click()

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "(//i[@class='save-icon tippy icon-[mdi--check-circle-outline] text-xl text-center text-green-500 cursor-pointer px-2'])[2]"))
    ).click()

    #time.sleep(2)


    next1_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/form/div/div[2]/div/div/button[3]")
    ))
    driver.execute_script("arguments[0].click();", next1_button)

    ################### p2️⃣ ###############
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@id='add_host_institution'])[1]")))
    driver.execute_script("arguments[0].click();", add_button)

    time.sleep(1)

    institution_name = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='full_name_of_institution'])[1]")))
    institution_name.send_keys("Department of Science and technology 53")

    institution_acronym = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='acronym'])[1]")))
    institution_acronym.send_keys("DOST")

    type_of_institution = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//select[@id='type_of_institution'])[1]"))
    )
    driver.execute_script("arguments[0].click();", type_of_institution)
    time.sleep(1)  # Adjust as needed

    driver.execute_script("""
                let selectElement = arguments[0];
                selectElement.value = '1';
                selectElement.dispatchEvent(new Event('change', { bubbles: true }));
            """, type_of_institution)

    institution_postal_address = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='postal_address'])[1]")))
    institution_postal_address.send_keys(" Tabuk City Kalinga Philippines , 3800")

    # Select Institution Region
    institution_region = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//select[@id='region'])[1]"))
    )
    driver.execute_script("arguments[0].click();", institution_region)
    time.sleep(1)

    driver.execute_script("""
        let selectElement = arguments[0];
        selectElement.value = '2';  // 
        selectElement.dispatchEvent(new Event('input', { bubbles: true }));
        selectElement.dispatchEvent(new Event('change', { bubbles: true }));
    """, institution_region)
    from selenium.webdriver.common.keys import Keys
    institution_region.send_keys(Keys.ENTER)

    time.sleep(1)

    institution_province = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//select[@id='province'])[1]"))
    )
    driver.execute_script("arguments[0].click();", institution_province)
    time.sleep(1)

    driver.execute_script("""
        let selectElement = arguments[0];
        selectElement.value = '21';
        selectElement.dispatchEvent(new Event('input', { bubbles: true }));
        selectElement.dispatchEvent(new Event('change', { bubbles: true }));
    """, institution_province)

    institution_province.send_keys(Keys.ENTER)

    institution_contact_numbers = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='contact_numbers'])[1]")))
    institution_contact_numbers.send_keys("09123456789")

    institution_email_addresses = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='email_addresses'])[1]")))
    institution_email_addresses.send_keys("test@gmail.com")

    institution_contact_person_name = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='contact_person_name'])[1]")))
    institution_contact_person_name.send_keys("test , test .")

    institution_designation = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='designation'])[1]")))
    institution_designation.send_keys("Intern")

    time.sleep(2)

    save_button = wait.until(EC.element_to_be_clickable((By.ID, "save")))
    driver.execute_script("arguments[0].click();", save_button)

    time.sleep(1)

    ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]")))
    driver.execute_script("arguments[0].click();", ok_button)

    time.sleep(1)

################### p2️⃣ incomplete ###############

    incomplete_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//i[@class='edit-tor-icon icon-[fa6-solid--pen-to-square] cursor-pointer'])[1]")))
    driver.execute_script("arguments[0].click();", incomplete_button)

    reference_part1 = wait.until(EC.presence_of_element_located((By.NAME, "part1")))
    driver.execute_script("arguments[0].scrollIntoView(true);", reference_part1)
    time.sleep(1)
    reference_part1.send_keys(" 1Test 1test 1test 1test 1test 1test 1test")

    reference_part2 = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='part2'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", reference_part2)
    time.sleep(1)
    reference_part2.send_keys(" 2Test 2test 2test 2test 2test 2test 2test")

    reference_part3 = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@id='part3'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", reference_part3)
    time.sleep(1)
    reference_part3.send_keys(" 3Test 3test 3test 3test 3test 3test 3test")

    time.sleep(1)
    elem_from2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='continuous_start'])[1]")))
    elem_from2.click()

    from_time = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='April 7, 2025'][normalize-space()='7'])[3]")))
    from_time.click()

    elem_from2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='continuous_end'])[1]")))
    elem_from2.click()

    from_time = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@aria-label='October 24, 2025'])[1]")))
    from_time.click()

    part5_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='part5_add'])[1]")))
    driver.execute_script("arguments[0].click();", part5_add_button)

    part5_activity = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//select[@id='activity'])[1]"))
    )
    driver.execute_script("arguments[0].click();", part5_activity)
    time.sleep(1)

    # Set the province value and trigger events
    driver.execute_script("""
                       let selectElement = arguments[0];
                       selectElement.value = '8';
                       selectElement.dispatchEvent(new Event('input', { bubbles: true }));
                       selectElement.dispatchEvent(new Event('change', { bubbles: true }));
                   """, part5_activity)


    activity_start = wait.until(EC.presence_of_element_located((By.XPATH, "(//input[@id='activity_start'])[1]")))
    activity_start.send_keys("April 10, 2025")
    activity_start.send_keys(Keys.ENTER)

    time.sleep(1)


    activity_end = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='activity_end'])[1]")))
    activity_end.send_keys("April 10, 2025")
    activity_end.send_keys(Keys.ENTER)

    activity_deliverable = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//textarea[@id='activity_deliverable'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", activity_deliverable)
    time.sleep(1)
    activity_deliverable.send_keys(" activity Test activity test activity test 2test 2test 2test 2test")

    activity_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='part5_save'])[1]")))
    driver.execute_script("arguments[0].click();", activity_save_button)

    time.sleep(2)

    activity_ok_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']")))
    driver.execute_script("arguments[0].click();", activity_ok_save_button)

    time.sleep(2)

    part6_seminar_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon-[mdi--check-bold] text-gray-200 text-xs'])[6]")))
    driver.execute_script("arguments[0].click();", part6_seminar_button)

    part6_1_add = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@id='part6_1_add'])[1]")))
    driver.execute_script("arguments[0].click();", part6_1_add)

    seminar_title = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='seminar_title'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", seminar_title)
    time.sleep(1)
    seminar_title.send_keys(" Seminar activity Test activity test activity test 2test 2test 2test 2test")

    seminar_duration = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='seminar_specific'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", seminar_duration)
    time.sleep(1)
    seminar_duration.send_keys(" Duration Seminar activity Test activity test activity test 2test 2test 2test 2test")

    seminar_audience = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='seminar_specific2'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", seminar_audience)
    time.sleep(1)
    seminar_audience.send_keys(" Audience Seminar activity Test activity test activity test 2test 2test 2test 2test")

    seminar_output = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//textarea[@id='seminar_output'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", seminar_output)
    time.sleep(1)
    seminar_output.send_keys(" Output Seminar activity Test activity test activity test 2test 2test 2test 2test")

    seminar_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='part6_1_save'])[1]")))
    driver.execute_script("arguments[0].click();", seminar_save_button)

    time.sleep(2)

    seminar_ok_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']")))
    driver.execute_script("arguments[0].click();", seminar_ok_save_button)

    part7_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='part7_add'])[1]")))
    driver.execute_script("arguments[0].click();", part7_add_button)

    support_activities = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='support_activities'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", support_activities)
    time.sleep(1)
    support_activities.send_keys(
        " support_activities activity Test activity test activity test 2test 2test 2test 2test")

    support_nature = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//input[@id='support_nature'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", support_nature)
    time.sleep(1)
    support_nature.send_keys(" support_nature activity Test activity test activity test 2test 2test 2test 2test")

    support_details = wait.until(
        EC.presence_of_element_located((By.XPATH, "(//textarea[@id='support_details'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", support_details)
    time.sleep(1)
    support_details.send_keys(" support_details activity Test activity test activity test 2test 2test 2test 2test")

    part7_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@id='part7_save'])[1]")))
    driver.execute_script("arguments[0].click();", part7_save_button)

    support_ok_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='OK']")))
    driver.execute_script("arguments[0].click();", support_ok_save_button)

    time.sleep(2)

    reference_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='tor_close']")))
    driver.execute_script("arguments[0].click();", reference_close_button)

    time.sleep(2)

    next2_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[1]/div[4]/button[3]")
    ))
    next2_button.click()

    time.sleep(1)


################## p3️⃣ ##################

    support_part3 = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@name='temp_support_needed'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", support_part3)
    support_part3.send_keys(" 1Test 1test 1test 1test 1test 1test 1test")
    time.sleep(1)

    details_part3 = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[@name='temp_details'])[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", details_part3)
    details_part3.send_keys(" detailsTest details test detailstest 1test 1test 1test 1test")
    time.sleep(1)

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//i[@class='save-icon tippy icon-[mdi--check-circle-outline] text-xl text-center text-green-500 cursor-pointer px-2'])[1]"))
    ).click()
    time.sleep(2)

    next3_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[3]/button[3]")
    ))
    next3_button.click()

    time.sleep(1)



################## p4️⃣ ##################
    Check0_button_part5 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon-[mdi--check-bold] text-gray-200 text-xs'])[1]")))
    driver.execute_script("arguments[0].click();", Check0_button_part5)

    Check1_button_part5 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon-[mdi--check-bold] text-gray-200 text-xs'])[2]")))
    driver.execute_script("arguments[0].click();", Check1_button_part5)

    Check2_button_part5 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon-[mdi--check-bold] text-gray-200 text-xs'])[3]")))
    driver.execute_script("arguments[0].click();", Check2_button_part5)

    Check3_button_part5 = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//i[@class='icon-[mdi--check-bold] text-gray-200 text-xs'])[4]")))
    driver.execute_script("arguments[0].click();", Check3_button_part5)


    time.sleep(2)

    next3_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div/div[3]/button[3]")
    ))
    next3_button.click()

    time.sleep(1)

    p4_ok_save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='OK'])[1]")))
    driver.execute_script("arguments[0].click();", p4_ok_save_button)

    time.sleep(2)

 ################## p5️⃣ ##################
    Accomplished_pdf = wait.until(EC.presence_of_element_located((By.ID, "bsp_forms")))
    accomplished_path = r"C:\Users\KalingaInnovationHub\Downloads\Accomplished.pdf"
    Accomplished_pdf.send_keys(accomplished_path)
    time.sleep(1)

    endorsement_letter_pdf = wait.until(EC.presence_of_element_located((By.ID, "endorsement_letter")))
    endorsement_letter_path = r"C:\Users\KalingaInnovationHub\Downloads\Endorsement letter.pdf"
    endorsement_letter_pdf.send_keys(endorsement_letter_path)
    time.sleep(1)

    medical_certificate_pdf = wait.until(EC.presence_of_element_located((By.ID, "medical_certificate")))
    medical_certificate_path = r"C:\Users\KalingaInnovationHub\Downloads\Medical Certificate.pdf"
    medical_certificate_pdf.send_keys(medical_certificate_path)
    time.sleep(1)

    passport_pdf = wait.until(EC.presence_of_element_located((By.ID, "passport")))
    passport_path = r"C:\Users\KalingaInnovationHub\Downloads\copy of passport.pdf"
    passport_pdf.send_keys(passport_path)
    time.sleep(1)

    diploma_pdf = wait.until(EC.presence_of_element_located((By.ID, "diploma")))
    diploma_path = r"C:\Users\KalingaInnovationHub\Downloads\copy of diploma.pdf"
    diploma_pdf.send_keys(diploma_path)
    time.sleep(1)

    curriculum_vitae_pdf = wait.until(EC.presence_of_element_located((By.ID, "curriculum_vitae")))
    curriculum_vitae_path = r"C:\Users\KalingaInnovationHub\Downloads\Curriculum Vitae.pdf"
    curriculum_vitae_pdf.send_keys(curriculum_vitae_path)
    time.sleep(1)

    next_button_6 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Submit'])[1]")))
    driver.execute_script("arguments[0].click();", next_button_6)
    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # ✅ Close the browser after a delay
    time.sleep(5)  # Reduce sleep time to 5 seconds
    driver.quit()
