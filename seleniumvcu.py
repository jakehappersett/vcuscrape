from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# start selenium instance and navigate to login
driver = webdriver.Firefox()
driver.get('https://ssb.vcu.edu/proddad/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu')


# login
eid = driver.find_element_by_name('sid')
pas = driver.find_element_by_name('PIN')
eid.send_keys('')
pas.send_keys('')
pas.send_keys(Keys.RETURN)

# navigate to page 
driver.find_element_by_partial_link_text('Stu').click()
driver.find_element_by_partial_link_text('Regist').click()
driver.find_element_by_partial_link_text('Add').click()
# select Summer 2016
termList = Select(driver.find_element_by_id('term_id'))
termList.select_by_visible_text('Summer 2016')

#if then for class selection
#assert "No results found." not in driver.page_source

