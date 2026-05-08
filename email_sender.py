import smtplib
connect=smtplib.SMTP('smtp.gmail.com',587)
print("connected")
connect.starttls()
connect.login('njanshemil@gmail.com', 'bshw fkic ojyo aebe')
connect.sendmail('njanshemil@gmail.com','mshemil004@gmail.com','hai,how are you hellooooooo ')
connect.quit()