import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
opx = webdriver.ChromeOptions()
opx.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opx)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element('xpath', '//input[@type = "search"]').send_keys("ca")
li = driver.find_elements('xpath', '//div[@class = "product"]')

# //div[@class = "product"]/h4[@class = 'product-name']
l1 = []
for i in li:
    l1.append(i.find_element('xpath', "h4[@class = 'product-name']").text)
    i.find_element('xpath', "div/button").click()
print(l1)
driver.find_element('css selector', 'img[alt = "Cart"]').click()
driver.find_element('xpath', '//button[text()="PROCEED TO CHECKOUT"]').click()
driver.find_element('xpath', "//input[@class = 'promoCode']").send_keys("rahulshettyacademy")
driver.find_element('xpath', "//button[@class = 'promoBtn']").click()
a = driver.find_elements('xpath', "//tr/td[5]/p[@class = 'amount']")
sum_1 = 0
for i in a:
    sum_1 = sum_1 + int(i.text)
print(sum_1)
num = int(driver.find_element('xpath', "//span[@class = 'totAmt']").text)
print(num)
assert sum_1 == num
driver.find_element('xpath', '//button[text() = "Place Order"]').click()
action = ActionChains(driver)
action.send_keys(Keys.ARROW_DOWN).perform()
driver.find_element('xpath', '//option [text() = "India"]').click()
driver.find_element('xpath', '//input [@class = "chkAgree"]').click()
driver.find_element('xpath', '//button[text() = "Proceed"]').click()
