from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

description = "A Data Science Specialist focuses on applying statistical and computational techniques to analyze and interpret complex data. This role is central to providing actionable insights that drive strategic decision-making in businesses and organizations."
concern_bsp = "DOST-CO"

desc_input = driver.find_element(By.ID, "description")
desc_input.send_keys(f"{description}")

concern_bsp_dropdown = driver.find_element(By.ID, "region_dropdown")
concern_bsp_dropdown_select = Select(concern_bsp_dropdown)
concern_bsp_dropdown_select.select_by_visible_text(f"f'{concern_bsp}'")

active_checkbox = driver.find_element(By.ID, "checkbox")
if not active_checkbox.is_slected():
    active_checkbox.click()
    print("Active checkbox is selected")