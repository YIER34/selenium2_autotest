# fixtures
# setUpModule/tearDownModule  在整个模块的开始和结束被执行
# setUpClass/tearDownClass  在测试类的开始和结束被执行，需要用@classmethod来装饰，并传参cls
# setUp/tearDown  在测试用例的开始和结束被执行
import unittest

def setUpModule():
    print("test module start >>>>>>>>>>")
def tearDownModule():
    print("test module end >>>>>>>>>>>>")

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test class start =========>")
    @classmethod
    def tearDownClass(cls):
        print("test class end ===========>")
    
    def setUp(self):
        print("test case start -->")
    def tearDown(self):
        print("test case end -->")
    
    def test_case1(self):
        print("test case1")
    def test_case2(self):
        print("test case2")

if __name__ == '__main__':
    unittest.main()
