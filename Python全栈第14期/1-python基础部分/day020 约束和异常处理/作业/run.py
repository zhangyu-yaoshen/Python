import handler

def func():
    objs = []
    name_list = dir(handler)
    # 去掉__
    new_lst = []
    for el in name_list:
        if el.startswith("__") and el.endswith("__"):
            new_lst.append(el)
    for el in new_lst:
        name_list.remove(el)

    # filter() => isinstance

    base_sub_list = []
    for name in name_list:
        cls = getattr(handler, name)
        if issubclass(cls, getattr(handler, "Base")) and cls != getattr(handler, "Base"):
            base_sub_list.append(cls())

    print(base_sub_list)

if __name__ == '__main__':
    func()
