from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):
    baseURL = "https://hard.clurb.net/login"
    driver = webdriver.Chrome(executable_path="C:\\Users\\ASUS\\Desktop\\Selenium\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("testCihan@test.com", "123456789")
        result = self.lp.verifyLoginSuccessful()

        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)

        self.lp.login("InvalidEmail@gmail.com", "testWithInvalidPassword")
        result = self.lp.verifyLoginFailed()

        assert result == False

if __name__ == "__main__":
    unittest.main()
