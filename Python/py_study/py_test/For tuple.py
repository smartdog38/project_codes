tuple_1 = (1,2,3,)
tuple_2 = ('a','b','c',)
tuple_3 = (1,'a',2,)
tuple_4 = tuple(i for i in range(10)) # 0-9，与列表不同，需要加上tuple
tuple_5 = tuple(i for i in range(10) if i%2==0)  # 0,2,4,6,8,加上条件
print(tuple_1)
print(tuple_2)
print(tuple_3)
print(tuple_4)
print(tuple_5)

# 转换为元组
s = 'abc'
l = [1,2,3]
d = {'a':1,'b':2}
st = {1,2,3}
tuple(s)
tuple(l)
tuple(d)
tuple(st)

# 元组的函数
tuple_1.index(1)
tuple_1.count(1)

# 切片
tuple_1[0:2]
tuple_1[0:]
tuple_1[:2]
tuple_1[0]

# 解包
tuple_a = (1,2,3,4,5,6,)
a,*b,c = tuple_a # *b a 得到第一个元素，c 得到最后一个元素，b得到剩下的元素，以列表形式
print(a,b,c) # 1 [2,3,4,5] 6