import datetime as dt
import pandas as pd
import smtplib, random

EMAIL = input('Email: ')
PASSWORD = 'umsokfspmluttuvp'


data = pd.read_csv('birthdays.csv')
today = dt.datetime.now()

data = data[(data.month == today.month) & (data.day == today.day)].reset_index(drop=True)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
  smtp.starttls()
  smtp.login(EMAIL, PASSWORD)

  for _, record in data.iterrows():
    with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as f:
      message = f"Subject: Happy Birthday!\n\n{f.read().replace('[NAME]', record['name'])}"
    
    smtp.sendmail(EMAIL, record['email'], message)
