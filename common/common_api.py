# -*- coding: utf-8 -*-
# @Time : 2021/11/30 16:46
# @Author : Limusen
# @File : common_api


import requests
from common.localconfig_utlis import local_config


def get_access_token_api(session, grant_type, appid, secret):
    params = {
        "grant_type": grant_type,
        "appid": appid,
        "secret": secret,
    }
    headers = {'content_type': 'application/json'}
    response = session.get(url=local_config.URL + '/cgi-bin/token',
                           params=params,
                           headers=headers)
    return response


def get_token_value(session):
    response = get_access_token_api(session,
                                    "client_credential",
                                    "wxb637f897f0bf1f0d",
                                    "501123d2d367b109a5cb9a9011d0f084")
    return response.json()['access_token']


def create_usr_tag_api(session, access_token, tag_json):
    """
    fang
    :param access_token:
    :param tag_json:
    :return:
    """
    params = {
        "access_token": access_token
    }
    json_data = tag_json
    headers = {'content_type': 'application/json'}
    response = session.post(url=local_config.URL + "/cgi-bin/tags/create",
                            params=params,
                            json=json_data,
                            headers=headers)

    return response


def delete_usr_tag_api(session, access_token, tag_json):
    """
    删除标签
    :param access_token:
    :param tag_json:
    :return:
    """
    params = {
        "access_token": access_token
    }
    json_data = tag_json
    response = session.post(url=local_config + "/cgi-bin/tags/delete",
                            params=params,
                            json=json_data)
    return response
