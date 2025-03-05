# 用于各种可迭代对象的元素遍历
# 列表的遍历
s_list = [1,2,3,4,5]
for i in s_list:
    print(i)
# 字符串的遍历
s_str  = "hello world"
for i in s_str:
    print(i)
# 集合的遍历
s_set  = {1,2,3,4,5}
for i in s_set:
    print(i)
# 元组的遍历
s_tuple = (1,2,3,4,5)
for i in s_tuple:
    print(i)
# 字典的遍历
s_dict = {'name':'1', 'age':'2'}
for i in s_dict: # 默认遍历字典的key
    print( i +': '+s_dict[i])
for key,value in s_dict.items(): # 遍历字典的key和value
    print(key +': '+value)

# 使用range()函数生成整数序列
for i in range(10):
    print(i)
for i in range(1,10,2):
    print(i)
# for 可以嵌套
for i in range(10):
    for j in range(10):
        print(i,j)

# 使用enumerate来获取索引与值
for index,value in enumerate(s_list):
    print(index,value)

# 使用zip()函数来组合两个序列
s_list = [1,2,3,4,5]
s_tuple = ('a','b','c','d','e')
for i,j in zip(s_list,s_tuple):
    print(i,j)

# else语句,正常结束后执行
for i in range(10):
    print(i)
else:
    print("else work")

# break 语句,跳出循环
for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print("else work")

# continue 语句,跳过本次循环
for i in range(10): #
    if i == 11:
        continue
    print(i)
else:
    print("else work")



