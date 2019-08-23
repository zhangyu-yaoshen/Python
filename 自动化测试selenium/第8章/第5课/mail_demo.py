#coding=utf-8
import smtplib
from email.mime.text import MIMEText 
from email.header import Header

#发件人
sender = "waitforxy@126.com"
#收件人
receiver = "waitfordev@126.com"

#不用密码发送，而是用授权码
auth_code = "xdclass123"

#主题
subject = "自动化测试报告"

#定义发送内容
msg = MIMEText("<html> <h2>欢迎来到小D课堂</h2></html>",_subtype="html",_charset="utf-8")
#主题
msg["Subject"] = subject
#设置发信人
msg["from"] = sender
#设置收信人
msg["to"] = receiver

#定义邮箱服务器
smtp = smtplib.SMTP()
#定义邮箱
smtp.connect("smtp.126.com")
#登录配置【账号加授权码】
smtp.login(sender,auth_code)
#发送邮件【发件人；收件人；发送内容；】
smtp.sendmail(sender, receiver, msg.as_string())
#关闭邮箱
smtp.quit()