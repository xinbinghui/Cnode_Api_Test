"""封装request"""
import requests
import logging

class RequestsHandler:
    def get_req(self,url,params=None,**kw):
        """封装一个get方法，发送get请求"""
        # 当处理不成功时，比如url地址输入方式错误，或者接口超时timeout，需要抛出一个异常
        try:
            res = requests.get(url=url,params=params,**kw)
        except TimeoutError:
            #记录日志信息，放入logger里面，这样我们就能知道问题出在哪里
            logging.error('访问不成功')
        else:
            return res

    def post_req(self,url,data=None,json=None,**kw):
        """封装一个post方法，发送post请求"""
        # 当处理不成功时，比如url地址输入方式错误，或者接口超时timeout，需要抛出一个异常
        try:
            res = requests.post(url=url,data=data,json=json,**kw)
        except TimeoutError:
            #记录日志信息，放入logger里面，这样我们就能知道问题出在哪里
            logging.error('访问不成功')
        else:
            return res

    def vist_req(self,method,url,params=None,data=None,json=None,**kw):
        """访问接口"""
        # 如果传输进来的是大写，可以使用lower方法
        if method.lower() == 'get':
            return self.get_req(url,params=params,**kw)
        elif method.lower() == 'post':
            return self.post_req(url,data=data,json=json,**kw)
        else:
            return requests.request(method,url,**kw)

    def json_req(self,method,url,params=None,data=None,json=None,**kw):
        """访问接口，获取json数据"""
        res = self.vist_req(method,url,params=params,data=data,json=json,**kw)
        try:
            return res.json()
        except:
            logging.error('不是json格式的数据')