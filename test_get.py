#encoding:utf-8
import requests
import unittest
from selenium import webdriver

class TestGet(unittest.TestCase):
    def test_get1(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://www.baidu.com'
        s = self.driver.get(self.url)
        return s


if __name__ == '__main__':
    unittest.main()