import datetime as dt
import random
import pandas as pd
import smtplib


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
                print(type(self.birthdays))
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
                self.generate_letter(row.name)

    def check_birthday(self, date):
        return date.month == self.date.month and date.day == self.date.day

    def generate_letter(self, name):
        letter_id = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_id}.txt") as letter_file:
            letter_template = letter_file.read()
        letter_msg = letter_template.replace("[NAME]", name)
        print(letter_msg)


# Main
birthday_mailer = BirthdayMailer()
birthday_mailer.check_birthdays()
# print(birthday_mailer.birthdays)

##################### Extra Hard Starting Project ######################

# DONE 1. Update the birthdays.csv
# DONE 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
