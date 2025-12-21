from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

url = 'https://www.newegg.com/p/pl?d=sony+headphones'
html_text = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_='item-cell')

for product in products:
    name = product.find('a', class_='item-title').text
    features = product.find('ul', class_='item-features').text
    original_price = product.find('li', class_='price-was').text
    curr_price = product.find('li', class_='price-current').text
    print(f'Name: {name}\nFeatures: {features}\nOriginal Price: {original_price}\nCurrent Price: {curr_price}\n')