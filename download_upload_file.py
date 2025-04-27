from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://rahulshettyacademy.com/upload-download-test/index.html')

driver.find_element(By.ID, "downloadButton").click()

file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_path = '/Users/jakelee/Downloads/download (3).xlsx'
file_input.send_keys(file_path)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)


driver.quit()










