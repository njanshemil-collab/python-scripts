import pandas as pd
import openpyxl
print("enter your csv file ")
pat=input("enter :")
df=pd.read_csv(pat)
flnme=input("enter file name :")
print("enter your sheet name ")
sht=input("name :")
df.to_excel(flnme+".xlsx",index=False,sheet_name=sht)
print("file name : ",flnme+".xlsx")
print("sheet name : ",sht)