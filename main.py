# Python Modules
import datetime as dt
import pandas as pd
import random
import smtplib

# Local Modules
import parameters as pr


# Constants
file_birthdays = "data/birthdays.csv"


# Classes
class BirthdayMailer():
    """  """

    def __init__(self):
        """  """
        self.get_date()
        self.get_birthdays()

    def get_date(self):
        self.date = dt.datetime.now().date()

    def get_birthdays(self):
        try:
            with open(file_birthdays, mode="r") as data_file:
                self.birthdays = pd.read_csv(data_file, index_col=0)
        except FileNotFoundError:
            print("No birthdays data exists")
            return False
        else:
            return True

    def check_birthdays(self):
        for _, row in self.birthdays.iterrows():
            birthday = dt.datetime(
                year=row.year, month=row.month, day=row.day).date()
            if self.check_birthday(birthday):
                self.send_Birthday_letter(row)

    def check_birthday(self, date):
        return date.month == self.date.month and date.day == self.date.day

    def generate_letter(self, name):
        letter_id = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_id}.txt") as letter_file:
            letter_template = letter_file.read()
        letter_msg = letter_template.replace("[NAME]", name)
        return letter_msg

    def send_Birthday_letter(self, birthday_person):
        subject = f"Happy Birthday {birthday_person.name}"
        message = self.generate_letter(birthday_person.name)
        email_msg = f"Subject: {subject}\n\n{message}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # secures connection
            connection.login(user=pr.my_email, password=pr.password)
            connection.sendmail(
                from_addr=pr.my_email,
                # Would be birthday_person.email but using demo to_email for testing
                to_addrs=pr.to_email,
                msg=email_msg)


# Main
birthday_mailer = BirthdayMailer()
birthday_mailer.check_birthdays()

##################### Extra Hard Starting Project ######################

# DONE 1. Update the birthdays.csv
# DONE 2. Check if today matches a birthday in the birthdays.csv
# DONE 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# DONE 4. Send the letter generated in step 3 to that person's email address.
