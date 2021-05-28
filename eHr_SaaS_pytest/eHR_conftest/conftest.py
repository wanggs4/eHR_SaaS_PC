# coding:utf-8
import pytest

class Testclass:

    # @fixture(scope="function", params=None, autouse=False,ids=None, name=None)
    @pytest.fixture(scope='function')
    def login(slef):
        print("输入账号密码登录")
