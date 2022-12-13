import smtplib, random
import datetime as dt

EMAIL = input('Email: ')
PASSWORD = "umsokfspmluttuvp"

if dt.datetime.now().weekday() == 0:
  with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(user=EMAIL, password=PASSWORD)

    with open('quotes.txt') as f:
      message = random.choice(f.readlines())

    smtp.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Monday Motivation!\n\n{message}")
