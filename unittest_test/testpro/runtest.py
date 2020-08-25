import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os 

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ===============定义发送邮件===============
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.ioa365.com")
    smtp.login('zena.huang@ioa365.com','Ybg654321')
    smtp.sendmail('zena.huang@ioa365.com','zena.huang@ioa365.com',msg.as_string()) # msgRoot或msg
    smtp.quit()
    print("email has send out!")

# ==============查找测试报告目录，早到最新生成的测试报告文件==============
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report+"//"+fn))
    file_new = os.path.join(test_report,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    test_dir = 'F:/selenium2_autotest/unittest_test/testpro/test_case'
    test_report = 'F:/selenium2_autotest/unittest_test/testpro/report'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S") #获取当前时间，将时间格式化为字符串
    filename= test_report +'//'+ now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description='用例执行情况')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report) # 发送测试报告

    
   




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
'''
# 使用unittst的defaultTestLoader类的discover()方法
# discover(start_dir,pattern='test*.py',top_level_dir=None)

discover = unittest.defaultTestLoader.discover('F:/selenium2_autotest/unittest_test/testpro/test_case','test*.py')
'''
'''
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
'''

'''
# 定义报告存放路径
now = time.strftime("%Y-%m-%d %H_%M_%S") #获取当前时间，将时间格式化为字符串
file_path = 'F:/selenium2_autotest/unittest_test/testpro/report/' + now + 'result.html'


with open(file_path, "wb") as f:
    runner = HTMLTestRunner(stream=f, title="百度测试报告", description='用例执行情况')
    runner.run(discover)
'''