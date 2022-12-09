import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

SHEETS_URL = "https://forms.gle/JeVfEkbd7fGroDz18"

options = Options()
# options.headless = True

class FormsBot:
  def __init__(self, options=options):
    self.driver = webdriver.Chrome('chromedriver', options=options)
  
  def fill(self, tup):
    self.driver.get(SHEETS_URL)
    time.sleep(5)

    inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for i, inp in enumerate(inputs):
      inp.send_keys(tup[i])
    
    self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').click()
