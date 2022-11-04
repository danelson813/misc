import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

url = "https://thegreatestbooks.org/lists/169"
r = requests.get(url)
soup = bs(r.text, 'html.parser')

books = soup.find_all('li', class_='item')
results = []
for book in books[:]:
    title = book.find("h4").find("a").text
    link = "https://thegreatestbooks.org" + book.find('h4').find('a')['href']
    author = book.find("h4").find_all("a")[1].text
    result = {
        'title': title, 
        'author': author, 
        'link': link}
    results.append(result)

df = pd.DataFrame(results)
df.to_csv("results.csv", index=False)
