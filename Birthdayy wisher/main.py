import pandas
import random
import smtplib
import datetime as dt

my_email = "lour login"
password = "your password"
completed = ""

now = dt.datetime.now()  # date of present moment
YEAR = now.year
MONTH = now.month
DAY = now.day
print(now)
data = pandas.read_csv("birthdays.csv")
names = data["name"]
print(f"Bugun {YEAR}-yil, {MONTH}-oy, {DAY}-kun, soat {now.hour} dan, {now.minute} minut, o'tdi ")


for name in names:
    person = data[data.name == f"{name}"]
    email = person["email"]
    year = int(person["year"])
    month = int(person["month"])
    day = int(person["day"])
    if month == MONTH and day == DAY:
        # print(f"bugun {name}ning tug'ilgan kuni")
        n = random.randint(1, 3)
        with open(f"letter_templates/letter_{n}.txt") as letter:
            for line in letter:
                completed += line.replace("[NAME]", name)
            with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                # connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:Happy your day\n\n{completed}"
                )