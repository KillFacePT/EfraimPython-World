import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento")
else:
    print("O site Pudim está acessivel no momento")