import smtplib
from parameters import password

myemail = ""

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # secures connection
connection.login(user=myemail, password=password)
