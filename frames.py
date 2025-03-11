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
driver.implicitly_wait(2)
driver.maximize_window()

# open the url
driver.get('https://the-internet.herokuapp.com/iframe')

# Wait for the page to load completely
WebDriverWait(driver, 20).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()

print(driver.find_element(By.CSS_SELECTOR, "h3").text)




driver.quit()