""" import smtplib
import parameters as pr


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # secures connection
    connection.login(user=pr.my_email, password=pr.password)
    connection.sendmail(
        from_addr=pr.my_email,
        to_addrs=pr.to_email,
        msg="Subject: Hello\n\nThis is the email body")
 """


import datetime as dt


now = dt.datetime.now()
print(now)


date_of_birth = dt.datetime(year=1989, month=1, day=18)
print(date_of_birth)
