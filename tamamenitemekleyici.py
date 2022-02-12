import requests
import re
from bs4 import BeautifulSoup

baslangic = input("link: ")
isim = input("isim: ")
dosyasi = input("dosya adi:")

#-klasik renk-#
html_page = requests.get(baslangic).text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
for i in range(30):
    oyle.write(f"{isim}|{images[23]}|{baslangic}|Renksiz\n")
#-burnt sienna-#
html_page = requests.get(baslangic+"/sienna").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Burnt Sienna\n")
#-safran-#
html_page = requests.get(baslangic+'/saffron').text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Saffron\n")
#-lime-#
html_page = requests.get(baslangic+"/lime").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Lime\n")
#-forest green-#
html_page = requests.get(baslangic+"/fgreen").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Forest Green\n")
#-orange-#
html_page = requests.get(baslangic+"/orange").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Orange\n")
#-purple-#
html_page = requests.get(baslangic+"/purple").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Purple\n")
#-tw-#
html_page = requests.get(baslangic+"/white").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Titanium White\n")
#-grey-#
html_page = requests.get(baslangic+"/grey").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Grey\n")
#-crimson-#
html_page = requests.get(baslangic+"/crimson").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Crimson\n")
#-sky blue-#
html_page = requests.get(baslangic+"/sblue").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Sky Blue\n")
#-kobalt-#
html_page = requests.get(baslangic+"/cobalt").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Cobalt\n")
#-pink-#
html_page = requests.get(baslangic+"/pink").text
soup = BeautifulSoup(html_page, features="html.parser")
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
oyle = open(dosyasi, "a+")
oyle.write(f"{isim}|{images[23]}|{baslangic}|Pink\n")