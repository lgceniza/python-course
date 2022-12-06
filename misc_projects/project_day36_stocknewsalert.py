import requests, re
import pandas as pd

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "JZJZ4STKUIP3UWS1"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "0fb8820eed454cb7a4e27cc5a8dd54d8"

STOCK_PARAMS = {
  'function': 'TIME_SERIES_DAILY_ADJUSTED',
  'symbol': STOCK_NAME,
  'apikey': STOCK_API_KEY
}

NEWS_PARAMS = {
  'q': COMPANY_NAME,
  'apiKey': NEWS_API_KEY
}

r = requests.get(STOCK_ENDPOINT, STOCK_PARAMS)
r.raise_for_status()

data = pd.DataFrame(r.json()['Time Series (Daily)'])
closing_prices = [date[1] for date in list(data.iloc[4,:2].items())]

percent_diff = round(abs(float(closing_prices[0]) - float(closing_prices[1])) / float(closing_prices[1]) * 100, 1)

if percent_diff > 5:
  r = requests.get(NEWS_ENDPOINT, NEWS_PARAMS)
  r.raise_for_status()

articles = r.json()['articles'][:3]

news = []
for article in articles:
  message = f"{STOCK_NAME}: {'🔺' if closing_prices[0] > closing_prices[1] else '🔻'}{percent_diff}%\n"
  message += f"Headline: {article['title']}\n"
  message += f"Brief: {re.sub(re.compile('<.*?>'), '', article['description'])}\n"
  message += f"Read more here: {article['url']}\n\n"
  news.append(message)

for article in news:
  print(article)
