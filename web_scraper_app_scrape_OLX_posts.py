import requests
from bs4 import BeautifulSoup

source_code = requests.get('https://www.olx.ro/electronice-si-electrocasnice/telefoane-mobile/')
soup = BeautifulSoup(source_code.content, 'lxml')
info = soup.find_all('div', class_='offer-wrapper')
d = {}
for i in info:
    anunt = i.find('div', class_='space rel')
    pret = i.find('p', class_='price')
    d[anunt.strong.text.strip()] = pret.strong.text.strip()
print(d)
for k,v in d.items():
    if 'IPhone' in k or 'IPHONE' in k or 'Iphone' in k:
        print(k, '--->', v)