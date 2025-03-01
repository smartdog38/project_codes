# 六大数据类型
# import math
# import random
# 1. 数字类型
# 没有长短符号区分，按内存定,且不需要加数值类型
# 整数
# x = 1
# a,b,c = 1,2,3 # 多个变量赋值
# a=b=c=1 # 多个变量赋值
#
# x.to_bytes()#bytes

# 浮点型
# y = 1.1
#
# y.hex()
# y.is_integer()#False

# 复数
# z = 1+1j
#
# z.imag#1j
# z.real#1

# 二进制
# x = 0b101
# 八进制
# x = 0o101
# 十六进制
# x = 0x101

# 随机数
# random.random()#0.0-1.0
# random.randint(1, 10)#1-10
# rand_uniform = random.uniform(1, 10)#1-10
# rand_choice = random.choice([1, 2, 3, 4, 5])#1-5

# 循环
# range(1, 10)#range(start, stop[, step]),step默认为1,不包含stop

# 数学运算
# abs(x)
# math.ceil(x)
# math.floor(x)
# math.fabs(x)
# sqrt_result = math.sqrt(16)  # 4.0
# log_result = math.log(10)  # 2.302585
# exp_result = math.exp(1)  # 2.718281828459045
# pow_result = math.pow(2, 3)  # 8.0

# 运算符
# a = 10
# b = 3

## 赋值运算符
# a += b  # 13
# a -= b  # 7
# a *= b  # 30
# a /= b  # 3.3333...
# a //= b  # 3
# a %= b  # 1
# a **= b  # 1000 (10^3)
# a &= b  # 2
# a |= b  # 11
# a ^= b  # 9
# a >>= b  # 0
# a <<= b  # 40
# a //= b  # 3
# a %= b  # 1
# a **= b  # 1000 (10^3)
# a = -a  # -10
# a = +a  # 10

## 算术运算符
# sum_result = a + b  # 13
# diff_result = a - b  # 7
# product_result = a * b  # 30
# div_result = a / b  # 3.3333...
# floor_div_result = a // b  # 3
# mod_result = a % b  # 1
# power_result = a ** b  # 1000 (10^3)
# negative_result = -a  # -10
# positive_result = +a  # 10

## 比较运算符
# gt_result = a > b  # True
# lt_result = a < b  # False
# ge_result = a >= b  # True
# le_result = a <= b  # False
# eq_result = a == b  # False
# ne_result = a != b  # True

## 逻辑运算符
# and_result = a > b and a < 15  # True
# or_result = a > b or a < 5  # True
# not_result = not a > b  # False

## 位运算符
# and_result = a & b  # 2
# or_result = a | b  # 11
# xor_result = a ^ b  # 9
# invert_result =~ a  # -11

# 2. 字符串类型
# x = 'hello'
# y = "hello"#单引号和双引号没有区别
# z = '''hello'''#多行字符串
#
# x.count('l')#计l的个数
# x.endswith('o')#是否以o结尾
# x.find('l')#查找是否存在
# x.index('l')#查找l的位置
# x.isalnum()#是否是字母或数字
# x.isalpha()#是否是字母
# x.isdigit()#是否是数字
# x.islower()#是否是小写
# x.isupper()#是否是大写
# x.join(['a', 'b', 'c'])#以x为分隔符，将列表中的元素连接成字符串
# x.lower()#将字符串转为小写
# x.lstrip()#去除左边空格
# x.replace('l', 'L')#将l替换为L
# x.rstrip()#去除右边空格
# x.split(" ")#以空格为分隔符，将字符串分割成列表
# x.strip()#去除两边空格
# x.swapcase()#大小写转换
# x.title()#首字母大写
# x.upper()#大写

# 运算符
# a = 'hello'
# b = 'world'

## 赋值运算符
# a += b  # 'helloworld'
# a = a + b  # 'helloworld'
# a *= 2  # 'helloworldhelloworld'
# a = a * 2  # 'helloworldhelloworld'

## 算术运算符
# sum_result = a + b  # 'helloworld'
# diff_result = a - b  # 'hello'

## 比较运算符，字符串比较是按照字符的ASCII码比较
# gt_result = a > b  # False


## 逻辑运算符
# and_result = a > b and a < 15  # False
# or_result = a > b or a < 5  # True
# not_result = not a > b  # True


# 3. 列表类型
# x=['a', 'b', 'c']#字符串列表，直接赋值
# x=[i for i in range(10)]#列表推导式
# x=[i for i in range(10) if i % 2 == 0]#列表推导式，加上过滤条件
# x=[1,2,3]#数字列表，直接赋值
# 多个for按从左到右深入
# [num for elem in vec for num in elem] #vec = [[1,2,3], [4,5,6], [7,8,9]]
# 列表推导式可以嵌套
# [[row[i] for row in matrix] for i in range(4)] # 方框内的更为深入


