from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    add_to_basket = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    name_of_book = (By.CSS_SELECTOR, '.col-sm-6.product_main > h1')
    price = (By.CSS_SELECTOR, '.col-sm-6.product_main > .price_color')
    basket_name = (By.CSS_SELECTOR, '.fade.in:nth-child(1) > .alertinner > strong')
    basket_price = (By.CSS_SELECTOR, '.fade.in:nth-child(3) > .alertinner strong')
    basket_link = (By.CSS_SELECTOR, 'span[class="btn-group"]')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")