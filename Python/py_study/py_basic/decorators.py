#修饰器decorators
#装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数

# def decorator_function(original_function):
#     def wrapper(*args, **kwargs):
#         # 这里是在调用原始函数前添加的新功能
#         before_call_code()
#
#         result = original_function(*args, **kwargs)
#
#         # 这里是在调用原始函数后添加的新功能
#         after_call_code()
#
#         return result
#
#     return wrapper
#
#
# # 使用装饰器
# @decorator_function
# def target_function(arg1, arg2):
#     pass  # 原始函数的实现


# 带参数的装饰器
# def repeat(n):#n是参数
#     def decorator(func):#在这里接收函数
#         def wrapper(*args, **kwargs):#在这里接收函数的参数，且进行修饰
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Alice")


#类装饰器
# class DecoratorClass:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         # 在调用原始函数之前/之后执行的代码
#         result = self.func(*args, **kwargs)
#         # 在调用原始函数之后执行的代码
#         return result
#
#
# @DecoratorClass
# def my_function():
#     pass