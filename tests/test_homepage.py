import pytest
from pom.homepage_nav import HomepageNav
from pom.sign_in_nav import SignInPageNav
import time

@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_goto_sign_in_page(self):
        homepage_nav = HomepageNav(self.driver)
        sign_in_nav = SignInPageNav(self.driver)
        homepage_nav.get_sign_in_button().click()
        assert sign_in_nav.get_sign_in_page_link()

