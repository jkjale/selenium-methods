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
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
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

prices = driver.find_elements(By.XPATH, "//table[@class='cartTable']/tbody/tr/td[5]/p")
total = driver.find_element(By.XPATH, "//span[@class='totAmt']").text
for price in prices:
    print(type(price.text))
    print(isinstance(price.text, str))
    print(price.text)
assert int(total) == sum(int(price.text) for price in prices), 'Total value does not match the sum of all prices!!'
total_after_discount = driver.find_element(By.XPATH, "//span[@class='discountAmt']").text
assert float(total) > float(total_after_discount), 'Total value does not match the sum of all prices!!'

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = driver.find_elements(By.XPATH, "//table[@id='productCartTables']/tbody/tr/td[2]/p")
print(expectedList)
print([item.text for item in actualList])
assert expectedList == [item.text for item in actualList], "Item list does not match the expected list!!"


driver.quit()