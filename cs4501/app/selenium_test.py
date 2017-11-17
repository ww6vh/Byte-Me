import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(
			command_executor='http://selenium-chrome:4444/wd/hub',
			desired_capabilities=DesiredCapabilities.CHROME
			)

	def test_home(self):
		driver = self.driver
		driver.get("http://web:8000/home/")
		assert "Welcome to ByteMe" in driver.page_source

	def test_signUp(self):
		driver = self.driver
		driver.get("http://web:8000/home/")
		driver.find_element_by_id("signup").click()
		assert "Sign up" in driver.page_source

	def test_login(self):
		driver = self.driver
		driver.get("http://web:8000/home/")
		driver.find_element_by_id("login").click()
		assert "Log In" in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
    unittest.main()
