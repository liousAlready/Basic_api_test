# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/11/28 4:59 下午
# User      : lishouwu
# Product   : PyCharm
# Project   : Basic_api_test
# File      : get_access_token_cases.py
# explain   : 文件说明

import requests
import unittest
from common.localconfig_utlis import local_config
from common.log_utils import logger


class GetAccessTokenCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL
        self.session = requests.Session()

    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        """[case01 正常获取access_token]"""
        logger.info("[case01 正常获取access_token]")
        params = {
            "grant_type": "client_credential",
            "appid": "wxb637f897f0bf1f0d",
            "secret": "501123d2d367b109a5cb9a9011d0f084",
        }
        result = self.session.get(url=self.hosts + '/cgi-bin/token',
                                  params=params)
        self.assertEqual(result.json()['expires_in'], 7200)

    def test_appid_error(self):
        logger.info("[case02 错误的appid]")
        params = {
            "grant_type": "client_credential",
            "appid": "wxb637f897f0bf112f0d",
            "secret": "501123d2d367b109a5cb9a9011d0f084",
        }
        result = self.session.get(url=self.hosts + '/cgi-bin/token',
                                  params=params)
        self.assertEqual(result.json()['errcode'], 40013)


if __name__ == '__main__':
    unittest.main()
