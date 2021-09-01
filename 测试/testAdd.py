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
    [1, 2, 3],
    [5, 6, 11],
    [-9, 8, -1],
    [-9, -9, -18],
    [0, 0, 0],
    [50000000000000, 5, 50000000000005],
    [10, 10, 20]
]


@ddt
class TestAdd(TestCase):

    @data(*da)
    @unpack
    def testAdd(self, a, b, c):
        calc = Calc()
        sum = calc.add(a, b)

        self.assertEqual(sum, c)

