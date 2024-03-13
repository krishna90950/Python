import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
opx = webdriver.ChromeOptions()
opx.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opx)
driver.get("https://demowebshop.tricentis.com/")
driver.find_element("css selector", "a[class = 'ico-register']").click()
driver.find_element("css selector",'input[id = "gender-male"]').click()
driver.find_element("css selector", "input[data-val-required = 'First name is required.']").send_keys("krishna")
driver.find_element("id", "LastName").send_keys("prasad")
driver.find_element("id", "Email").send_keys("abc90950@gmail.com")
driver.find_element("id", "Password").send_keys("Abcde@123")
driver.find_element("id", "ConfirmPassword").send_keys("Abcde@123")
driver.find_element("id", "register-button").click()


