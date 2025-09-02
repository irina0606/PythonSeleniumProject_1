import webdriver_manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()

driver.get("https://www.rcvacademy.com/")
driver.maximize_window()
print(driver.title)
driver.close()