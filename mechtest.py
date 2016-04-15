import mechanize
import http.cookiejar
#test
from BeautifulSoup import BeautifulSoup

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

###### start going to vcu site #####
br.open('https://ssb.vcu.edu/proddad/bwcklibs.P_StoreTerm')

# print forms
#for f in br.forms():
#	print f 

br.select_form(nr=0)

# logon 
br.form['sid']='happersettjw'
br.form['PIN']='Happ876J'
br.submit()

# navigate to page
br.follow_link(text='Student')
br.follow_link(text='Registration')
br.follow_link(text='Look Up Classes')


# semester select
br.select_form(nr=1)

br.form['p_term'] = ['201630']
br.submit()
# subject select 

#br.form = list(br.forms())[1]
#br.select_form(nr=1)
#  get form name !!!
#br.form['sel_subj'] = ['FIRE']
#for form in br.forms():
#	print "form name:", form.name
#	print form
#print [form for form in br.forms()][1]
#count = 0 
#for i in br.form.controls:
#	count +=1
#	print count, i
#controls = br.form.controls
#controls[13].set_value('pleasework')
#br.form['pleasework'] = ['FIRE']
br.select_form(nr=1)
forms = [f for f in br.forms()]
forms[1].controls[13] = ['FIRE']
br.submit(id=)

#for link in br.links():
#	print link.text, link.url
#br.submit(nr=27)
#print br.response().read()
