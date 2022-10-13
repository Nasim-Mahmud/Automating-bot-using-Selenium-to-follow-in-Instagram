import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

LINK = "https://www.instagram.com/"
id = os.environ["ID"]
password = os.environ["PASS"]

chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get()

item = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
item.send_keys("00")

# driver.quit()