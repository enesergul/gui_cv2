from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.udemy.com')
time.sleep(20)
signup = driver.find_elements("xpath",'//*[@id="udemy"]/div[1]/div[1]/div[3]/div[7]/a/span')
time.sleep(2)
signup[0].click()
driver.close()