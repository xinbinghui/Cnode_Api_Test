from common.Request import RequestsHandler
from conf.conf import *
from common.Assert import Assertions
from common import Consts
from common.Yaml_Data import HandleYaml
import pytest
import sys
import os
from common.Logs import Log

file_name = os.path.basename(sys.argv[0])
log = Log(file_name)
logger = log.Logger

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_hasnot_read_message.yaml'))
def test_hasnot_read_message(caseinfo):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assertions(def_name)
    logger.info("开始执行脚本%s",def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url']
    data = {}
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,params=data)
    test_assert.assert_body(json_response,'success',caseinfo['vaildate'])
    Consts.RESULT_LIST.append('pass')

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_messages.yaml'))
def test_messages(caseinfo):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assertions(def_name)
    logger.info("开始执行脚本%s",def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url']
    data = caseinfo['request']['data']
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,params=data)
    test_assert.assert_body(json_response,'success',caseinfo['vaildate'])
    Consts.RESULT_LIST.append('pass')