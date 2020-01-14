import time
import unittest
import os
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearchTest1(unittest.TestCase):

    def setUp(self):
        print("Executing setUp & initializing Selenium")
        caps = {'browserName': 'firefox'}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps)
        self.logger = logging
        self.logger.info("About to call a test")

    def test_app_endpoint(self):
        print("Checking if the app is up or not")
        self.logger.info("In simple")
        browser = self.browser
        browser.get('http://localhost:5001')
        time.sleep(3) # simulate long running test
        self.assertIn("Wisdom of the Ages", browser.title)
        page_heading = browser.find_element_by_name('page_heading')
        quote_button = browser.find_element_by_name('random_quote')
        quote_button.click()
        self.assertIn("Wisdom of the Ages", browser.title)
        self.assertIn('Wisdom of the Ages', browser.page_source)

    def tearDown(self):
        print("Quiting now")
        self.browser.quit() # quit vs close?


if __name__ == '__main__':
    logging.basicConfig(filename='/selenium-plugin.log',level=logging.INFO)
    logging.info("About to call main")
    unittest.main()
