from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.webdriver.common.keys import Keys
import time


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__sign_in_locator: str = '//a[contains(text(),"SIGN IN")]'

    def get_sign_in_button(self) -> WebElement:
        return self.is_visible('css', self.__sign_in_locator, 'Search')
