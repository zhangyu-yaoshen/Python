class User:
    def __init__(self, id, nick_name, login_name, login_psw, real_name, card, phone, address, email):
        self.id = id
        self.nick_name = nick_name
        self.login_name = login_name
        self.login_psw = login_psw
        self.real_name = real_name
        self.card = card
        self.phone = phone
        self.address = address
        self.email = email
        self.order_list = []



class Order:
    #  订单编号, 流⽔号, 所属⽤户编号, 收货地址. 邮费. 订单状态(0:发货, 1:收货, 2: 退货), 评价编号.
    def __init__(self, id, liushui,  address, user, pingjia, youfei=0.00, order_status=0):
        self.order_detail_list = []
        pass

# 信息: 评价编号, 评价分数, 评价内容, 评价显⽰(0:显⽰, 1:不显⽰), 评价
# 类型(1: 物流评价, 2: 服务评价, 3: 商品评价)
class PingJia:
    def __init__(self, id, score, content, pingjia_status, isShow=0):
        pass

# 明细编号, ⼩流⽔号, 商品购买时价格, 购买数量. 商品编号
class OrderDetail:
    def __init__(self, id, xiaoliushui, price, num, product, order):
        pass

# 商品编号, 商品名称, 商品描述, 商品价格, 商品库存
class Product:
    def __init__(self, id, name, desc, price, store):
        pass

