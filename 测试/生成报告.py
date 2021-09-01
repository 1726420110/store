# 加载测试用例的方法：discover（迪斯卡瓦）方法
import os
import unittest
from unittestreport import TestRunner

# os.path.abspath(__file__)
# 测试用例，使用绝对路径加载测试用例，使用 r 进行转码

one_suite = unittest.defaultTestLoader.discover(os.getcwd(), pattern="Test2.py")

# 执行用例
# 1.需要创建执行器对象，使用 unittest 当中的 TestRunner（译：泰斯特.软那儿）
"""
:param suites: 测试套件
:param filename: 报告文件名
:param report_dir:报告文件的路径
:param title:测试套件标题
:param templates: 可以通过参数值1或者2，指定报告的样式模板，目前只有两个模板
:param tester:测试者
"""
one_runner = TestRunner(one_suite,
                        filename="计算机报告.html",
                        report_dir=r"C:\Users\Administrator\PycharmProjects\pythonProject\测试",
                        title="演示用例运行产生的测试报告",
                        tester="守护",
                        desc="第一个报告",
                        templates=1
                        )
# 2.运行套件
one_runner.run()
