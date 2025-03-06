from selenium import webdriver
from selenium.webdriver import Keys
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
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Wait for the page to load completely
WebDriverWait(driver, 20).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)


radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(radio_buttons))
radio_buttons[0].click()
assert radio_buttons[0].is_selected()

# for radio_button in radio_buttons:
#     if radio_button.get_attribute("value") == 'radio1':
#         radio_button.click()
#         assert radio_button.is_selected()
#         break


sleep(2)

driver.quit()