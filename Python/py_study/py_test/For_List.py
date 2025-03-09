# 直接定义
list_1 = [1,2,3,4,5]
list_2 = ['a','b',"c",'''d''']
list_3 = [i for i in range(10)] # 0-9
list_4 = [i for i in range(10) if i%2==0] # 0,2,4,6,8,加上条件
list_5 = [i**2 for i in range(10) if i%2==0] # 0,2,4,6,8,加上条件
print(list_1)  # [1,2,3,4,5]
print(list_2)  # ['a','b','c',d']
print(list_3)  # [0,1,2,3,4,5,6,7,8,9]
print(list_4)  # [0,2,4,6,8]
print(list_5)   # [0,4,16,36,64]

# 转换为 list
s = "StRing"
t = (1,2,)
d = {'a':1,'b':2}
st = {12,1,2}
print(list(s))
print(list(t))
print(list(d))
print(list(st))

# 赋值
list_1[1] = 10

list_1.append(1) # 添加元素
list_1.extend(s) # 添加可迭代对象里的元素
list_1.insert(0,1) # 插入元素
list_1.pop() # 删除最后一个元素
list_1.pop(0) # 删除第一个元素
list_1.remove(1) # 删除第一个1
list_1.clear() # 清空
del list_1[0] # 删除第一个元素
del list_1  # 删除整个list


list_1.copy() # 复制

list_1.reverse() # 反转
list_1.sort() # 排序,无返回值
list_1.sorted()  # 返回排序后的新list
list_1.count(1)# 1 的个数，没有为 0
list_2.index('a') # a 的索引，没有会报错

# 切片
print(list_1[0:2]) # [1,2]
print(list_1[0:]) # [1,2,3,4,5]
print(list_1[:2]) # [1,2]
print(list_1[0]) # 1
print(list_1[-1]) # 5
print(list_1[0:4:2]) # [1,3]