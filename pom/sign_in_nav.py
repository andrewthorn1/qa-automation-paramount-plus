from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.keys import Keys
import time


class SignInPageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__title_locator: str = '//title[contains(text(),"Paramount Plus Sign In")]'
        self.__signin_page_link_locator: str = '//*[@rel="canonical"][@href="https://www.paramountplus.com/account/signin/"]'
        self.__input_email_fild_locator: str = '//*[@name="email"]'
        self.__input_password_fild_locator: str = '//*[@name="password"]'
        self.__recapcha_locator: str = '//*[@class="recaptcha-checkbox-border"]'
        self.__continue_button_locator: str = '//button[@type="button"]'
        self.__invalid_email_alert: str = '//p[@role="alert"]'

    def get_sign_in_page_link(self) -> WebElement:
        return self.is_present('xpath', self.__signin_page_link_locator)

    def get_input_email_fild(self) -> WebElement:
        return self.is_visible("xpath", self.__input_email_fild_locator)

    def get_input_password_fild(self) -> WebElement:
        return self.is_visible("xpath", self.__input_password_fild_locator)

    def get_recapcha_checkbox(self):
        return self.is_visible("xpath", self.__recapcha_locator)

    def get_continue_button(self):
        return self.is_visible("xpath", self.__continue_button_locator)

    def get_alert(self):
        return self.is_visible("xpath", self.__invalid_email_alert)
