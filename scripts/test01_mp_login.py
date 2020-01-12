import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

# 获取日志器对象
log = GetLog.get_logger()


class TestMpLogin:

    def setup_class(self):
        # 初始化driver
        self.driver = GetDriver.get_driver(page.url_mp)
        # 获取pageMpLogin对象（统一入口类）
        self.login = PageIn(self.driver).page_get_PageMpLogin()

    # 关闭driver
    def teardown_class(self):
        GetDriver.quit_driver()

    # 登录测试业务方法
    @pytest.mark.parametrize("phone, code, expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, phone, code, expect):
        # 调用登录业务方法
        self.login.page_mp_login(phone, code)
        try:
            # 断言  昵称   ***指定异常信息
            assert expect == self.login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛异常
            raise
