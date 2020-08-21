import unittest
'''
# 加载测试文件
import testadd
import testsub

suite = unittest.TestSuite()
suite.addTest(testadd.TestAdd("test_add"))
suite.addTest(testadd.TestAdd("test_add2"))
suite.addTest(testsub.TestSub("test_sub"))
suite.addTest(testsub.TestSub("test_sub2"))

if __name__ == "__main__":

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
'''
# 使用unittst的defaultTestLoader类的discover()方法
# discover(start_dir,pattern='test*.py',top_level_dir=None)

discover = unittest.defaultTestLoader.discover('./','test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)