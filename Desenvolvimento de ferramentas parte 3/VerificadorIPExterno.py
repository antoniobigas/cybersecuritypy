import re
import json
from urllib.request import urlopen
###################
url='https://ipinfo.io/json'
resposta=urlopen(url)

dados=json.load(resposta)
print(dados)
###################
ip=dados['ip']
org=dados['org']
city=dados['city']
region=dados['region']
country=dados['country']

print('\n',ip,city)
###################