##转化为列表
# x=list(range(10))#range转为列表
# x=list('abc')#字符串转为列表,[a,b,c]
# x=list((1,2,3))#元组转为列表,[1,2,3]
# x=list({1,2,3})#集合转为列表,[1,2,3]
# x=list({1:2,3:4})#字典转为列表,[1,3]

# x.append(1)#在末尾添加元素l
# x.extend([1,2,3])#在末尾添加可迭代对象里的元素
# x.insert(0,1)#在指定位置添加元素
# x.pop()#删除最后一个元素
# x.pop(0)#删除指定位置的元素,0表示第一个
# x.remove(1)#删除指定元素l,如果有多个l，则删除第一个
# x.clear()#清空列表
# x.count(1)#计算l出现的次数
# x.index(1)#查找l的位置
# x.reverse()#反转列表
# x.sort()#排序
# x.copy()#复制
# del x[0] #删除指定位置的元素
# del x #删除整个列表

# 推导式
# 结果 for 变量名 in 原列表
# x=[i for i in range(10)]#列表推导式
# x=[i for i in range(10) if i % 2 == 0]#列表推导式，加上过滤条件
# 结果值1 if 判断条件 else 结果2  for 变量名 in 原列表
# list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
# print(list2)

# 运算符
# a = [1, 2, 3]
# b = [4, 5, 6]

## 赋值运算符
# a += b  # [1, 2, 3, 4, 5, 6]
# a = a + b  # [1, 2, 3, 4, 5, 6]
# a *= 2  # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# a = a * 2  # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]


## 算术运算符
# sum_result = a + b  # [1, 2, 3, 4, 5, 6]
# diff_result = a - b  # [1, 2, 3]

## 比较运算符，比较的是列表的长度
# gt_result = a > b  # False
# lt_result = a < b  # True

## 逻辑运算符
# and_result = a > b and a < 15  # False
# or_result = a > b or a < 5  # True
# not_result = not a > b  # True


#列表索引
# x=[1,2,3]
# x[0]#1
# x[-1]#3
# x[0:2]#[1,2]
# x[1:]#[2,3]
# x[:2]#[1,2]
# x[:]#[1,2,3]

# 4. 元组类型
# x=(1,2,3)#元组，直接赋值
# x=tuple(range(10))#range转为元组
# x=tuple('abc')#字符串转为元组,('a','b','c')
# x=tuple((1,2,3))#元组转为元组，不变
# x=tuple({1,2,3})#集合转为元组，（1，2，3）
# x=tuple({1:2,3:4})#字典转为元组,（1，3）


#推导式
# x=(i for i in range(10))#元组推导式
# x=(i for i in range(10) if i % 2 == 0)#元组推导式，加上过滤条件

# x.count(1)#计算l出现的次数
# x.count(1)#计算l出现的次数
# x.index(1)#查找l的位置



## 算术运算符
# sum_result = a + b  # (1, 2, 3, 4, 5, 6)

## 比较运算符，比较的是元组的长度
# gt_result = a > b  # False
# lt_result = a < b  # True


## 逻辑运算符
# and_result = a > b and a < 15  # False
# or_result = a > b or a < 5  # True
# not_result = not a > b  # True

# 元组索引，也是用[]
# x=(1,2,3)
# x[0]#1
# x[-1]#3
# x[0:2]#(1,2)
# x[1:]#(2,3)
# x[:2]#(1,2)
# x[:]#(1,2,3)


# 5. 字典类型
# x={1:2,3:4}#字典，直接赋值
# x=dict(zip([1,2,3],[4,5,6]))#zip转为字典
# x=dict(enumerate(['a','b','c']))#enumerate转为字典
# x=dict(('a','b','c'),(1,2,3))#字符串和数字转为字典
# x=dict({1:2,3:4})#字典转为字典

#添加键值对
# x[1]=2

#推导式
# x={i:i**2 for i in range(10)}#字典推导式
# x={i:i**2 for i in range(10) if i % 2 == 0}#字典推导式，加上过滤条件

# del x[1]#删除键为1的键值对
# x.clear()#清空字典
# x.copy()#复制
# x.fromkeys(['a','b','c'],1)#字典推导式
# x.get(1)#获取1的值
# x.items()#获取键值对
# x.keys()#获取键
# x.pop(1)#删除键为1的键值对
# x.popitem()#删除最后一个键值对
# x.setdefault(1,2)#如果键为1，则返回2，否则返回None
# x.update({1:2,3:4})#更新字典
# x.values()#获取值

