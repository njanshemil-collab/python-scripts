import pandas as pd
from bs4 import BeautifulSoup
import requests as rq
cleanlis=[]
cleanprice=[]
for n in range (1,51):
   k=str(n)
   url="https://books.toscrape.com/catalogue/page-"+k+".html" 
   fet=rq.get(url)
   fet.encoding="utf-8"
   soup=BeautifulSoup(fet.text,"html.parser")
   print(soup.title.text)
   lis=soup.find_all("h3")
   price=soup.find_all("p",class_="price_color")
   for i,j in zip(lis,price):
     print(i.a["title"]," - ",j.text)
   for titl in lis:
     b=titl.a["title"]
     cleanlis.append(b)
   for rte in price:
     c=rte.text
     cleanprice.append(c)   
   books={}
   books["book_title"]=cleanlis
   books["price"]=cleanprice
   df=pd.DataFrame(books)
df.to_csv(r'C:\Users\Lenovo\OneDrive\Desktop\DODOW\books.csv')