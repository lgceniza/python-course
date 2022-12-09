import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MINIMUM_SPEED = 45
SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"

options = Options()
# options.headless = True

class InternetSpeedTwitterBot:
  def __init__(self, username, password, options=options):
    self.driver = webdriver.Chrome('chromedriver', options=options)
    self.username = username
    self.password = password
    self.down = 0
  
  def getInternetSpeed(self):
    print("Performing SpeedTest.")
    self.driver.get(SPEEDTEST_URL)

    el = WebDriverWait(self.driver, 60).until(
      EC.element_to_be_clickable((By.CLASS_NAME, 'js-start-test'))
    )
    el.click()
    time.sleep(30)

    self.down = float(self.driver.find_element(By.CLASS_NAME, 'download-speed').text)
    print("SpeedTest done.")

  def tweetAtProvider(self):
    if self.down >= MINIMUM_SPEED:
      print("Internet speed is good. Will not send tweet to ISP. Exiting...")
      return

    print("Sending tweet...")
    self.driver.get(TWITTER_URL)
    el = WebDriverWait(self.driver, 60).until(
      EC.presence_of_element_located((By.NAME, 'text'))
    )
    el.send_keys(self.username + Keys.ENTER)

    el = WebDriverWait(self.driver, 60).until(
      EC.presence_of_element_located((By.NAME, 'password'))
    )
    el.send_keys(self.password + Keys.ENTER)

    el = WebDriverWait(self.driver, 60).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]'))
    )
    el.send_keys(f"My Internet speed is {self.down} Mbps. I thought the minimum was {MINIMUM_SPEED}, @/Globe?")

    self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]').click()
    print("Tweet sent.")
