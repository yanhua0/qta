import time

import form as form
from testbase.retry import Retry
from testbase.testcase import TestCase


def string_combine(param, param1):
    return param + param1


class StrCombineTest(TestCase):
    '''测试字符串拼接接口
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    timeout = 1

    def run_test(self):
        # ---------------------------
        self.start_step("测试字符串拼接")
        # ---------------------------
        result = string_combine("xxX", "yy")
        self.assert_("检查string_combine调用结果", result == "xxXyy9")


if __name__ == '__main__':
    for w in Retry(timeout=2, interval=0.5, raise_error=False):

        print(w)
# StrCombineTest().debug_run()
