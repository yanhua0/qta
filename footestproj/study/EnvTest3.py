from testbase.testcase import TestCase


def _add_host(param, param1):
    pass


def _del_host(param, param1):
    pass


class EnvTest3(TestCase):
    '''环境构造测试
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    timeout = 1

    def pre_test(self):
        _add_host("www.qq.com", "11.11.12.12")
        super(EnvTest3, self).pre_test()

    def run_test(self):
        # main test logic
        # ...
        pass

    def post_test(self):
        super(EnvTest3, self).post_test()
        _del_host("www.qq.com", "11.11.12.12")


if __name__ == '__main__':
    EnvTest3().debug_run()
