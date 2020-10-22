#código criado para salvar automaticamente no desktop (Windows)
import requests
import os

opl = requests.get('http://openlibrary.org/search.json?subject=python')

try:
    if opl.status_code == 200:
        print('Dados coletados')
except:
    "Erro ao capturar os dados."

with open('C:/Users/' + os.getlogin() + '/Desktop/openLib.json','x') as f:
    f.write(str(opl.json()))
f.close()
