# -*- coding: utf-8 -*-
'''ʾ����������
'''
#2020/06/06 QTAF�Զ�����

from foolib.testcase import FooTestCase

class HelloTest(FooTestCase):
    '''ʾ����������
    '''
    owner = "Administrator"
    timeout = 5
    priority = FooTestCase.EnumPriority.High
    status = FooTestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
if __name__ == '__main__':
    HelloTest().debug_run()
