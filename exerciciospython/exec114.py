import requests
try:
    p = requests.get('https://www.pudim.com.br/')
except:
    print('O site Pudim não está acessivel no momento!')
else:
    print('O site Pudim está acessivel no momento!')