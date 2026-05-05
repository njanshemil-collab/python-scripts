from bs4 import BeautifulSoup
import pandas as pd
import requests as rq
fet=rq.get("https://books.toscrape.com")
fet.encoding="utf-8"
soup=BeautifulSoup(fet.text,"html.parser")
print(soup.title.text)
lis=soup.find_all("h3")
price=soup.find_all("p",class_="price_color")
for i,j in zip(lis,price):
    print(i.a["title"]," - ",j.text)
cleanlis=[]
for titl in lis:
    b=titl.a["title"]
    cleanlis.append(b)
cleanprice=[]
for rte in price:
    c=rte.text
    cleanprice.append(c)   
books={}
books["book_title"]=cleanlis
books["price"]=cleanprice
df=pd.DataFrame(books)
df.to_csv(r'C:\Users\Lenovo\OneDrive\Desktop\DODOW\books.csv')