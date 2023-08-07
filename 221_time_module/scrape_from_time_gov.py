import requests
from bs4 import BeautifulSoup

url = "https://time.gov/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

r = requests.get(url=url, headers=headers)
# print(r)

soup = BeautifulSoup(r.content, 'html.parser')
# print(soup)

time_text_element = soup.findAll('div', class_='time-text')
print(time_text_element)
