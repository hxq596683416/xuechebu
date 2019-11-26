# 添加通讯录页面
from selenium.webdriver.common.by import By

address_book = By.ID, "com.android.contacts:id/floating_action_button"
# 保存选择页面
save = By.XPATH, "//*[contains(@text,'本地保存')]"
# 添加用户页面
name = By.XPATH, "//*[contains(@text,'姓名')]"
name_spell = By.XPATH, "//*[contains(@text,'姓名拼音')]"
# nickname = By.XPATH, "//*[contains(@text,'昵称')]"
phone = By.XPATH, "//*[contains(@text,'电话')]"
back_btn = By.CLASS_NAME, "android.widget.ImageButton"
