import os
print(os.getcwd())
import pandas as pd
print("enter your csv file ")
while True:
 pat=input("enter valid path :")
 try:
  df=pd.read_csv(pat)
  break
 except FileNotFoundError:
  print("give valid csv path ")
flnme=input("enter file name :")
print("enter your sheet name ")
sht=input("name :")
df.to_excel(flnme+".xlsx",index=False,sheet_name=sht)
print("file name : ",flnme+".xlsx")
print("sheet name : ",sht)
print("rows = ",df.shape[0])
print("colomns = ",df.shape[1])