# encoding: utf-8
# Author    : limusen
# Datetime  : 2021/11/28 4:59 下午
# User      : lishouwu
# Product   : PyCharm
# Project   : Basic_api_test
# File      : create_tag_cases01.py
# explain   : 文件说明


import requests
import unittest
from common.localconfig_utlis import local_config
from common.log_utils import logger


class CreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = local_config.URL

    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        logger.info("[case01 创建标签]")

        params = {
            "grant_type": "client_credential",
            "appid": "wxb637f897f0bf1f0d",
            "secret": "501123d2d367b109a5cb9a9011d0f084",
        }
        response = requests.get(url=self.hosts + '/cgi-bin/token',
                                params=params)

        get_params = {
            "access_token": response.json()['access_token']
        }
        post_params = {"tag": {"name": "zxzcs123"}}
        headers = {'content_type': 'application/json'}

        create_tag_response = requests.post(url=self.hosts + "/cgi-bin/tags/create", params=get_params,
                                            json=post_params, headers=headers)
        actual_result = create_tag_response.json()['tag']['name']
        self.assertEqual(actual_result, "zxzcs123")



if __name__ == '__main__':
    unittest.main()
