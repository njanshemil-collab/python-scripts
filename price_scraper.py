from bs4 import BeautifulSoup
import requests as rq
fet=rq.get("https://books.toscrape.com")
soup=BeautifulSoup(fet.text,"html.parser")
print(soup.title.text)
lis=soup.find_all("h3")
price=soup.find_all("p",class_="price_color")
for i,j in zip(lis,price):
    print(i.a["title"],j.text)