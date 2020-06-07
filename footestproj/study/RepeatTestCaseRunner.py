from testbase.testresult import TestResultCollection
from testbase.testcase import ITestCaseRunner, TestCaseRunner


class RepeatTestCaseRunner(ITestCaseRunner):

    def run(self, testcase, testresult_factory):
        passed = True
        results = []
        for _ in range(testcase.repeat):
            self.logInfo('第%s次测试执行' % _)
            result = TestCaseRunner().run(testcase, testresult_factory)
            results.append(result)
            passed &= result.passed
            if not passed:  # 有一次执行不通过则中止执行
                break
        return TestResultCollection(results, passed)

    def logInfo(self, param):
        print(param)
