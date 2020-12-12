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
                self.birthdays = pd.read_csv(data_file)
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
                print(birthday)

    def check_birthday(self, date):
        return date.month == self.date.month and date.day == self.date.day


        # Main
birthday_mailer = BirthdayMailer()
birthday_mailer.check_birthdays()
# print(birthday_mailer.birthdays)

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
