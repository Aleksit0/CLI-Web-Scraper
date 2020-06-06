import requests
from csv import writer
from bs4 import BeautifulSoup

# uzimamo url stranice
response = requests.get('https://www.codedemo.net/')

# 2 parametra (urlvar.text, 'html.parser')
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.head.title)
