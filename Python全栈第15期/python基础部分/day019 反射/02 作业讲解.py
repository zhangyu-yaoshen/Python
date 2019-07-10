# class UserInfo(object):
#     pass
#
# class Department(object):
#     pass
#
# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
# class RoleConfig(StarkConfig):
#
#         def changelist(self, request):
#             print(666, self.num)
#
# class AdminSite(object):
#         def __init__(self):
#             self._registry = {}
#         def register(self, k, v): # k:UserInfo,  v:StarkConfig
#             self._registry[k] = v(k)
#
# # site = AdminSite()
# # site.register(UserInfo, StarkConfig) # {UserInfo:StarkConfig(Userinfo)}
# # site.register(Department, RoleConfig) # {UserInfo:StarkConfig(Userinfo), Department:RoleConfig(Department)}
# #
# # for k, row in site._registry.items():
# #     row.run()


class UserInfo(object):
    pass


class Department(object):
    pass


class StarkConfig(object):

    def __init__(self, num):
        self.num = num

    def get_vals(self):
        v = [11, 22, 33]
        extra = self.extra_vals()
        if extra:
            v.extend(extra)
        return v

    def extra_vals(self):
        pass

    def run(self):
        return self.get_vals()


class RoleConfig(StarkConfig):

    def extra_vals(self):
        return [99, 88]


class AdminSite(object):
    def __init__(self):
        self._registry = {}

    def register(self, k, v):
        self._registry[k] = v(k)


site = AdminSite()
site.register(UserInfo, StarkConfig)
site.register(Department, RoleConfig)  # {UserInfo:StarkConfig(Userinfo), Department:RoleConfig(Department)}
for k, row in site._registry.items():
    print(row.run())
# StarkConfig(Userinfo).run()
# RoleConfig(Department).run()
