"""
测试用例
"""
from common.utils import init_driver
from page.page_factory import PageFactory


class TestPage(object):

    def setup(self):
        self.driver = init_driver()
        self.page_factory = PageFactory(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_address_book(self):
        self.page_factory.index_page.click_address_book()
        self.page_factory.save_page.click_save()
        self.page_factory.add_person.input_name("惠普")
        # self.page_factory.add_person.input_name_spell("pujing")
        # self.page_factory.add_person.input_nick_name("小普")
        # self.page_factory.add_person.input_phone("789874")
        self.page_factory.add_person.click_back_btn()
        