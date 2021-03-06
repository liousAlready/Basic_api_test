# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 8:50 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : localconfig_utlis.py
# @Software: PyCharm


import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '..', 'conf/config.ini')


class LocalconfigUtils():
    ''' 取配置文件方式二 '''

    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding='utf-8')

    @property  # 把方法变成属性方法
    def URL(self):
        url_value = self.cfg.get('default', 'URL')
        return url_value

    @property
    def CASE_DATA_PATH(self):
        case_data_path_value = self.cfg.get('path', 'CASE_DATA_PATH')
        return case_data_path_value

    @property
    def REPORT_PATH(self):
        reports_path = self.cfg.get('path', 'REPORT_PATH')
        return reports_path

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('path', 'LOG_PATH')
        return log_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = self.cfg.get('log', 'LOG_LEVEL')
        return int(log_level_value)


local_config = LocalconfigUtils()

if __name__ == "__main__":
    print(local_config.URL)
