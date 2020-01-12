from selenium.webdriver.common.by import By

"""以下为黑马头条项目url"""
# 自媒体
url_mp = "http://ttmp.research.itcast.cn/#/login"


"""以下为自媒体数据配置"""
# 手机号
mp_phone_css = By.CSS_SELECTOR, "[placeholder='请输入手机号']"
# 验证码
mp_code_css = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录
mp_login_css = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"

"""以下是内容管理的数据配置"""
# 点击内容管理
mp_content_manage = By.XPATH, "//div[@class='menu-wrapper']//*[text()='内容管理']"
# 点击发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 输入标题
mp_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# 输入内容之前要切换iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 输入内容
mp_content = By.CSS_SELECTOR, "#tinymce"
# 选择封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 选择点击请选
mp_select = By.CSS_SELECTOR, "[placeholder='请选择']"
# 点击具体频道----数据库
mp_select_database = By.XPATH, "//*[text()='数据库']"
# 点击发表
mp_commit = By.CSS_SELECTOR, ".el-button.filter-item.el-button--primary"
# 获取发表结果
mp_commit_result = By.XPATH, "//*[contains(text(),'成功')]"
