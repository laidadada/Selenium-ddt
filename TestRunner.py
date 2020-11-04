# coding:utf-8

import unittest, time, HTMLTestRunner
from config.globalparameter import test_case_path, report_name

# 构建测试集,包含Selenium-ddt/test_case目录下的所有以test开头的.py文件
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test_*.py')

# 执行测试
if __name__ == '__main__':
    report = report_name + "Report.html"
    fb = open(report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title=u'猿盟自动化测试报告',
        description=u'项目描述：开发环境'
    )
    runner.run(suite)
    fb.close()
