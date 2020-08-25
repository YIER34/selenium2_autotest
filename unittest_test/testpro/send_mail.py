# 自动发邮件功能
# SMTP(Simple Mail Transfer Protocol) 简单邮件传输协议
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# 发送邮箱服务器
smtpserver = 'smtp.ioa365.com'
# 发送邮箱用户/密码
user = 'zena.huang@ioa365.com'
password = 'Ybg654321'
# 发送邮箱
sender ="zena.huang@ioa365.com"
# 接送邮箱
receiver = "zena.huang@ioa365.com"
# 发送邮件主题
subject = 'Python email test'

# 可选发送的附件
sendfile = open('F:/selenium2_autotest/unittest_test/testpro/report/log.txt','rb').read()
att = MIMEText(sendfile,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="log.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>您好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string()) # msgRoot或msg
smtp.quit()