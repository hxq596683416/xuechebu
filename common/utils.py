# 1. 导包

from appium import webdriver


def init_driver():
    """驱动对象获取方法"""

    # 3. 声明启动参数
    capabilities = {
        "platformName": "Android",  # 平台名称 iOS 或 Android
        "platformVersion": "5.1",  # 手机系统版本
        "deviceName": "模拟器",  # 设备名称(模拟器或真机)
        "appPackage": "com.android.contacts",  # App 应用的包名
        "appActivity": ".activities.PeopleActivity",  # App 应用的启动名
        "resetKeyboard": True,
        "unicodeKeyboard": True

    }

    #     capabilities = dict()  # 声明空字典
    # capabilities['platformName'] = "Android"  # 平台类型(iOS 和 Android)
    # capabilities['platformVersion'] = "5.1"  # 手机系统版本
    # capabilities['deviceName'] = "模拟器"  # 设备名称
    # capabilities['appPackage'] = "com.android.contacts"  # 待测应用的包名
    # capabilities['appActivity'] = ".activities.PeopleActivity",  # 待测应用的启动名
    # capabilities['resetKeyboard'] = True
    # capabilities['unicodeKeyboard'] = True

    # 通讯录 包名/启动名
    # com.android.contacts/.activities.PeopleActivity

    # 2. 实例化驱动对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver
