from selenium import webdriver


class GetDriver:
    __driver = None

    # 获取driver
    @classmethod
    def get_driver(cls, url):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()
            cls.__driver.maximize_window()
            cls.__driver.get(url)
        return cls.__driver

    # 关闭driver
    @classmethod
    def quit_driver(cls):
        # if cls.__driver is not None:
        if cls.__driver:
            cls.__driver.quit()
            cls.__driver = None
