from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class Sel:
    def __init__(self, link):
        self.chrome_drive_path = "C:\Development\chromedriver.exe"
        self.s = Service(self.chrome_drive_path)
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get(link)
