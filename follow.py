from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException


class Follow:
    def __init__(self):
        chrome_drive_path = "C:\Development\chromedriver.exe"
        self.s = Service(chrome_drive_path)
        self.driver = webdriver.Chrome(service=self.s)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for button in follow_buttons:
            try:
                button.click()
                sleep(2)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.CSS_SELECTOR, ".x5fp0pe ._a9-z ._a9_1")
                cancel.click()
