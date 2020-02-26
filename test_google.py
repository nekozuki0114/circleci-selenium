import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestGoogle:

    driver = webdriver.Chrome(ChromeDriverManager().install())

    def setup_class(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def setup_method(self):
        self.driver.get("http://172.17.0.1:80/")

    def test_case(self):
        driver = self.driver

        driver.save_screenshot("test-reports/result_001.png")


    def teardown_class(cls):
        cls.driver.quit()
