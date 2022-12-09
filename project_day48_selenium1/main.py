import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://orteil.dashnet.org/experiments/cookie/"


d = webdriver.Chrome('chromedriver')

d.get(URL)
cookie = d.find_element(By.ID, 'cookie')

time_check = time.time() + 5
timeout = time.time() + 60*5
while time.time() < timeout:
  cookie.click()

  if time.time() >= time_check:
    buyable = d.find_elements(By.CSS_SELECTOR, '#store [class=""]')
    buyable[-1].click()
  
    time_check = time.time() + 5

print(d.find_element(By.ID, 'cps').text)
d.quit()
