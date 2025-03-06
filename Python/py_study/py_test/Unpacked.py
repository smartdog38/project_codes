# 解包（列表，元组等）
# 基本解包
list_1 = [1,2,3,4,]
set_1 = {1,2,3,4,}
tuple_1 = (1,2,3,4,)
dict_1 = {'a':1,'b':2,'c':3,'d':4}
x,y,z,w = list_1
print(x,y,z,w)  # 1 2 3 4
x,y,z,w = set_1
print(x,y,z,w)  # 1 2 3 4
x,y,z,w = tuple_1
print(x,y,z,w)  # 1 2 3 4
x,y,z,w = dict_1
print(x,y,z,w) # a b c d ->默认解出键值

# 用 * 解包（解出剩余元素，放进列表里）
x,y,*w = list_1
print(x, y, w) # 1 2 [3,4]
x,y,*w = set_1
print(x, y, w) # 1 2 [3,4]
x,y,*w = tuple_1
print(x, y, w) # 1 2 [3,4]
x,y,*w = dict_1
print(x, y, w) # a b ['c', 'd']

# 解包到中间变量里
x, *y, z = list_1
print(x, y, z) # 1 [2,3] 4
x, *y, z = set_1
print(x, y, z) # 1 [2,3] 4
x, *y, z = tuple_1
print(x, y, z) # 1 [2,3] 4
x, *y, z = dict_1
print(x, y, z) # a ['b', 'c'] d

# 解包可以解嵌套结构(不含字典),()与[]可以混用,但最好还是规范使用
list_2 = [1, 2, [3, 4], 5]
set_2 = {1, 2, (3, 4), 5}
tuple_2 = (1, 2, (3, 4), 5)

x, y, (z, w), m = list_2 # 里面为[] ,但可以用()
print(x, y, z, w, m) # 1 2 3 4 5
# 集合为无序，不能直接指定解包，可以先转换
# 但注意转换以后，嵌套的结构会被放在最后，所以尽量不用集合进行嵌套解包
x, y, m, [z, w] = list(set_2) # list(set_2) -> [1, 2, 5, (3, 4)]
print(x, y, z, w, m) # 1 2 3 4 5
x, y, [z, w], m = tuple_2
print(x, y, z, w, m) # 1 2 3 4 5


# 解包字符串
s = 'abc'
x,y,z = s
print(x,y,z) # a b c
x, *y = s
print(x,y)  # a ['b', 'c']

# 函数解包 （具体细节到函数在进行详细介绍）
def func(x,y,z):
    print(x,y,z)
args = (1,2,3,)
func(*args) # 1 2 3

def greet(name, age):
    return f"Hello, {name}! You are {age} years old."
kwargs = {"name": "Alice", "age": 25}
print(greet(**kwargs))  # Hello, Alice! You are 25 years old.

