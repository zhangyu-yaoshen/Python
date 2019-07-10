import struct
num = 156
#将int类型的数据打包成4个字节的数据
num_stru = struct.pack('i',num)
print(len(num_stru))
print(num_stru)
print('11111111111111111111111111111111')

#在通过int类型解包,将前面打包的数据解包成打包之前的int数据
num2 = struct.unpack('i',num_stru) #解包出来是个元组
print(num2)#(156,)
print(num2[0])










