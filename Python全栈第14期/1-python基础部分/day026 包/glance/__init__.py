# from glance import api, cmd, db
from . import api, cmd, db # 必须在外面启动
__all__ = ["money"]
print("glance__init")
money = 5000

def hello():
    print("hello")



