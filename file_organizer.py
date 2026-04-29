import os
print("Enter the path of Folder to organize")
user=input("enter : ")
file=os.listdir(user)
for i in file:
    split=os.path.splitext(i)
    x=split[1][1:]
    os.makedirs(os.path.join(user,x),exist_ok=True)
    os.rename(os.path.join(user,i),os.path.join(os.path.join(user,x),i))