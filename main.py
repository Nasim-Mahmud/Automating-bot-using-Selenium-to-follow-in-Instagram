import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException


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

# Logging into account
username = driver.find_element(By.NAME, "username")
username.send_keys(id)
sleep(1)

passw = driver.find_element(By.NAME, "password")
passw.send_keys(password)
sleep(1)

submit = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
submit.click()
sleep(10)

# Searching for the designated page
search = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
search.send_keys("cookingchannel")
sleep(2)
search.send_keys(Keys.ARROW_DOWN)
sleep(2)
search.send_keys(Keys.ENTER)
sleep(7)

# Following the followers of the page.
followers = driver.find_element(By.CSS_SELECTOR, ".xieb3on li a")
followers.click()
sleep(4)

# Clicking follow button
follow_buttons = driver.find_elements(By.CSS_SELECTOR, "._aano button")
for button in follow_buttons:
    try:
        button.click()
        sleep(2)
    except ElementClickInterceptedException:
        cancel = driver.find_element(By.CSS_SELECTOR, ".x5fp0pe ._a9-z ._a9_1")
        cancel.click()

# driver.quit()
