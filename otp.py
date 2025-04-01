"""smtp is used to connect python with ur email"""
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

otp = random.randint(1111,9999)
body = f"Otp for verification is {otp}"

msg = MIMEMultipart()
msg["From"] = "kartiksaridevi02@gmail.com"
msg["To"] = input("Enter Email ID: ")
msg["Subject"] = "Otp For Validation"
msg.attach(MIMEText(body,"plain"))


server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("kartiksaridevi02@gmail.com","qiyg derj dpfd ihwu")
server.send_message(msg)
server.quit()

cotp = int(input("Enter the recieved otp:"))
if cotp == otp:
    print("Otp verification is successfull")

else:
    print("Invalid Otp")
 
