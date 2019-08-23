"""
问：1234能组成多少个不重复不相同的三位数？
"""

# from collections import deque
# from functools import reduce, partial
from itertools import permutations, chain  # 排列s  Python Cook Book

ret = permutations('1234', 3)
print(list(ret))


list1 = [11, 22, 33]
list2 = ['aa', 'bb', 'cc']

for i in chain(list1, list2):
    print(i)
