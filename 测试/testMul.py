'''
    unittest:
    ddt: data driver test
        主角：数据
    ddt
    data
    unpack
    1.@ddt修饰这个类
    2.@data(引入数据)
    3.@unpack 不解包
'''
from unittest import TestCase
from threading import Thread
from ddt import ddt
from ddt import data
from ddt import unpack
from Calc import Calc

da = [
    [1, 2, 2],
    [5, 6, 30],
    [-9, 8, -72],
    [-9, -9, 81],
    [0, 0, 0],
    [10000000000000, 5, 50000000000000],
    [10, 10, 100]
]


@ddt
class TestMul(TestCase):

    @data(*da)
    @unpack
    def testMul(self, a, b, c):
        calc = Calc()
        sum = calc.multi(a, b)

        self.assertEqual(sum, c)
