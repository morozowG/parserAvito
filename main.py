import requests as req
from bs4 import BeautifulSoup as bs


url = 'https://www.avito.ru/arhangelsk/bytovaya_elektronika'
page = req.get(url)

if page.status_code != 200:
    print("Не удалось подключится")

soup = bs(page.text, "html.parser")

products = soup.findAll("a", class_="snippet-link")
print(type(products.text))
#with open('produc.txt', "w") as w:
#    w.write((products)
#    w.close

