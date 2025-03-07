#################################################################################################
#################################################################################################
"""

异常（Exception）
异常处理是 Python 编程中的重要部分，用于捕获和处理程序运行过程中可能出现的错误
通过异常处理，可以避免程序崩溃，并提供友好的错误提示或恢复机制

异常（Exception）：程序运行过程中发生的错误或意外情
常处理（Exception Handling）：捕获并处理异常，避免程序崩溃

"""
#################################################################################################
"""

异常的类型

"""
#################################################################################################

# Python 中的异常是一个类，所有内置异常都继承自 BaseException 类
# 常见的异常类包括：
# Exception：所有内置异常的基类
# ValueError：值错误，如类型转换失败
# TypeError：类型错误，如对不支持的操作数类型进行操作
# IndexError：索引错误，如访问列表时索引超出范围
# KeyError：键错误，如访问字典中不存在的键
# FileNotFoundError：文件未找到错误
# ZeroDivisionError：除零错误

#################################################################################################
"""

异常处理的基本语法

"""
#################################################################################################

# Python 使用 try、except、else 和 finally 语句来处理异常

# try 和 except
# try 块包含可能引发异常的代码
# except 块捕获并处理异常
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")


# 可以捕获多个异常，并为每个异常提供不同的处理逻辑
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Division by zero")


# 可以使用 except Exception 捕获所有异常（尽量不用）


# else 块
# else 块中的代码在 try 块没有引发异常时执行
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print(f"Result: {result}")


# finally 块
# finally 块中的代码无论是否引发异常都会执行，通常用于释放资源或清理操作
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found")
finally:
    file.close()
    print("File closed")

#################################################################################################
"""

自定义异常
可以通过继承 Exception 类创建自定义异常。

"""
#################################################################################################

class MyError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    # 用 raise 直接引起指定异常，并可以传递信息，用 err(message) 来使用
    raise MyError("This is a custom error")
except MyError as e:
    print(f"Caught an error: {e.message}")

#################################################################################################
"""

异常的传递
如果异常在函数中没有被捕获，它会传递到调用该函数的地方，直到被捕获或程序终止

"""
#################################################################################################

def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
    # 当函数引起异常，就会传递出来，被 except 捕获
except ZeroDivisionError:
    print("Error: Division by zero")

#################################################################################################
"""

异常的抛出
在 except 块中可以使用 raise 重新抛出异常

"""
#################################################################################################

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught an error, re-raising it")
    # 直接 raise 就行，还是这个异常
    raise

#################################################################################################
"""

断言
断言用于检查某个条件是否为真，如果为假，则引发 AssertionError 异常

"""
#################################################################################################

def divide(a, b):
    # b 不能等于 0
    assert b != 0
    return a / b

result = divide(10, 0)

#################################################################################################
"""

上下文管理与资源释放
使用 with 来进行管理

"""
#################################################################################################
"""

异常的链式处理
异常的链式处理是指将一个异常（通常是新抛出的异常）与另一个异常（通常是捕获的原始异常）关联起来
这样可以在抛出新异常的同时，保留原始异常的上下文信息
使用 raise ... from ...

异常链的主要作用是：
保留上下文：在抛出新异常时，保留原始异常的上下文信息，方便调试
明确因果关系：通过异常链，可以清晰地看到异常的因果关系，即新异常是由原始异常引发的

"""
#################################################################################################

try:
    10 / 0
except ZeroDivisionError as e:
    raise ValueError("Invalid operation") from e

# Traceback (most recent call last):
#   File "example.py", line 2, in <module>
#     10 / 0
# ZeroDivisionError: division by zero
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "example.py", line 4, in <module>
#     raise ValueError("Invalid operation") from e
# ValueError: Invalid operation

# 可以看到其会有异常之间的关联信息

#################################################################################################
"""
异常的链式处理通过 raise ... from ... 语法实现，用于将一个异常与另一个异常关联起来
异常链保留了原始异常的上下文信息，方便调试和错误追踪
__cause__ 和 __context__ 属性用于访问异常链中的前一个异常
使用 raise ... from None 可以避免保留原始异常的上下文
异常链适用于封装异常、调试、日志记录和错误转换等场景
"""
#################################################################################################
#################################################################################################