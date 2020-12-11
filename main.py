import smtplib
import parameters as pr


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()  # secures connection
connection.login(user=pr.my_email, password=pr.password)
connection.sendmail(from_addr=pr.my_email,
                    to_addrs=pr.to_email,
                    msg="Subject: Hello\n\nThis is the email body")
connection.close()
