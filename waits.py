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

driver.implicitly_wait(5)

# open the url
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

# Wait for the page to load completely
WebDriverWait(driver, 20).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)


driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

productList = WebDriverWait(driver, 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='product']"))
)

if productList:
    assert len(productList) == 3, 'There are less than 3 products shown!!'
else:
    raise Exception('No products shown')


driver.quit()
