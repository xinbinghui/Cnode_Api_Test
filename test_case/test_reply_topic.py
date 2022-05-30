from common.Request import RequestsHandler
from common.Yaml_Data import HandleYaml
from conf.conf import *
from common import Consts
from common import Assert
import pytest
from string import Template
import yaml
import os
from common.Logs import Log
import sys

file = os.path.basename(sys.argv[0])
log = Log(file)
logger = log.Logger

# @pytest.fixture(scope='module')
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

@pytest.fixture(scope='module')
def opera_url():
    with open(os.getcwd() + '\\test_data\\test_reply_topic.yaml',encoding='utf-8') as f:
        read_yaml_str = f.read()
        topic_id = HandleYaml().read_extract_yaml('topic_id')
        data = Template(read_yaml_str).safe_substitute({"url": f"/topic/{topic_id}/replies"})
    opera_url = server_ip('realse') + yaml.safe_load(data)[0]['request']['url']
    return opera_url


# @pytest.fixture(scope='module')
# def reply_id(opera_url):
#     data = {
#         "accesstoken": HandleYaml().read_extract_yaml('access_token'),
#         "content": "创建reply_id"
#     }
#     opera_result = RequestsHandler().post_req(opera_url,data=data)
#     assert opera_result.status_code == 200
#     reply_id = opera_result.json()['reply_id']
#     return reply_id

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_reply_topic.yaml'))
def test_reply_topic(caseinfo,opera_url):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s:", def_name)
    data = caseinfo['request']['data']
    if caseinfo['reply'] == 1:
        data['reply_id'] = HandleYaml().read_extract_yaml('reply_id')
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,data=data)
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')

@pytest.mark.parametrize('caseinfo',HandleYaml().read_testcase_yaml('test_reply_ups.yaml'))
def test_reply_ups(caseinfo):
    def_name = sys._getframe().f_code.co_name
    test_assert = Assert.Assertions(def_name)
    logger.info("开始执行脚本%s",def_name)
    opera_url = server_ip('realse') + caseinfo['request']['url'] + HandleYaml().read_extract_yaml('reply_id') + '/ups'
    data={}
    data['accesstoken'] = HandleYaml().read_extract_yaml('access_token')
    json_response = RequestsHandler().json_req(caseinfo['request']['method'],opera_url,data=data)
    test_assert.assert_body(json_response,'success',caseinfo['validate'])
    Consts.RESULT_LIST.append('pass')