# 运算符
# a = {1: 2, 3: 4}
# b = {5: 6, 7: 8}

## 赋值运算符
# a += b  # {1: 2, 3: 4, 5: 6, 7: 8}
# a = a + b  # {1: 2, 3: 4, 5: 6, 7: 8}
# a *= 2  # {1: 2, 3: 4, 5: 6, 7: 8, 1: 2, 3: 4, 5: 6, 7: 8}
# a = a * 2  # {1: 2, 3: 4, 5: 6, 7: 8, 1: 2, 3: 4, 5: 6, 7: 8}

## 算术运算符
# sum_result = a + b  # {1: 2, 3: 4, 5: 6, 7: 8}
# diff_result = a - b  # {1: 2, 3: 4}


## 比较运算符，比较的是字典的长度，即键的个数
# gt_result = a > b  # False
# lt_result = a < b  # True


## 逻辑运算符
# and_result = a > b and a < 15  # False
# or_result = a > b or a < 5  # True
# not_result = not a > b  # True

# 字典索引
# x={1:2,3:4}
# x[1]#2

# 6. 布尔类型
# x=True
# x=False

# 运算符
# a = True
# b = False
# and_result = a and b  # False
# or_result = a or b  # True
# not_result = not a  # False
#凡是有非0值的都为True，0为False

# 7. 集合类型
# x={1,2,3}#集合，直接赋值
# x=set(range(10))#range转为集合
# x=set('abc')#字符串转为集合
# x=set((1,2,3))#元组转为集合
# x=set({1,2,3})#集合转为集合，不变
# x=set({1:2,3:4})#字典转为集合,{1,3}

# x.add(1)#添加元素
# x.clear()#清空集合
# x.copy()#复制
# x.difference({1,2,3})#差集
# x.difference_update({1,2,3})#差集更新
# x.discard(1)#删除元素
# x.intersection({1,2,3})#交集
# x.intersection_update({1,2,3})#交集更新
# x.isdisjoint({1,2,3})#是否为空
# x.issubset({1,2,3})#是否为子集
# x.issuperset({1,2,3})#是否为超集
# x.pop()#删除一个元素
# x.remove(1)#删除元素l
# x.symmetric_difference({1,2,3})#对称差集
# x.symmetric_difference_update({1,2,3})#对称差集更新
# x.union({1,2,3})#并集
# x.union_update({1,2,3})#并集更新

# 运算符
# a = {1, 2, 3}
# b = {4, 5, 6}

## 赋值运算符
# a += b  # {1, 2, 3, 4, 5, 6}
# a = a + b  # {1, 2, 3, 4, 5, 6}
# a *= 2  # {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}
# a = a * 2  # {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}

## 算术运算符
# sum_result = a + b  # {1, 2, 3, 4, 5, 6}
# diff_result = a - b  # {1, 2, 3}

## 比较运算符，比较的是集合的长度
# gt_result = a > b  # False
# lt_result = a < b  # True

## 逻辑运算符
# and_result = a > b and a < 15  # False
# or_result = a > b or a < 5  # True
# not_result = not a > b  # True


# 集合索引，也是用[]，以1为起始
# x={1,2,3}
# x[1]#1

# 8. 空类型
# x=None

# 9. 类型转换
# int(x)  #x转为整数
# float(x)  #x转为浮点数
# complex(x)  #x转为复数
# str(x)  #x转为字符串
# repr(x)  #x转为字符串
# list(x)  #x转为列表
# tuple(x)  #x转为元组
# set(x)  #x转为集合
# dict(x)  #x转为字典
# bool(x)  #x转为布尔值
# bytearray(x)  #x转为字节数组
# bytes(x)  #x转为字节
# chr(x)  #x转为字符
# ord(x)  #x转为整数
# round(x)  #x转为整数
# hex(x)  #x转为16进制
# oct(x)  #x转为8进制
# bin(x)  #x转为2进制

# 10. 类型判断
# isinstance(x, int)  #是否为整数
# issubclass(x, int)  #是否为整数类型

#对于所有类型都适用的方法
#len(x)  #x的长度，就是元素个数
#max(x)  #x的最大值
#min(x)  #x的最小值
#sum(x)  #x的和
#any(x)  #x是否有真值
#all(x)  #x是否全为真值
#abs(x)  #x的绝对值
#hash(x)  #x的哈希值
#dir(x)  #x的方法
#id(x)  #x的内存地址
#type(x)  #x的类型