"""
动态调用本地接口还是服务端接口
"""

def server_ip(env):
    """
    dev_ip 开发环境地址
    sit_ip 测试环境服务器地址
    """
    if env == 'test':
        server_ip = 'http://106.12.126.197'
        return server_ip
    if env == 'realse':
        server_ip = 'http://47.100.175.62:3000/api/v1'
        return server_ip
    else:
        print("get environment ip error")