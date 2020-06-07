import sys

from testbase.testcase import TestCase
from testbase import logger

class HelloTest(TestCase):
    '''第一个测试用例
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.High
    timeout = 1
    tags = "Demo"

    def run_test(self):
        # ---------------------------
        self.start_step("第一个测试步骤")
        # ---------------------------
        self.log_info("hello")
        logger.error("错误")


if __name__ == '__main__':

    HelloTest().debug_run()
