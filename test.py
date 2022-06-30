import requests
from bs4 import BeautifulSoup

url = 'https://priem.mirea.ru/accepted-entrants-list/'
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '/'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '/'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
        'Accept': '/'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
        'Accept': '/'
    },
    {
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
        'Accept': '/'
    },
]


response = requests.get(url, headers=heads)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.text)