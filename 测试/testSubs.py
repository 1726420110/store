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
from ddt import ddt
from ddt import data
from ddt import unpack
from Calc import Calc

da = [
    [1, 2, -1],
    [5, 6, -1],
    [-9, 8, -17],
    [-9, -9, 0],
    [0, 0, 0],
    [50000, 5, 49995],
    [10, -10, 20]
]


@ddt
class TestSubs(TestCase):

    @data(*da)
    @unpack
    def testSubs(self, a, b, c):
        calc = Calc()
        sum = calc.subs(a, b)

        self.assertEqual(sum, c)
