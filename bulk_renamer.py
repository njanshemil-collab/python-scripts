import os
print(os.getcwd())
c=os.listdir(r'C:\Users\Lenovo\OneDrive\Desktop\shemi codes test')
for i in c:
   os.rename(os.path.join(r'C:\Users\Lenovo\OneDrive\Desktop\shemi codes test',i),os.path.join(r'C:\Users\Lenovo\OneDrive\Desktop\shemi codes test',"mew_"+i))
              

