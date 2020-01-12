import logging.handlers


class GetLog:
    __logger = None

    # 获取日志器方法
    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger("hcf")
            # 设置 日志器默认级别
            cls.__logger.setLevel(logging.INFO)
            # 获取处理器 根绝时间切割
            th = logging.handlers.TimedRotatingFileHandler(filename="./log/hmtt.log",
                                                           when='D',
                                                           interval=1,
                                                           encoding="utf-8",
                                                           )
            # 获取 格式器
            fm = ""
            fmt = logging.Formatter(fm)
            # 将格式器--->处理器
            th.setFormatter(fmt)
            # 将处理器--->日志器
            cls.__logger.addHandler(th)
        return cls.__logger


# 测试日志的方法
if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info("info级别的错误")
    log.error("error级别的错误")
    log.warning("warning级别的错误")
