# -*- coding: utf-8 -*-
# @Time : 2021/12/1 10:09
# @Author : Limusen
# @File : random


import random


def random_name():
    code = ''.join(random.choice("abcdefghijklmn7654321") for i in range(5))
    return code


print(random_name())