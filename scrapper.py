import requests
from bs4 import BeautifulSoup

url = "http://ingsoftware.reduaz.mx/moodle/"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

links2 = soup.find_all("a")


text_file = open("scraper.html", "w")

for link in links:
	
	text_file.write("<a href='%s'>%s</a>" %(link.get("href"), link.text))
	
	#print("<a href='%s'>%s</a>" %(link.get("href"), link.text))



text_file.close()

treetest = "treetest.html"

for link in links2:
    	
	
