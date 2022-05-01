import time

import pytest
from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        # print(homepage_nav.get_nav_links_text())
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert expected_links == actual_links, 'Validation Nav Links Text'
        # elements = homepage_nav.get_nav_links()
        for index in range(8):
            homepage_nav.get_nav_links()[index].click()
            homepage_nav.driver.delete_all_cookies()  # удаление куки при переходе на другую страницу
        # homepage_nav.get_nav_link_by_name('Beauty').click()
        time.sleep(1.5)
