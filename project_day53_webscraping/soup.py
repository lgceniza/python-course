import requests
from bs4 import BeautifulSoup

ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.871971656195164%2C%22east%22%3A-122.30527011279297%2C%22south%22%3A37.678485658229235%2C%22west%22%3A-122.56138888720703%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

HEADERS = {
  "Accept-Language": "en-US,en;q=0.5",
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0"
}


class Soup:
  def __init__(self):
    zillow_html = requests.get(ZILLOW_URL, headers=HEADERS).text
    self.__soup = BeautifulSoup(zillow_html, 'html.parser')
    self.__addresses = [addr.text.strip() for addr in self.__soup.select('[data-test="property-card-addr"]')]
    self.__prices = [price.text.replace('/','+').split('+')[0] for price in self.__soup.select('[data-test="property-card-price"]')]
    self.__links = ["https://www.zillow.com" + link.get('href') for link in self.__soup.select('[data-test="property-card-link"]')]
  
  def getDetails(self):
    return list(zip(self.__addresses, self.__prices, self.__links))
