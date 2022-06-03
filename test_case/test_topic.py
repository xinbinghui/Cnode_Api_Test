from asyncio.log import logger
from common.Request import RequestsHandler
from common.Yaml_Data import HandleYaml
from conf.conf import *
from common import Consts
from common import Assert
from common.Logs import Log
import pytest
import sys
import os
import allure

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger

@allure.description("测试http://47.100.175.62:3000/api/v1/topics接口")
@allure.testcase("http://47.100.175.62:3000/api/v1/topics","测试用例地址")
@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_get_topic.yaml'))
def test_get_topic(caseinfo):
    # 获取当前函数的名称
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url']
    json_reponse = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,params=caseinfo['params'])
    test_assert.assert_body(json_reponse,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')

# @pytest.fixture
# def topic_id():
#     opera_url = server_ip('realse') + '/topics'
#     data = {
#         "accesstoken": HandleYaml().read_extract_yaml('access_token'),
#         "title": "创建topic_id",
#         "tab": "ask",
#         "content": "创建topic_id"
#     }
#     opera_result = RequestsHandler().post_req(opera_url,data=data)
#     assert opera_result.status_code == 200
#     topic_id = opera_result.json()['topic_id']
#     return topic_id

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_topic_detail.yaml'))
def test_topic_detail(caseinfo):
    # 获取当前函数的名称
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url'] + HandleYaml().read_extract_yaml('topic_id')
    data = caseinfo['params']
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,params=data)
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_create_topic.yaml'))
def test_create_topic(caseinfo):
    # 获取当前函数的名称
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url']
    data = caseinfo['request']['data']
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],url=opera_url,data=data)
    # json_response= opera_result.json()
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_edit_topic.yaml'))
def test_eidt_topic(caseinfo):
    # 获取当前函数的名称
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url']
    data = caseinfo['request']['data']
    data['topic_id'] = HandleYaml().read_extract_yaml('topic_id')
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,data=data)
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')