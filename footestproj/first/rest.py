from testbase.testcase import TestCase
from testbase import logger
# from testbase.testcase import RepeatTestCaseRunner
from study.RepeatTestCaseRunner import RepeatTestCaseRunner
import requests, json


def send(url, data):
    dict = []

    for _ in data:
        dict.append({"s": _})
    data = json.dumps(dict)
    print("data=" + data)
    r = requests.get(url, data)
    return r


class EnvTest3(TestCase):
    '''环境构造测试
    '''
    owner = "zjl"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.High
    timeout = 1
    case_runner = RepeatTestCaseRunner()
    repeat = 4

    def pre_test(self):
        logger.info("注册xxx")

    def run_test(self):
        url = "http://localhost/rpc"
        list = [0, 1, 2]
        res = send(url, list)
        if res.status_code != 200:
            logger.error("服务错误")
        dict_json = json.loads(res.content.decode())
        pass

    def post_test(self):
        logger.info("清楚xxx")


if __name__ == '__main__':
    EnvTest3().debug_run()
