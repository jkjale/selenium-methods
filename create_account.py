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
driver.get('https://rahulshettyacademy.com/client')

# Wait for the page to load completely
WebDriverWait(driver, 10).until(
    lambda driver: driver.execute_script('return document.readyState') == 'complete'
)

f_name = 'Jarvis'
l_name = 'Persona'
email_address = 'jarvis@test.com'
phone_num = '8881234567'
password = 'Password1.'

driver.find_element(By.XPATH, "//div[@class='login-section-wrapper']/div[2]/p/a").click()

firstname_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "firstName"))
)
firstname_input.send_keys(f_name)

driver.find_element(By.ID, "lastName").send_keys(l_name)

driver.find_element(By.ID, "userEmail").send_keys(email_address)

driver.find_element(By.ID, "userMobile").send_keys(phone_num)

select_occupation = driver.find_element(By.XPATH, "//select[@formcontrolname='occupation']")
occupation_dropdown = Select(select_occupation)
occupation_dropdown.select_by_visible_text("Engineer")

driver.find_element(By.XPATH, "//input[@type='radio' and @value='Male']").click()

driver.find_element(By.ID, "userPassword").send_keys(password)

driver.find_element(By.ID, "confirmPassword").send_keys(password)

driver.find_element(By.XPATH, "//input[@type='checkbox' and @formcontrolname='required']").click()

driver.find_element(By.XPATH, "//input[@type='submit' and @value='Register']").click()

success_msg = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h1[@class='headcolor']"))
).text
assert 'success' in success_msg.strip().lower(), 'Success message not showing!!'

driver.quit()