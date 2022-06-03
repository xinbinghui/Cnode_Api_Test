from common.Request import RequestsHandler
from common import Consts
from common import Assert
from common.Yaml_Data import HandleYaml
from conf.conf import *
from common.Logs import Log
import pytest
import sys
import os

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_user_detail.yaml'))
def test_user_detail(caseinfo):
    # 获取当前函数的名称
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url'] + caseinfo['loginname']
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url)
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')
    # print(Consts.RESULT_LIST)

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_user_accesstoken.yaml'))
def test_user_accesstoken(caseinfo):
    # 获取当前函数的名称
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url']
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,data=caseinfo['request']['data'])
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')