import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

# 获取日志器对象
log = GetLog.get_logger()


class Base:

    def __init__(self, driver):
        """
        初始化driver
        :param driver:
        """
        log.info("正在初始化driver：{}".format(driver))
        self.driver = driver

    def base_find(self, loc, timeout=5, poll=0.5):
        """
        查找元素方法----输入，点击，获取文本方法使用
        :param loc:
        :param timeout:
        :param poll:
        :return:
        """
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(loc[0],loc[1]))

    def base_input(self, loc, text):
        """
        输入方法
        :param loc:
        :param text:
        :return:
        """

        ele = self.base_find(loc)
        log.info("正在执行清空操作")
        ele.clear()
        log.info("正在给{}元素 执行输入操作：{}".format(loc, text))
        ele.send_keys(text)

    def base_click(self, loc):
        """
        点击方法
        :param loc:
        :return:
        """
        log.info("正在对{}元素 执行点击操作".format(loc))

        self.base_find(loc).click()

    def base_get_text(self, loc):
        """
        获取文本方法
        :param loc:
        :return:
        """
        log.info("正在获取{}元素文本值：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    def base_get_img(self):
        """
        截图
        :return:
        """
        log.error("出现异常！正在截图操作")
        self.driver.get_screenshot_as_file("./images/err.png")
        self.__base_write_img()

    def __base_write_img(self):
        """
        将图片写入allure报告
        :return:
        """
        log.error("异常处理！正在截图写入报告")
        with open("./images/err.png", "rb")as f:
            allure.attach("错误原因：", f.read(), allure.attach_type.PNG)
