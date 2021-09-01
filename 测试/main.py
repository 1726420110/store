import unittest
from HTMLTestRunner import HTMLTestRunner
import os

# 加载所有用例
tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="test*.py")

# 创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器的测试报告",
    description="计算器的加法和减法测试报告",
    verbosity=1,
    stream=open("计算器测试报告.html", mode="w+", encoding="utf-8")
)

# 运行
runner.run(tests)

# 任务1：使用多线程同时并发执行四个模块用例。Thread: run():
# 任务2：针对银行系统开户模块进行参数化测试
'''
    [
        ["jason","admin","cn","安徽省","桃园路","s001","05as1dfad",5000,1],
        ["jason","admin","cn","安徽省","桃园路","s001","05as1dfad",5000,2],
        ["",3]
    ]


'''
