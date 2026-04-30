import pandas as pd
import os
print("Enter the path of csv file to clean")
csv=input("enter : ")
df=pd.read_csv(csv)
df=df.dropna()
print(df)
nm=os.path.basename(csv)
df.to_csv('cleaned_'+nm)
print("Rows = ",df.shape[0])
print("columns = ",df.shape[1])
print(list(df.columns))