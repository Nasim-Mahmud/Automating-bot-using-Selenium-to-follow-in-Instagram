import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
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


# driver.quit()