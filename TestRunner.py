import unittest
from HTMLTestRunner import HTMLTestRunner
import time

if __name__ == '__main__':
    # 指定批量执行的模块
    test_module = './test_case/'
    discover = unittest.defaultTestLoader.discover(test_module, pattern="test*.py")

    # 报告存放的文件夹
    dir_path = './test_report/'
    # 报告命名加上时间格式化
    now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    # 报告绝对路径
    report_path = dir_path + now + ' result.html'
    # 打开文件，写入测试结果
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner(stream=f, verbosity=2, title='Math测试报告', description='用例执行详细信息')
        runner.run(discover)
    f.close()
