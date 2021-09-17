from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email_field = "email"
    _password_field = "password"
    _login_button = "button"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="linktext")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")


    def login(self, email="", password=""):
        # self.clickLoginLink()
        # self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("/html//div[@id='content-area']/div[@class='content-wrapper']//header/div[@class='vs-con-items']/div[4]/button", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//?/p[@innertext='There is 1 error']", locatorType="xpath")
        return result

    def clearFields(self):
        emailField =  self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
