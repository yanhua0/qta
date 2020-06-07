from testbase import TestCase


class LogErrorTest(TestCase):
    '''异常测试
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    timeout = 1

    def run_test(self):
        #---------------------------
        self.start_step("异常测试")
        #---------------------------
        self.fail("异常发生")

if __name__ == '__main__':
    LogErrorTest().debug_run()