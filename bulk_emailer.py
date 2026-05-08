import smtplib
connect=smtplib.SMTP('smtp.gmail.com',587)
print("connected")
connect.starttls()
connect.login('njanshemil@gmail.com', 'bshw fkic ojyo aebe')
m=open("emails.txt")
mail=m.readlines()
for email in mail:
    ml=email.strip("\n")
    connect.sendmail("njanshemil@gmail.com",ml,"check check")
connect.quit()
