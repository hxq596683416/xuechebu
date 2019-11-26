import page
from base.base_page import BasePage


class AddPerson(BasePage):
    name = page.name
    name_spell = page.name
    phone = page.phone
    # nickname = page.nickname
    back_btn = page.back_btn

    def input_name(self, text):
        self.input_func(self.name, text)

    def input_name_spell(self, text):
        self.input_func(self.name_spell, text)

    # def input_nick_name(self, text):
        self.input_func(self.name_spell, text)

    def input_phone(self, text):
        self.input_func(self.phone, text)

    def click_back_btn(self):
        self.click_func(self.back_btn)
