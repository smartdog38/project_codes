# 集合元素必须可哈希，不可变
# 如 tuple，int，str，float

set_1 = {1,2,3,4,5}
set_2 = {'a','b','c'}
set_3 = {1,'a',2}
set_4 = set(i for i in range(10)) # 0-9
set_5 = set(i for i in range(10) if i%2==0) # 0,2,4,6,8
print(set_0)
print(set_1)
print(set_2)
print(set_3)
print(set_4)
print(set_5)

# 转换为集合
s = 'abc'
l = [1,2,3]
d = {'a':1,'b':2}
st = {1,2,3}
set(s)
set(l)
print(set(d)) # {'a', 'b'}
set(st)

# 函数
set_1.add(1) # 添加元素
set_1.remove(1) # 删除元素 1 ，没有会报错
set_1.discard(1)  # 删除元素 1 ，没有不报错
set_1.pop() # 删除第一个元素
set_1.clear() # 清空

set_1.difference(set_2)  # set_1 与 set_2 的差集
set_1.intersection(set_2)  # set_1 与 set_2 的交集
set_1.union(set_2)  # set_1 与 set_2 的并集

