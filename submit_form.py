from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://rahulshettyacademy.com/angularpractice/')

# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

driver.find_element(By.NAME, "name").send_keys("Jake Test")

driver.find_element(By.NAME, "email").send_keys("jake@test.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("mypassword123")

driver.find_element(By.ID, "exampleCheck1").click()

select_element = driver.find_element(By.ID, "exampleFormControlSelect1")
dropdown = Select(select_element)
dropdown.select_by_visible_text("Male")
# dropdown.select_by_index(1)

# when you need to loop through all options before selecting one
# for option in dropdown.options:
#     if option.text.strip().lower() == 'female':
#         option.click()
#         break

driver.find_element(By.ID, "inlineRadio2").click()

date_input = driver.find_element(By.NAME, "bday")
date_input.send_keys("09-30-2021")

driver.find_element(By.CSS_SELECTOR, "input[type='Submit']").click()

success_msg = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='container']/div[2]/div"))
).text
assert 'submitted successfully' in success_msg.lower(), 'Success message not found!!!'

driver.quit()