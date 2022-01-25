import requests
from bs4 import BeautifulSoup

# with open('index.html', 'rb') as hf:
#     soup = BeautifulSoup(hf, 'html.parser')

# print(soup.prettify())
# print(soup.head.title.text)
# print(soup.li.a.h2.text)
# print(soup.li.a.p.text)
source_code = requests.get('https://mariusciurea.github.io/links/')
soup = BeautifulSoup(source_code.content, 'lxml')

apps = soup.find_all('a', {'title':'Ajuta un elev sa aleaga informat facultatea'})
for app in apps:
    print(app)
