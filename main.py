import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

LINK = "https://www.instagram.com/"
id = os.environ["ID"]
password = os.environ["PASS"]

chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get(LINK)
# To prevent acting like a bot, we need to delay loading time so that Instagram don't block us from logging.
# Trust me, I checked!
sleep(4)


username = driver.find_element(By.NAME, "username")
username.send_keys(id)
sleep(1)

passw = driver.find_element(By.NAME, "password")
passw.send_keys(password)
sleep(1)

submit = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
submit.click()
sleep(10)

search = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
search.send_keys("cookingchannel")
search.send_keys(Keys.ENTER)
sleep(4)



# driver.quit()