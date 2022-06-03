from common import Consts
from common.Request import RequestsHandler
from conf.conf import *
from common import Assert
from common.Return_Reponse import dict_style
from common.Yaml_Data import HandleYaml
import pytest
import sys
import os
from common.Logs import Log

file_name = os.path.basename(sys.argv[0])
log = Log(file_name)
logger = log.Logger

# @pytest.fixture(scope='module')
# def topic_id():
#     opera_url = server_ip('realse') + '/topics'
#     data = {
#         "accesstoken": HandleYaml().read_extract_yaml('access_token'),
#         "title": "创建topic_id",
#         "tab": "job",
#         "content": "创建topic_id"
#     }
#     opera_result = RequestsHandler().post_req(opera_url,data=data)
#     topic_id = opera_result.json()['topic_id']
#     return topic_id

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_collect_topic.yaml'))
def test_collect_topic(caseinfo):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s",def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url']
    data = {}
    data['topic_id'] = HandleYaml().read_extract_yaml('topic_id')
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,data=data)
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_decollect_topic.yaml'))
def test_decollect_topic(caseinfo):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s",def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url']
    data = {}
    data['topic_id'] = HandleYaml().read_extract_yaml('topic_id')
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,data=data)
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_all_collect.yaml'))
def test_all_collect(caseinfo):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s",def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url'] + caseinfo['loginname']
    opera_result = RequestsHandler().get_req(opera_url)
    sting_response = opera_result.content.decode()
    json_response = dict_style(sting_response)
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')