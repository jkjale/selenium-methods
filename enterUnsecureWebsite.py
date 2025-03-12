from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors') # able to bypass unsafe websites

driver_path = ChromeDriverManager().install()
service = Service(driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

# open the url
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Wait for the page to load completely
WebDriverWait(driver, 20).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')




sleep(2)

driver.quit()