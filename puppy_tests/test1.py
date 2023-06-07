from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
from selenium import webdriver
import brooke
import sparky


class AdoptPuppies(unittest.TestCase):

    def Webdriver(self):
        self.driver: WebDriver = webdriver.Chrome()

    def adopte_brooke(self):
        self.driver.get(brooke)

    def adopte_sparky(self):
        self.driver.get(sparky)

    def tearDown(self):
        self.driver.quit()

