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
    [1, 2, 0.5],
    [6, 6, 1],
    [-9, 9, -1],
    [-9, -9, 0],
    [0, 1, 0],
    [50000000000000, 5, 10000000000000],
    [10, 0.5,20 ]
]


@ddt
class TestDiv(TestCase):

    @data(*da)
    @unpack
    def testDiv(self, a, b, c):
        calc = Calc()
        sum = calc.devision(a, b)

        self.assertEqual(sum, c)
