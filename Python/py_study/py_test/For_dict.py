# 字典的键必须为不可变类型（int 、float、str、tuple、bool、None），且唯一
dict_1 = {'a':1,'b':2,'c':3} # 键为字符串
dict_2 = {1:1,2:2,3:3} # 键为数字
dict_3 = {(1,2):1,(2,3):2,(3,4):4} # 键为元组
dict_4 = {True:1,False:2} # 键为布尔值
dict_5 = {None:1} # 键为None
print(dict_1['a'])  # 1
print(dict_2[1])  # 1
print(dict_3[(1,2)])  # 1
print(dict_4[True])  # 1
print(dict_5[None])  # 1

# 字典的值可以为任意类型且可重复
my_dict = {
    "number": 42,                         # 整数
    "text": "hello",                      # 字符串
    "flag": True,                         # 布尔值
    "empty": None,                        # None
    "list": [1, 2, 3],                    # 列表（可变）
    "inner_dict": {"key": "value"},       # 嵌套字典
    "function": print,                    # 函数对象
    "tuple": (4, 5, 6)                    # 元组（不可变）
}

# 转换为字典
# 列表/元组->字典
data = [("name", "Alice"), ("age", 25), ("job", "Engineer")]
d = dict(data) # {'name': 'Alice', 'age': 25, 'job': 'Engineer'}
# 两个列表->字典(zip)
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values)) # {'a': 1, 'b': 2, 'c': 3}
# 列表推导式->字典
nums = [10, 20, 30]
d = {f"key_{i}": num for i, num in enumerate(nums)}
# {'key_0': 10, 'key_1': 20, 'key_2': 30}
# 字符串->字典
import json
json_str = '{"name": "Alice", "age": 25}'
d = json.loads(json_str) # {'name': 'Alice', 'age': 25}
# URL参数->字典
query_str = "name=Alice&age=25&job=Engineer"
d = {k: v for k, v in [pair.split("=") for pair in query_str.split("&")]}
# {'name': 'Alice', 'age': '25', 'job': 'Engineer'}


dict_1[3] = 4 # 添加键值对
del dict_1[3] # 删除键值对，没有会报错哦
dict_1.pop('a') # 删除键为a的键值对
dict_1.pop("x", "不存在")  # 没有时，返回"不存在"
dict_1.popitem() # 删除最后一个键值对
dict_1.clear() # 清空

dict_1['a'] # 访问键为a的值，不存在会报错
dict_1.get('a') # 访问键为a的值，不存在返回None
dict_1.get('a',0) # 访问键为a的值，不存在返回0

dict_1.copy()  # 复制

dict_1.keys() # 返回键的列表
dict_1.values() # 返回值的列表
dict_1.items() # 返回键值对的列表

for k,v in dict_1.items():
    print(k,v)