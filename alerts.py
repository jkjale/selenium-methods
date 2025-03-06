from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

name = "Jarvis"

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

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
# driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
driver.find_element(By.CSS_SELECTOR, "#confirmbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert name in alertText
# alert.accept()
alert.dismiss()


driver.quit()
