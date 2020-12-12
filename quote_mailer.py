from random import choice
import datetime as dt
import smtplib
import parameters as pr


# Main
quotes_file = "data/quotes.txt"

weekday = dt.datetime.now().weekday()
if weekday == 4:
    with open(quotes_file, mode="r", encoding="utf-8") as quotes_data:
        quotes = quotes_data.readlines()
    random_quote = choice(quotes)
    random_quote = random_quote.replace(
        "“", "\"").replace("”", "\"").replace("…", "...").replace("–", "-")
    # print(random_quote)

    email_msg = f"Subject: Inspirational Quote\n\nMessage: \n{random_quote}"
    # print(email_msg)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # secures connection
        connection.login(user=pr.my_email, password=pr.password)
        connection.sendmail(
            from_addr=pr.my_email,
            to_addrs=pr.to_email,
            msg=email_msg)
