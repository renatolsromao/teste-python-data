import requests
import json
import os

opl = requests.get('http://openlibrary.org/search.json?subject=python')

try:
    if opl.status_code == 200:
        print('Dados coletados')
except:
    "Erro ao capturar os dados."

with open('C:/Users/' + os.getlogin() + '/Desktop/openLib.json','x') as f:
    json.dump(opl.json(),f)
f.close()
