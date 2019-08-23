# class JiaoFu:
#     def qd(self):
#         print("教父带你祈祷")
# class Fu:
#     def msj(self):
#         print("alex喜欢msj")
#
# class Zi(Fu, JiaoFu):
#     def dbj(self):
#         print("刘伟喜欢大宝剑")
#
# z = Zi()
# z.msj()
# z.dbj()
# z.qd()

#
# class Base1: # Base1 object
#     def func(self):
#         print("娃哈哈")
#
#
# class Base2:
#     def func(self):
#         print("雪碧")
#
# class Foo(Base1, Base2): # Foo, Base1, Base2
#     pass
#
# f = Base1()
# f.func() # 雪碧, 娃哈哈

# class A:
#     pass
#
# class B:
#     pass
#
# class C:
#     pass
#
# class D:
#     pass
#
# class E(A, C):
#     pass
#
# class F(B, D):
#     pass
#
# class G(E, F):
#     pass


# GEACFBD #


# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B, C):
#     pass
# class E(C, A):
#     pass
# class F(D, E):
#     pass
# class G(E):
#     pass
# class H(G, F):
#     pass
# print(H.__mro__)
# H的MRO: ??
# 拆
# L(H)= H + L(G) + L(F) -> H + (GECA) + (FDBECA) -> HGFDBECA (MRO)

# L(G) = G + L(E) -> G +(ECA) -> GECA
# L(F) = F + L(D) + L(E) -> F +(DBCA) + (ECA) -> FDBECA

# L(E) = E +  L(C) + L(A) -> E + (CA) + A -> ECA
# L(D) = D + L(B)+ L(C)  -> D + (BA) + (CA) -> DBCA

# L(c) = C + A  CA
# L(B) = B + A  BA

# L(A) = A

# 合
# + merge((B,), (A, ), 元组......)
#




# '''
# merge((a, b, e), ( a, b, e))
# '''
#
#
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass
class E(C, A):
    pass
class F(D, E):
    pass
class N:
    pass
class O:
    pass
class M(N, O):
    pass
class G(E, M):
    pass
class H(G, F):
    pass
#
print(H.__mro__)
#
# # H的MRO
# '''
# L(H) = H + L(G) + L(F) -> H + (MNO) + () -> H G F D B E C A M N O
#
# L(G) = G + L(E) + L(M)  -> G + (ECA) + (MNO) -> GECAMNO
# L(F) = F + L(D) + L(E)  -> F + (DBCA) + (ECA) -> FDBECA
#
# L(E) = E + (CA) + A -> ECA
# L(M) = M + N + O  -> MNO
# L(D) = D + (BA) + (CA) -> DBCA
#
# 1. 面试
# 2. 装逼
# 3. 考试
#
# H G F D B E C A M N O
# '''



