# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/11/28 4:59 下午
# User      : lishouwu
# Product   : PyCharm
# Project   : Basic_api_test
# File      : create_tag_cases01.py
# explain   : 文件说明
import warnings

import requests
import unittest
from common.localconfig_utlis import local_config
from common.log_utils import logger
from common.common_api import *


class CreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.hosts = local_config.URL
        self.session = requests.Session()

    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        logger.info("[case01 创建标签]")  # 用例方法: 提供测试数据 测试操作步骤 断言判定
        response = get_access_token_api(self.session,
                                        "client_credential",
                                        "wxb637f897f0bf1f0d",
                                        "501123d2d367b109a5cb9a9011d0f084")

        token = response.json()['access_token']
        post_params = {"tag": {"name": "keguasjas"}}
        create_tag_response = create_usr_tag_api(self.session, token, post_params)
        actual_result = create_tag_response.json()['tag']['name']
        self.assertEqual(actual_result, "keguasjas")

    def test_add_tag01(self):
        logger.info("[case01 创建标签]")
        token = get_token_value(self.session)
        post_params = {"tag": {"name": "1236665sss"}}
        create_tag_response = create_usr_tag_api(self.session, token, post_params)
        actual_result = create_tag_response.json()['tag']['name']
        self.assertEqual(actual_result, "1236665sss")


if __name__ == '__main__':
    unittest.main()
