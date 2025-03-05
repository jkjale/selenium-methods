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
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

# Wait for the page to load completely
WebDriverWait(driver, 20).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

driver.find_element(By.ID, "autosuggest").send_keys("ind")

sleep(2)

countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
country_selection = 'Indonesia'

for country in countries:
    if country.text == country_selection:
        country.click()
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == country_selection



driver.quit()