import datetime


def print_header():
    print('----------------------------')
    print("       BIRTHDAY APP         ")
    print('----------------------------')
    print()

def get_birthday_from_user():
    print("When were you born? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))

    birthday = datetime.date(year,month,day)
    return birthday
    

def compute_days_between_dates(original_date,target_date):
    this_year = datetime.date(target_date.year,original_date.month,original_date.day)
    dt = this_year - target_date
    return dt.days

def print_birthday_info(days):
    if days < 0:
        print("Your birthday was {} days ago ".format(-days))
    elif days > 0:
        print("Your birthday will be in {} days.".format(days))
    else:
        print("Happy Birthday!")

def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    today = datetime.date.today()
    time_delta = (compute_days_between_dates(bday, today))
    print_birthday_info(time_delta)

main()