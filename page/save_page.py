import page
from base.base_page import BasePage


class SavePage(BasePage):
    save = page.save

    def click_save(self):
        self.click_func(self.save)
