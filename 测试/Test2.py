import unittest, threading
from testAdd import TestAdd
from testSubs import TestSubs
from testMul import TestMul
from testDiv import TestDiv

# 创建2个套件，每个套件使用一个线程去执行
suite1 = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
suite2 = unittest.defaultTestLoader.loadTestsFromTestCase(TestSubs)
suite3 = unittest.defaultTestLoader.loadTestsFromTestCase(TestMul)
suite4 = unittest.defaultTestLoader.loadTestsFromTestCase(TestDiv)


def work1():
    """执行套件1"""
    unittest.TextTestRunner().run(suite1)


def work2():
    """执行套件2"""
    unittest.TextTestRunner().run(suite2)


def work3():
    """执行套件2"""
    unittest.TextTestRunner().run(suite3)


def work4():
    """执行套件2"""
    unittest.TextTestRunner().run(suite4)


t1 = threading.Thread(target=work1)
t2 = threading.Thread(target=work2)
t3 = threading.Thread(target=work3)
t4 = threading.Thread(target=work4)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
