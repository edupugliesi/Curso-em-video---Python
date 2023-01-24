'''Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.'''

import urllib
import urllib.request
from Modulos114 import titulo

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    titulo.titulo('O site PUDIM não está disponível.')
else:
    titulo.titulo('Site PUDIM está disponível')
    print(site.read())