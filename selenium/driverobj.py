import time
from selenium import webdriver

opx = webdriver.ChromeOptions()
opx.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opx)
driver.get("https://demowebshop.tricentis.com/")
# driver.get("https://demo.actitime.com/")

# demo.actitime.com

# driver.close()
##### Browser comments ####
# driver.maximize_window()
# time.sleep(4)
# driver.minimize_window()
# driver.fullscreen_window()
# print(driver.get_window_size())
# print(driver.get_window_position())
# print(driver.get_window_rect())
# driver.set_window_size(300,200)
# driver.set_window_position(500,100)
# driver.set_window_rect(200,100,400,500)

##Browser Navigation###

# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
# driver.close() # close current window
# driver.quit()  # close all the windows

####Locator#####

# driver.find_element(By.CLASS_NAME, "ico-register").click()
# driver.find_element("class name", "ico-register").click()

# driver.find_element("id", "small-searchterms").send_keys("hello")
# driver.find_element("name", "q").send_keys("hello")
# driver.find_element("link text", "Register").click()
# driver.find_element("partial link text", "Reg").click()
# driver.find_element("id", "small-searchterms").clear()

## CSS selector syntax = "HTML tag[attribute name = 'attribute value']"
# driver.find_element("css selector", "a[class = 'ico-register']").click()
# driver.find_element("css selector", "input[data-val-required = 'First name is required.']").send_keys("krishna")

###CSS Selector parent child syntax = "parent tag > child tag [attribute name = 'attribute value']"
# CSS Selector grand child syntax  =  "grandparent    child tag [attribute name = 'attribute value']"

# driver.find_element("css selector", "tr input[name = 'username']").send_keys("Krishna")
# driver.find_element("css selector", "td>input[name = 'pwd']").send_keys("password")


### Xpath is syntax or language for finding any element in the webpage. Used to navigate in DOM structure
#Xpath helps to find elements which are not found by anyother locators
#types
# absolute it starts with /html (if any changes made in path it will fail)
#relative it starts with // element can be search anywhere in the web pages

#//tagname[@attr_name = attr_value]
#//tagname[text() = value]
# using contains - mainly used to remove spaces in value
#//tagname[contains[@attr_name,attr_value]
#//tagname [contains(text(), value)]

# driver.find_element('xpath', '//input[@id="small-searchterms"]').send_keys("hello")
# driver.find_element('xpath', '//a[text() = "Register"]').click()

# using index
# driver.find_element('xpath', '(//input[@name = "Gender"])[2]').click()
# driver.find_element('xpath','//a[contains(text(), "Books")]').click()

#dep - indepen xpath

# 1. Need to identify dep and indepn element
# 2. write the xpath expression for independent element
# 3. traverseback until common parent of both dependent nd independent element is obtained (/..)
# 4. write the xpath expression for dependent element

#syntax "inde"tagname[@attr_nam = attr_value]/.."dep"//tagname[@@attr_nam = attr_value]

# from selenium import webdriver
# opx = webdriver.ChromeOptions()
# opx.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opx)
# driver.get("https://www.python.org/downloads/")
# driver.find_element('xpath', "//a[text()='Python 3.9.9']/../..//a[text()='Release Notes']").click()

# find elements method will give the list of web elements
# e = driver.find_elements('xpath', "//div[@class = 'footer-menu-wrapper']//a")
# for ele in e:
#     print(ele.text)  # .text gives the text of the element
#     print(ele.get_property("href")) # get property the attribute values of any element by passing the required attribute

# Select class - all the list box methods are implemented using select class

# import select class, pass the web element (list box) asa arguments
# three methods - visible text, index and value
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# opx = webdriver.ChromeOptions()
# opx.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opx)
# driver.get("file:///C:/Users/Krishna/Downloads/selenium_batch-master/selenium_batch-master/HTML_Files/demo.html")
#
# element = driver.find_element("id", "standard_cars")
# element = driver.find_element("id", "multiple_cars")
# sel_obj = Select(element)
#
# sel_obj.select_by_index(1)
# time.sleep(2)
# sel_obj.select_by_visible_text("Ford")
# time.sleep(2)
# sel_obj.select_by_value("for")
# time.sleep(2)

# checking if the list box is multi select or single select

# print(sel_obj.is_multiple)

# sel_obj.deselect_all()

# print(sel_obj.first_selected_option.text)
#  to get all the options
# al = sel_obj.options
# print all options in web element
# for i in al:
#     i.click()
# using range to select one by one
# for i in range(len(al)):
#     sel_obj.select_by_index(i)
#     time.sleep(1)

# for i in al:
#     sel_obj.select_by_visible_text(i.text)
#     time.sleep(1)


# for i in al:
#     sel_obj.select_by_value(i.get_property("value"))
#     time.sleep(1)


## syncronization: process of matching the application speed with that of selenium webdriver

# 2 types -
# conditional(implicit wait)  - driver.implicitly_wait(sec).if element found it won't wait for mentioned sec. time saving
# conditional(explicit wait) - condition not satisfy, time out specified. it execute using time module. time consuming

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# opx = webdriver.ChromeOptions()
# opx.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opx)
# driver.get("file:///C:/Users/Krishna/Downloads/selenium_batch-master/selenium_batch-master/HTML_Files/progress.html")

# driver.implicitly_wait(5)
# driver.find_element('xpath', '//button[text() = "Click Me"]').click()
# driver.find_element('xpath', '//div[text() = "100%"]')
# print("done")
# locat = ('xpath', '//div[text() = "100%"]')
# w = WebDriverWait(driver, 60)
# driver.find_element('xpath', '//button[text() = "Click Me"]').click()
# w.until(EC.presence_of_element_located(locat))
# driver.find_element('xpath', '//div[text() = "100%"]')

# print("done")


"""
to automate low level interaction like mouse movements, mouse buttons, press keys

import actionchains class
create an object for Actionchain class
"""
# import time
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)

# driver.get("https://www.myntra.com/")
# driver.maximize_window()

# from selenium.webdriver.common.action_chains import ActionChains
# act_obj = ActionChains(driver)
# # link = driver.find_element("xpath", '//div[@class="desktop-navLink"]//a[text()="Men"]')
# # act_obj.move_to_element(link).perform()
#
# profile = driver.find_element("xpath", '//span[text()="Profile"]')
# act_obj.move_to_element(profile).perform()
# time.sleep(2)

############################################################################################################
# double click and page down
# from selenium.webdriver.common.keys import Keys
# driver.get("file:///C:/Users/Lenovo/Desktop/website/demo.html")
# driver.maximize_window()
#
# button = driver.find_element("id", "double-click")
# act_obj.double_click(button).perform()
#
# act_obj.send_keys(Keys.PAGE_DOWN).perform()
#
# time.sleep(2)

################################################################################################
# drag and drop
driver.get("https://crossbrowsertesting.github.io/drag-and-drop.html")
driver.maximize_window()

draggable = driver.find_element("id", "draggable")
droppable = driver.find_element("id", "droppable")

act_obj.drag_and_drop(draggable, droppable).perform()
time.sleep(2)


#################################################################################################3
# file upload
# driver.get("file:///C:/Users/Krishna/Downloads/selenium_batch-master/selenium_batch-master/HTML_Files/demo.html")
# driver.maximize_window()
#
# path = r"C:\Users\Krishna\Desktop\Python course learning\Python notes_Part 1.txt"
# driver.find_element("xpath", '//input[@type="file"]').send_keys(path)
#
# time.sleep(10)
# driver.close()