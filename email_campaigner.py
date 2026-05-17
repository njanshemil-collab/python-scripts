import pandas as pd
import smtplib
connect=smtplib.SMTP('smtp.gmail.com',587)
print("connected")
connect.starttls()
print("enter your mail id and paste the app password")
mymail=input("your mail :")
appass=input("app pass :")
connect.login(mymail,appass)
df=pd.read_csv("contacts.csv")
for i in range(len(df)):
    name=df["name"][i]
    emaill=df["email"][i]
    message=df["message"][i]
    print("To : ",name," email : ",emaill," message : ",message)
    try:
        connect.sendmail(mymail,emaill,"Subject : Message to "+name+"\n\n"+message)
        print("sent to ",name)
    except:
        print("not sent to ",name)
connect.quit()