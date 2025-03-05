from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

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

select_options = driver.find_element(By.ID, "dropdown-class-example")
dropdown = Select(select_options)
# dropdown.select_by_value("option3")
# dropdown.select_by_visible_text("Option3")
dropdown.select_by_index(3)

# when you need to loop through all options before selecting one
# for option in dropdown.options:
#     if option.text.strip().lower() == 'Option3':
#         option.click()
#         break



driver.quit()