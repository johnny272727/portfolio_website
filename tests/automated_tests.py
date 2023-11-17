import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from pathlib import Path

class PortfolioAutoTest(unittest.TestCase):
    def setUp(self):
      self.web_url = "https://ningz27.pythonanywhere.com"
      self.options = webdriver.EdgeOptions()
      self.options.add_argument("headless")
      self.driver = webdriver.Edge(options=self.options)
      
    def test_is_website_availability(self):
        self.driver.get(self.web_url)
        self.assertIn('Ning - Portfolio',self.driver.title)
        
    def test_send_msg_btn_availability(self):
        self.driver.get(self.web_url)
        element = self.driver.find_element(By.ID,'sendMessageButton')
        self.assertEqual(element.text, 'Send Message')

    def teste

    def tearDown(self):
        self.driver.close()

# 'Ning - Portfolio'
if __name__ == '__main__':
    unittest.main()