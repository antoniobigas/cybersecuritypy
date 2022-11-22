import requests
from bs4 import BeautifulSoup

site=requests.get('https://www.climatempo.com.br/').content

#Baixar o html do site:
soup = BeautifulSoup(site, 'html.parser')

#html to string:
#print(soup.prettify())

#Procurar: span class="_block _margin-b-5 -gray"
tag_class = soup.find("span", class_="_block _margin-b-5 -gray")

print(tag_class)
#print(tag_class.string)

print(soup.title.string,'\n')

print(soup.a.string)
print(soup.p.string)

print(soup.find('admin'))
###################
#pip3 install bs4
#pip3 install requests
###################