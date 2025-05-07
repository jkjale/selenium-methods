from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, timeout=10)

driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element(By.CSS_SELECTOR, "[href='/angularpractice/shop']").click()

checkout_btn = driver.find_element(By.CSS_SELECTOR, "#navbarResponsive a")
checkout_btn_counter = checkout_btn.text

cards = driver.find_elements(By.CSS_SELECTOR, ".card.h-100")

for card in cards:
    if card.find_element(By.CSS_SELECTOR, "h4 a").text.strip().lower() == 'iphone x':
        card.find_element(By.CSS_SELECTOR, "button").click()

checkout_btn_counter_updated = checkout_btn.text

assert checkout_btn_counter != checkout_btn_counter_updated, "Checkout button counter has not been updated"

checkout_btn.click()

driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()

country = 'united states of america'
country_input = driver.find_element(By.ID, "country")
country_input.send_keys(country)

country_dropdown_selection = (By.XPATH, "//a[text()='United States of America']")

country_select = driver.wait.until(
    EC.element_to_be_clickable(country_dropdown_selection),
    message=f'Element not clickable by {country_dropdown_selection}'
)

country_select.click()

driver.find_element(By.CSS_SELECTOR, "[for='checkbox2']").click()

driver.find_element(By.CSS_SELECTOR, "[value='Purchase']").click()

success_msg = driver.wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success > strong")),
)

assert 'success!' in success_msg.text.strip().lower()

driver.quit()








