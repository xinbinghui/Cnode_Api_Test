import yaml
import os

class HandleYaml:
    # def __init__(self,file_path=None):
    #     if file_path:
    #         self.file_path = file_path
    #     else:
    #         root_dir = os.path.dirname(os.path.abspath('.'))
    #         # os.path.abspath('.')表示获取当前文件所在的目录；os.path.dirname表示获取文件所在的父目录；所以整个就是项目所在的路径
    #         self.file_path = root_dir + '\\api_rili\\test_data\\test_yaml_data.yaml' # 获取文件所在的相对路径（相对整个项目）

    # def get_data(self):
    #     with open(self.file_path,mode='r',encoding='utf-8') as f:
    #         data = yaml.load(stream=f,Loader=yaml.FullLoader)
    #         yaml.warnings({'YAMLLoadWarning':False})
    #         return data

    # 读取测试用例的yaml文件
    def read_testcase_yaml(self,yaml_name):
        # return (os.getcwd() + '\\test_data\\' + yaml_name)
        with open(os.getcwd() + '\\test_data\\' + yaml_name,mode='r',encoding='utf-8') as f:
            data = yaml.load(stream=f,Loader=yaml.FullLoader)
            yaml.warnings({'YAMLLoadWarning':False})
            return data

    # 读取extract.yaml文件
    def read_extract_yaml(self,key):
        with open(os.getcwd() + '\\extract.yaml',mode='r',encoding='utf-8') as f:
            data = yaml.load(stream=f,Loader=yaml.FullLoader)
            return data[key]
    
    # 写入extract.yaml文件
    def write_extract_yaml(self,data):
        with open(os.getcwd() + '\\extract.yaml',mode='a',encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    # 清除extract.yaml文件
    def clear_extract_yaml(self):
        with open(os.getcwd() + '\\extract.yaml',mode='w',encoding='utf-8') as f:
            f.truncate()
