# coding:utf-8
import pytest
import selenium.webdriver

class Testclass:

    def setup_function():
        print('setup_function:每个用例开始前都会执行')

    def teardown_function():
        print('teardown_function:每个用例结束后都会执行')

    def setup_module():
        print('setup_module:整个.py模块只执行一次，比如所有的用例开始前只打开一次浏览器')

    def teardown_module():
        print('teardown_module:整个.py模块只执行一次,比如所有的用例结束只最后关闭浏览器')

    def func(x):
        return x + 1

    def test_login(login):
        print('用例1，执行前先执行login')
        print(login)

    def test_1(self):
        print('test_1')
        s='wang'
        assert 'w' in s

    def test_2(self):
        print('test2')
        q='wangguosheng'
        assert hasattr(q,'w')

    def test_3(self):
        print('test3')
        a='wang'
        b='wangguosheng'
        assert  a in b

if __name__ == '__main__':
    pytest.main('-q test_empCheck.py')


