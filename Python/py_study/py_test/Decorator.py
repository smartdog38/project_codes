# 装饰器
# @ Python的语法糖，等价于
# def greet():
#     print("Hello, World!")
# greet = decorator(greet)
# greet()
# 即调用 decorator 后再调用器返回值


# 函数修饰器
def decorator(func): # func 为修饰的函数
    def wrapper():
        print("函数执行前") # 函数运行前进行操作
        func()
        print("函数执行后") # 函数运行后进行操作
    return wrapper

@decorator # 放在要修饰的函数上
def greet():
    print("Hello, World!")
greet()

# 带参数的修饰器
# 即被修饰的函数要带参数
def decorator(func):
    def wrapper(*args, **kwargs):
        print("函数执行前")
        result = func(*args, **kwargs)
        print("函数执行后")
        return result
    return wrapper
@decorator
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

# 修饰器本身带参数就要再嵌套一层
def repeat(n):  # 修饰器自己的参数
    def decorator(func): # 传进的函数
        def wrapper(*args, **kwargs): # 传进的函数的参数
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")


# 类修饰器
# 先看 class ，再来研究
class Decorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("函数执行前")
        result = self.func(*args, **kwargs)
        print("函数执行后")
        return result

@Decorator
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")


# 多个修饰器
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("装饰器 1 执行前")
        result = func(*args, **kwargs)
        print("装饰器 1 执行后")
        return result
    return wrapper
def decorator2(func):
    def wrapper(*args, **kwargs):
        print("装饰器 2 执行前")
        result = func(*args, **kwargs)
        print("装饰器 2 执行后")
        return result
    return wrapper
@decorator1
@decorator2
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")