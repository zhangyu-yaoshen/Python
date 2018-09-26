
import subprocess
import requests
#执行命令模块subprocess；发送数据模块requests

# pip3 install requests

# ################## 采集数据 ##################
# result = subprocess.getoutput('ipconfig')
# result正则处理获取想要数据

# 整理资产信息
# data_dict ={
#     'nic': {},
#     'disk':{},
#     'mem':{}
# }

# ##################  发送数据 ##################
# requests.post('http://www.127.0.0.1:8000/assets.html',data=data_dict)