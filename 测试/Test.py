import unittest
from concurrent.futures.thread import ThreadPoolExecutor
from testAdd import TestAdd
from testSubs import TestSubs
from testMul import TestMul
from testDiv import TestDiv


def run_test(suite, thread_count=1):
    """
    多线程执行用例的方法
    :param suite: 测试套件
    :param thread_count: int  ---->执行的线程数量，默认为1
    :return: TestResult--->测试结果
    """
    res = unittest.TestResult()
    # 创建一个线程池，执行测试用例
    with ThreadPoolExecutor(max_workers=thread_count) as ts:
        for case in suite:
            # 将用例的执行任务提交到线程池中
            ts.submit(case.run, result=res)
    return res


if __name__ == '__main__':
    # 创建两个套件
    suite1 = unittest.defaultTestLoader.loadTestsFromTestCase(TestAdd)
    suite2 = unittest.defaultTestLoader.loadTestsFromTestCase(TestSubs)
    suite3= unittest.defaultTestLoader.loadTestsFromTestCase(TestMul)
    suite4 = unittest.defaultTestLoader.loadTestsFromTestCase(TestDiv)
    # 给根据套件的数量，每个套件创建一个线程去执行
    res1 = run_test(suite=suite1, thread_count=1)
    res2 = run_test(suite=suite2, thread_count=1)
    res3 = run_test(suite=suite3, thread_count=1)
    res4 = run_test(suite=suite4, thread_count=1)

    # 打印测试结果
    print(res1,res2,res3,res4)
