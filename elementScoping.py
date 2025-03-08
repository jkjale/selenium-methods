from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

# Element scoping (chaining elements via xpath)
results = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='product']"))
)
for result in results:
    result.find_element(By.XPATH, "div[3]/button").click()

driver.find_element(By.CSS_SELECTOR, '.cart-icon').click()

proceed_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='cart-preview active']/div[2]/button"))
)
proceed_button.click()

promocode_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@class='promoCode']"))
)
promocode_field.send_keys("rahulshettyacademy")

driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

codeAppliedMsg = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@class='promoInfo']"))
)

assert 'applied' in codeAppliedMsg.text.lower(), 'Code applied confirmation message not found!!!!'


sleep(2)
driver.quit()