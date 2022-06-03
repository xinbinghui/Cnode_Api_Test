"""
封装assert方法
"""
from common import Consts
import json
from common.Logs import Log

class Assertions:
    def __init__(self,def_name):
        self.def_name = def_name
        log = Log(def_name)
        self.logger = log.Logger

    def assert_code(self,code,expected_code):
        """
        验证response状态码
        """
        try:
            assert code == expected_code
            self.logger.info("statusCode true, expected_code is %s, statusCode is %s" %(expected_code, code))
        except:
            self.logger.error("statusCode error, expected_code is %s, statusCode is %s" %(expected_code, code))
            Consts.RESULT_LIST.append('fail')
            raise
    
    def assert_body(self,body,body_msg,expected_msg):
        """
        验证response body中任意属性的值
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            self.logger.info("Response body msg == expected_msg, expected_msg is %s, body_message is %s" %(expected_msg, body[body_msg]))
        except:
            self.logger.error("Response body msg != expected_msg, expected_msg is %s, body_message is %s" %(expected_msg, body[body_msg]))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_in_text(self,body,expected_msg):
        """
        验证response body中是否包含预期字符串
        """
        try:
            text = json.dumps(body,ensure_ascii=False)
            assert expected_msg in text
            self.logger.info("Response body contain expected_msg, expected_msg is %s" %expected_msg)
        except:
            self.logger.error("Response body Does not contain expected_msg, expected_msg is %s" %expected_msg)
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_text(self,body,expect_msg):
        """
        验证response body中是否等于预期字符串
        """
        try:
            assert body == expect_msg
            self.logger.info("Response body == expected_msg, expected_msg is %s, body is %s" %(expect_msg, body))
        except:
            self.logger.error("Response body != expected_msg, expected_msg is %s, body is %s" %(expect_msg, body))
            Consts.RESULT_LIST.append('fail')
            raise
    
    def assert_time(self,time,expect_time):
        """
        验证response body 响应时间小于预期最大响应时间，单位：毫秒
        """
        try:
            assert time < expect_time
            self.logger.info("Response time < expected_time, expected_time is %s, time is %s" %(expect_time,time))
        except:
            self.logger.error("Response time > expected_time, expected_time is %s, time is %s" %(expect_time,time))
            Consts.RESULT_LIST.append('fail')
            raise
    
