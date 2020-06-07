# -*- coding: utf-8 -*-
'''
一个用例重复执行
'''

from testbase import TestCase

from study.RepeatTestCaseRunner import RepeatTestCaseRunner

'''
多次执行
'''


class RepeatTest(TestCase):
    '''测试示例
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    timeout = 1
    priority = TestCase.EnumPriority.Normal
    case_runner = RepeatTestCaseRunner()
    repeat = 5

    def run_test(self):
       pass


if __name__ == '__main__':
    RepeatTest().debug_run()
