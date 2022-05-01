from selenium.webdriver.remote.webelement import WebElement
from typing import List
from base.seleniumbase import SeleniumBase
from base.utils import Utils


class HomepageNav(SeleniumBase): #  Наследуем класс SeleniumBase

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'
        self.NAV_LINK_TEXT = 'Women,Men,Beauty,Home,Furniture,Shoes,Handbags,Jewelry,Kids,Toys,Gifts,Own Your Style,Sale'

    def get_nav_links(self) -> List[WebElement]:  # Функция будет возвращать нам наш элемент
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    '''Возвращаем текст с веб элементов'''

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)  # метод возвращат текст
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
