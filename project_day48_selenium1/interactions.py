from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

options = Options()
options.headless = True
driver = webdriver.Chrome('chromedriver', options=options)


driver.get(URL)

interactions = driver.find_element(By.CSS_SELECTOR, '[title="Special:Statistics"]').text
print(interactions)


driver.quit()
