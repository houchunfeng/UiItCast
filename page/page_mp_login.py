from base.base import Base
import page
from tools.get_log import GetLog
# 获取日志器对象
log = GetLog.get_logger()


class PageMpLogin(Base):
    def page_input_phone(self, phone):
        """
        输入手机号
        :param phone: 手机号
        :return:
        """
        self.base_input(page.mp_phone_css, phone)

    def page_input_verify_code(self, code):
        """
         输入验证码
        :param code: 验证码
        :return:
        """
        self.base_input(page.mp_code_css, code)

    def page_click_login_btn(self):
        """
        点击登录按钮
        :return:
        """
        self.base_click(page.mp_login_css)

    def page_get_nickname(self):
        """
        获取 昵称
        :return:
        """
        return self.base_get_text(page.mp_nickname)

    def page_mp_login(self, phone, code):
        """
        组合业务方法----测试脚本业务层调用
        :param phone:手机号
        :param code:验证码
        :return:
        """
        log.info("")
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        self.page_click_login_btn()

    def page_mp_login_success(self, phone="13812345678", code="246810"):
        """
        组合业务方法----登录成功方法
        :param phone:手机号
        :param code:验证码
        :return:
        """
        self.page_input_phone(phone)
        self.page_input_verify_code(code)
        self.page_click_login_btn()
