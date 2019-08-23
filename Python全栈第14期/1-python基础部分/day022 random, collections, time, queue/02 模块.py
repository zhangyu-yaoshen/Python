class Animal:
    pass

from collections import Iterable, Iterator
lst = []
print(isinstance(lst, Iterable))   #  True
print(isinstance(lst, Iterator))   # False
