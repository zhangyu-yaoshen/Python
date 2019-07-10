# def create_resource(conf):
#     print('from version.py: ',conf)

# sys.path
# 在包内使用相对路径. 你的启动脚本就不能在这个包下, 在包外面使用时没有问题
from ..cmd import manage
manage.main()