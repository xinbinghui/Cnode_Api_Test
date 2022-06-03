import pytest
import requests
import re
from common.Yaml_Data import HandleYaml
from conf.conf import *
from common.Request import RequestsHandler

@pytest.fixture(scope='session',autouse=True)
def conn_database():
    print('\n====连接数据库====')
    yield
    print('\n====关闭数据库====')

@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    HandleYaml().clear_extract_yaml()

@pytest.fixture(scope="session")
def session():
    return requests.Session()

@pytest.fixture(scope="session")
def user_session(session):
    """自动登录"""
    url = "http://47.100.175.62:3000/signin"
    body = {
        "name":"haha123",
        "pass":"123456"
    }
    resp = session.post(url=url,data=body)
    return session

@pytest.fixture(scope="session",autouse=True)
def get_accesstoken(user_session):
    url = "http://47.100.175.62:3000/setting"
    rep = user_session.get(url=url)
    accessToken = re.search('var accessToken = "(.*?)"',rep.text)[1]
    HandleYaml().write_extract_yaml({'access_token':accessToken})


@pytest.fixture(scope="session")
def topic_id():
    opera_url = server_ip('realse') + '/topics'
    data = {
        "accesstoken": HandleYaml().read_extract_yaml('access_token'),
        "title": "创建topic_id",
        "tab": "ask",
        "content": "创建topic_id"
    }
    opera_result = RequestsHandler().post_req(opera_url,data=data)
    assert opera_result.status_code == 200
    topic_id = opera_result.json()['topic_id']
    HandleYaml().write_extract_yaml({'topic_id':topic_id})
    return topic_id

@pytest.fixture(scope="session",autouse=True)
def reply_id(topic_id):
    # topic_id = HandleYaml().read_extract_yaml('topic_id')
    opera_url = server_ip('realse') + f'/topic/{topic_id}/replies'
    data = {
        "accesstoken": HandleYaml().read_extract_yaml('access_token'),
        "content": "创建reply_id"
    }
    opera_result = RequestsHandler().post_req(opera_url,data=data)
    assert opera_result.status_code == 200
    reply_id = opera_result.json()['reply_id']
    HandleYaml().write_extract_yaml({'reply_id':reply_id})