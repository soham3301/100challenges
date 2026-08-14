
import random
import smtplib
import csv
import datetime as dt

now = dt.datetime.now()
date_of_today = now.day
month_of_today = now.month

def load_credential():
    creds = []
    with open("./constants.csv") as cons_file:
        render_cons = csv.reader(cons_file)
        for row in render_cons:
            creds.append(row[1])
    return creds

def load_birthday_mail(the_name):
    mail = ""
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        the_letter = letter_file.read()
        mail = the_letter.replace("[NAME]", the_name)
    return mail

def send_birthday_mail(cred, letter, to_email):
    my_email = cred[0]
    my_password = cred[1]
    try:
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            subject = "HAPPY BIRTHDAY"
            body = letter
            message = f"Subject: {subject}\n\n{body}"
            connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=message)
    except Exception as e:
        print(e)

with open("./birthdays.csv") as birthday_file:
    render_bday = csv.reader(birthday_file)
    for row in render_bday:
        if row[0] != "name":
            if int(row[4]) == date_of_today and int(row[3]) == month_of_today:
                print("Someone has birthday today")
                name = row[0]
                target_email = row[1]
                cred_list = load_credential()
                the_mail = load_birthday_mail(name)
                send_birthday_mail(cred_list, the_mail, target_email)
                print(f"Birthday wish sent to {target_email}")
