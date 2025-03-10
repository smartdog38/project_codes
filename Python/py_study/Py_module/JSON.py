#################################################################################################
#################################################################################################
"""

JSON
Python的json模块是处理JSON数据的核心模块
支持序列化（将Python对象转换为JSON字符串）和反序列化（将JSON字符串转换为Python对象）

"""
#################################################################################################
"""

主要函数

"""
#################################################################################################

# 序列化
# json.dumps(obj)
# json.dump(obj, file)
# 反序列化
# json.loads(json_str)
# json.load(file)

import json



# json.dumps(obj)
# 将Python对象（字典、列表等）转换为JSON格式的字符串
data = {"name": "Alice", "age": 30, "city": "New York"}
json_str = json.dumps(data)
# 其实还是 str 的类型
print(type(json_str))
print(json_str)  # {"name": "Alice", "age": 30, "city": "New York"}


# json.dump(obj, file)
# 将Python对象写入JSON文件
data = {"name": "Alice", "age": 30, "city": "New York"}
with open(r"D:\code\Python\py_study\Py_module\data\json_test.json", "w") as f:
    json.dump(data, f)
# 发现 data 里面多了个 json_test.json
# 里面的内容为：{"name": "Alice", "age": 30, "city": "New York"}


# json.loads(json_str)
# 直接定义为 json 格式
json_str = '{"name": "Bob", "age": 25}'
data = json.loads(json_str)
print(data["name"])  # Bob


# json.load(file)
with open(r"D:\code\Python\py_study\Py_module\data\json_test.json", "r") as f:
    data = json.load(f)
    print(data) # {'name': 'Alice', 'age': 30, 'city': 'New York'}

#################################################################################################
"""

相关参数

"""
#################################################################################################

# indent
# ensure_ascii
# default
# object_hook

import json


# indent
# 美化输出
data = {"a": 1, "b": 2}
pretty_json = json.dumps(data, indent=4)

print(pretty_json)
# {
#     "a": 1,
#     "b": 2
# }


# ensure_ascii
# 处理非ASCII字符
data = {"name": "张三"}
json_str = json.dumps(data, ensure_ascii=False)

print(json_str) # {"name": "张三"}


# default
# 处理无法直接序列化的对象（如日期、自定义类）
from datetime import datetime



def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

data = {"time": datetime.now()}
# 对于无直接序列化的值进行 default
json_str = json.dumps(data, default=custom_serializer)

print(json_str)


# object_hook
# 将JSON字典转换为自定义对象
# 定义对象
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 调用对象的逻辑实现
def dict_to_user(d):
    return User(d["name"], d["age"])

json_str = '{"name": "Charlie", "age": 40}'
# object_hook 会将里面的数据返回，利用这个进行对象赋值
user = json.loads(json_str, object_hook=dict_to_user)

print(user.name)  # Charlie

#################################################################################################
"""

支持的类型映射

"""
#################################################################################################

# Python类型	JSON类型
# dict          object
# list, tuple	array
# str           string
# int, float    number
# True/False    true/false
# None          null

# 无法直接序列化的类型
# 如datetime、自定义类等，需通过default参数处理

#################################################################################################
#################################################################################################