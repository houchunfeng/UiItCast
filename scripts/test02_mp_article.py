import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

# 获取日志器对象
log = GetLog.get_logger()


class TestMpArticle:

    def setup_class(self):
        # 初始化driver
        self.driver = GetDriver.get_driver(page.url_mp)
        # 统一入口类
        # 使用统一入口类对象---调用登录成功方法
        self.login = PageIn(self.driver).page_get_PageMpLogin().page_mp_login_success()
        # 获取 发布文章的页面驱动对象
        self.article = PageIn(self.driver).page_get_PageMpArticle()

    def teardown_class(self):
        """
        关闭driver
        :return:
        """
        GetDriver.quit_driver()

    # 登录测试业务方法
    @pytest.mark.parametrize("title, content, expect", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content, expect):
        # 调用发布文章的业务方法
        self.article.page_publish_article(title, content)
        try:
            # 断言     ***指定异常信息
            assert expect == self.article.page_get_commit_result()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            # 抛异常
            raise
