"""
封装发送邮件的方法
"""
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from common.Logs import Log
import os
import sys
from common import Consts
import time



my_sender = 'allan0706@sina.cn'
my_passwd = '2c3921efe562cd83'
my_user = '917042025@qq.com'
my_stmp_host = 'smtp.sina.cn' # 163的stmp服务器地址

file_name = os.path.basename(sys.argv[0])
log = Log(file_name)
logger = log.Logger

def mail():
    try:
        # 开始打包邮件
        msg = MIMEMultipart()
        msg['From'] = my_sender
        msg['To'] = my_user
        msg['Subject'] = 'cnode接口测试报告'

        result_body = Consts.RESULT_LIST
        len_result = len(result_body)
        T = 0
        F = 0
        Error = 0
        for r in result_body:
            if r == 'pass':
                T = T+1
            if r == 'fail':
                F = F+1
        if T + F == len_result:
            pass
        else:
            Error = len_result - T - F

        rate = (float(T) / float(len_result) * 100)
        content = 'Hi，all\n本次接口自动化报告如下：\n' + '执行时间：' + time.ctime() + '\n' + '执行脚本数为：' + str(len_result) + '，成功数为：' + str(T) + '，失败数为：' + str(F) + '，异常数为：' + str(Error) + '\n通过率为：' + str(rate) + '%'
        text = MIMEText(content)
        msg.attach(text)

        xlsxpart = MIMEApplication(open(os.getcwd() + '/report/reporthtml/index.html', 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', file_name='index.html')
        msg.attach(xlsxpart)

        server = smtplib.SMTP(my_stmp_host, 25)
        # server.set_debuglevel(1)
        logger.info("开始发送邮件")
        server.login(my_sender,my_passwd)
        server.sendmail(my_sender,[my_user],msg.as_string())
        server.quit()
        logger.info("邮件发送成功，详见内容结果")
    except Exception as e:
        logger.error("邮件发送失败，详见日志分析原因", e)
        print("邮件发送失败，详见日志分析原因", e)