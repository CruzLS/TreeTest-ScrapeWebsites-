import requests
from bs4 import BeautifulSoup

#url = "http://ingsoftware.reduaz.mx/moodle/"
url = input("Ingresa el link del website para comenzar la prueba: ")

r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

listaURLS = list()



#Variables string para definir el css de la pagina
stylevar = "stylesheet"
stylehref = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
#stylehref = "css/main.css"
withtable = "width:100%"


requestSubs = list()

#Se crea y se escribe dentro de un archivo html
text_file = open("scraper.html", "w")

#text_file.write escribe el contenido dentr del html
text_file.write("<!DOCTYPE html> <html> <head> <meta charset='utf-8'>>  <h1>Tree Test del sitio: "+url+
"</h1><link rel="+stylevar+"  href="+stylehref+"> <title>Web scrapping de: "+url+"</title> </head> <body> <table class='table table-striped table-hover table-bordered'> <thead class='thead-dark'> <tr> <th>Links principales y sub-links de la pagina</th>  </tr> </thead>")

for link in links:
	
	#text_file.write("<tr> <td><a href='%s'>%s</a> </td> </tr>" %(link.get("href"), link.text) )
	listaURLS.append(link.get("href"))
	if "http" in link:
		listaURLS.append(link)
		
for urls in listaURLS:
		#print(urls)
		if "http" in urls:
			response = requests.get(urls)
			bsoup = BeautifulSoup(response.content)
			sublinks = bsoup.find_all("a")

			for subs in sublinks:
    				text_file.write("<tr> <td><h3>Link: "+urls+" </h3><h3>Sub-link: </h3><a href='%s'>%s</a> </td> </tr>" %(subs.get("href"), subs.text) )
    	

    	

text_file.write("</table> </body>\</html>")

text_file.close()

treetest = "treetest.html"
