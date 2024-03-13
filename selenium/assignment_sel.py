# from selenium import webdriver
# opx = webdriver.ChromeOptions()
# opx.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opx)
# driver.get("https://www.python.org/downloads/")
# driver.find_element('xpath', "//a[text()='Python 3.9.9']/../..//a[text()='Release Notes']").click()

# driver.get("file:///C:/Users/Krishna/OneDrive/Desktop/demo.html")

# words = ['hello','hai', 'welcome', 'python', 'world', 'program', 'how', 'are', 'you']
# text_boxes = driver.find_elements('name' , 'fname')
#
# for txt,word in zip(text_boxes,words):
#    txt.send_keys(word)


# chk = driver.find_elements('xpath', "//input[@type = 'checkbox']")
#
# for ch in chk:
#     ch.click()


import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
opx = webdriver.ChromeOptions()
opx.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opx)
driver.implicitly_wait(20)
driver.get("https://demowebshop.tricentis.com/")
driver.find_element("link text", "Facebook").click()
handles = driver.window_handles
driver.switch_to.window(handles[1])
driver.find_element("xpath", "(//input[@name = 'email'])[2]").send_keys("abc@gmail.com")
time.sleep(2)
driver.find_element('xpath', '//div[@class="x1i10hfl x6umtig x1b1mbwd xaqea5y xav7gou x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8 x1hl2dhg xggy1nq x87ps6o x1lku1pv x1a2a7pz x6s0dn4 x14yjl9h xudhj91 x18nykt9 xww2gxu x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x78zum5 xl56j7k xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 xc9qbxq x14qfxbe x1qhmfi1"]').click()
driver.switch_to.window(handles[0])
driver.find_element("link text", "Register").click()
time.sleep(2)
driver.quit()

