import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URlError:
    print('O site Pudim não está acessível no momento')
else:
    print('O site Pudim está acessível no momento')
    print(site.read())
