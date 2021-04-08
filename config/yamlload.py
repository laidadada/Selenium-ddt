# 用来读取yaml的数据

import yaml

def loadyaml(filename):
    files = open(filename, 'r', encoding='utf-8')
    #读取yaml文件
    data = yaml.load(files,Loader=yaml.FullLoader)
    return data

#测试
# a = loadyaml('../Cases_data/login_datas.yaml')
# # print(a)