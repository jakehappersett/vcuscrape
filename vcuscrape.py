import mechanize
import http.cookiejar
#test
from BeautifulSoup import BeautifulSoup
import splinter
###### set up mechanize browser #######
br = mechanize.Browser()
cj = http.cookiejar.LWPCookieJar()
br.set_cookiejar(cj)

# browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# TMNT
browser = splinter.Browser()
###### start going to vcu site #####
br.open('https://ssb.vcu.edu/proddad/bwcklibs.P_StoreTerm')

# print forms
#for f in br.forms():
#       print f 

br.select_form(nr=0)

# logon 
br.form['sid']='
br.form['PIN']='
br.submit()

# navigate to page
br.follow_link(text='Student')
br.follow_link(text='Registration')
br.follow_link(text='Add or Drop Classes')

# semester select
br.select_form(nr=1)

br.form['term_in'] = ['201630']
br.submit()

# input CRN for FIRE 311 class I want
#br.select_form(nr=1)

#br.form[nr=60] = ['32433']
#br.submit()i
#br.select_form(nr=1)
#nr = len(br.form.controls)-1
#print nr
forms = [f for f in br.forms()]
forms[1].set_value('32433', nr=100)
#response = br.submit(name='REG_BTN', label='Submit Changes')
first_found = browser.find_by_name('REG_BTN').first
first_found.click()
# extra stuff
def linkfinder():
	for link in br.links():
		print link.text, link.url
def formfinder():
	count = 0 
	for form in br.forms():
		count=+1
		print count, "form name:", form.name
		print form
#print br.response().read()


