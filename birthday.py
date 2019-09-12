from banner import banner
import datetime

banner("Birthday", "Gavin")

# 1. Find out when you were born
# 2. Figure out how many days until your birthday
# 3. Print information about the birthday: Days until, Days ago, or Happy birthday

def main():
    get_birthday_info()
    compute_days_between_dates()
    print_birthday_info()

def get_birhtday_info():
    print("When were you born?")
    year = int(input("Year [YYYY] > "))
    month = int(input("Month [MM] > "))
    day = int(input("Day [DD] > "))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates():
    pass

def print_birthday_info():
    pass
get_birhtday_info()