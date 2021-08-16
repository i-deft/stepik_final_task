from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException


class ProductPage(BasePage):
    def should_be_product_url(self):
        assert '/?promo=' in self.url, 'URL некорректен'

    def add_to_basket(self):
        try:
            button = self.browser.find_element(*ProductPageLocators.add_to_basket)
        except NoSuchElementException:
            return False
        assert button
        button.click()

    def check_name_and_price_of_item(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.name_of_book).text
        book_price = self.browser.find_element(*ProductPageLocators.price).text
        assert name_of_book == self.browser.find_element(*ProductPageLocators.basket_name).text, 'Название книги неверно'
        assert book_price == self.browser.find_element(*ProductPageLocators.basket_price).text, 'Цена книги неверна'




