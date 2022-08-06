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
        self.signin_page_link_locator: str = '//*[@rel="canonical"][@href="https://www.paramountplus.com/account/signin/"]'

    def get_sign_in_page_link(self) -> WebElement:
        return self.is_present('xpath', self.signin_page_link_locator)
