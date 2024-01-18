# open browswe(chrome, firefox, edge)
# open URL (https://opensource-demo.orangehrmlive.com/)
# Enter Username(Admin)
# Enter Password(admin123)
# Click on login
# capture title of the homepage(Actual Title)
# Verify title of the page(OrangeHRM)
# close browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
service=Service()
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
#

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME , "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

act_title= driver.title
exp_title= "OrangeHRM"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()