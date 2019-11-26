from page.add_person import AddPerson
from page.index_page import IndexPage
from page.save_page import SavePage


class PageFactory(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def index_page(self):
        return IndexPage(self.driver)

    @property
    def add_person(self):
        return AddPerson(self.driver)

    @property
    def save_page(self):
        return SavePage(self.driver)
