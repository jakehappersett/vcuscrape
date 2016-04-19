from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import smtplib

def sendEmail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("", "") #"email","pass" (no @gmail)

        msg = "Quick! Fire 311 is open! The CRN is 32433!"
        server.sendmail("jake.happersett@gmail.com", "8042100901@msg.fi.google.com", msg)

# start selenium instance and navigate to login
driver = webdriver.Firefox()
driver.get('https://ssb.vcu.edu/proddad/twbkwbis.P_GenMenu?name=bmenu.P_MainMnu')

# login
eid = driver.find_element_by_name('sid')
pas = driver.find_element_by_name('PIN')
eid.send_keys('') #EID
pas.send_keys('') #PASS
pas.send_keys(Keys.RETURN)

# navigate to page 
driver.find_element_by_xpath("/html/body/div[@class='pagebodydiv']/table[@class='menuplaintable']/tbody/tr[3]/td[@class='mpdefault'][2]/a[@class='submenulinktext2 ']").click()
driver.find_element_by_partial_link_text('Regist').click()
driver.find_element_by_partial_link_text('Look').click()

# select Summer 2016
termList = Select(driver.find_element_by_id('term_input_id'))
termList.select_by_visible_text('Summer 2016')
driver.find_element_by_xpath("//input[@type='submit' and @value='Submit']").click()

# look up classes menu
subj = Select(driver.find_element_by_css_selector('select#subj_id'))
subj.select_by_value('FIRE')
driver.find_element_by_xpath("//input[@type='submit' and @value='Course Search']").click()

# fire 311 !!!ITS WORKING!!! 
driver.find_element_by_xpath("/html/body/div[@class='pagebodydiv']/table[@class='datadisplaytable'][2]/tbody/tr[4]/td[3]/form/input[30]").click()

# gets the attribute from the html, tests if it equals 40 (then class is still full)

isFull = driver.find_element_by_xpath("/html/body/div[@class='pagebodydiv']/form/table[@class='datadisplaytable']/tbody/tr[6]/td[@class='dddefault'][12]").text


if str(isFull) == "40":
	driver.close()
else :
	sendEmail()
	driver.close()	
