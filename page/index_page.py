import page
from base.base_page import BasePage


class IndexPage(BasePage):
    address_book = page.address_book

    def click_address_book(self):
        return self.click_func(self.address_book)
