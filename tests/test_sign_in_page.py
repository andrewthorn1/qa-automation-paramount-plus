import pytest
from pom.homepage_nav import HomepageNav
from pom.sign_in_nav import SignInPageNav
import time
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures('setup')
class TestSignInPage:

    def test_invalid_email_or_password(self):
        homepage_nav = HomepageNav(self.driver)
        sign_in_nav = SignInPageNav(self.driver)
        homepage_nav.get_sign_in_button().click()
        sign_in_nav.get_input_email_fild().send_keys('thornpython@gmail.com')
        sign_in_nav.get_input_password_fild().send_keys('WRONG PASSWORD')
        sign_in_nav.get_continue_button().click()
        time.sleep(1)
        assert sign_in_nav.get_alert()





