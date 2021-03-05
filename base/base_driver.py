from appium import webdriver


def init_driver():
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = 'H4K5T20B24018397'
    # app信息
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'
    # 不重置应用
    #desired_caps['noReset'] = True

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)