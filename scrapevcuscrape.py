import requests
from BeautifulSoup import BeautifulSoup
url = 'https://ssb.vcu.edu/proddad/twbkwbis.P_GenMenu?name=bmenu.P_RegMnu'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

nput = soup.findAll('input')


print nput
