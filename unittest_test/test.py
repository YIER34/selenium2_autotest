# 测试两个整数相加
from calculator import Count
import unittest

# 如果每个用例都需要相同的setUp()和tearDown(),可以封装为单独的测试类
class MyTest(unittest.TestCase):
    def setUp(self):
        print("test start")
    def tearDown(self):
        print("test end")


class TestAdd(MyTest):
    # def setUp(self):
    #     print("test start")
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)
    # def tearDown(self):
    #     print("test end")

class TestSub(MyTest):
    # def setUp(self):
    #     print("test start")
    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)
    def test_sub2(self):
        j = Count(71,46)
        self.assertEqual(j.sub(),25)
    # def tearDown(self):
    #     print("test end")



# __name__表示调用方式，__main__表示直接调用
if __name__ == '__main__':
    unittest.main() # main()使用TestLoader类来搜索所有包含在该模块中以test命名开头的测试方法，并自动执行它们

'''   
# 执行测试类的测试方法
mytest = TestCount()
mytest.test_add()
'''
'''
if __name__ == '__main__':
    # 去掉main()方法，采用构造测试集的方法来加载与运行测试用例，实现有选择地执行测试用例
    # 构造测试集,添加测试用例
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
'''