from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver_path = ChromeDriverManager().install()
service = Service(driver_path)

driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

# Wait for the page to load completely
WebDriverWait(driver, 20).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)


# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names into browserSortedVeggies
browserSortedVeggies = []
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# sort veggieList and assign it to newSortedList
browserSortedVeggies.sort()

# check if originalBrowserSortedList == browserSortedVeggies
assert originalBrowserSortedList == browserSortedVeggies



sleep(2)

driver.quit()