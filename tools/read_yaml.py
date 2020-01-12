import os
import yaml

from config import BASE_URL


def read_yaml(filename):
    """
    读取yaml数据方法
    :param filename: 文件名字
    :return:
    """
    with open(BASE_URL + os.sep + "data" + os.sep + filename, "r", encoding="utf-8")as f:
        arr = []
        # for data in yaml.load(f).values():
        for data in yaml.load(f, Loader=yaml.FullLoader).values():
            arr.append(tuple(data.values()))
        return arr


# 测试读取方法
# if __name__ == '__main__':
#     print(read_yaml("mp_login.yaml"))
