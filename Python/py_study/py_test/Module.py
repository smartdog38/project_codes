#################################################################################################
#################################################################################################
"""

模块（Module）
Python 里最有特色的部分
模块（Module）是 Python 中组织代码的基本单位
一个模块通常是一个 .py 文件，包含 Python 代码（如函数、类、变量等）

"""
#################################################################################################
"""

创建模块

创建一个模块非常简单，只需编写一个 .py 文件即可
即，这个 .py 文件就可以叫做模块
模块里所有的函数、类、变量看为一个整体

"""
#################################################################################################

# 现在这个文件就是一个模块
# 我们创建一个 mymodule.py 文件来实践一下
# 并在该文件里输入下面的代码
# def greet(name):
#     print(f"Hello, {name}")
#
# class MyClass:
#     def __init__(self,value):
#         self.value = value
#
#     def display(self):
#         print(f"Value: {self.value}")

#################################################################################################
"""

模块的导入
使用 import 来导入

"""
#################################################################################################

# 导入整个模块
# import module
import mymodule

# 调用模块里的函数，使用 module.func()
mymodule.greet("Alice") # Hello, Alice

# 调用模块里的类，使用 module.class()
obj = mymodule.MyClass(13)
# 访问属性与方法调用与在一个文件里一样
print(obj.value) # 13
obj.display() # Value: 13


# 导入模块的特定内容
# from module import func1,func2,class1,class2 ...
from mymodule import MyClass, greet

# 这样可以直接调用，不用加模块名
greet("Tom") # Hello, Tom
obj_1 = MyClass(88)
print(obj_1.value) # 88
obj_1.display() # Value: 88


# 导入模块时起别名
# 用 as
# 不止模块，函数和类等都可以起
# 但是那是在你的名字与其起冲突时
# 因为每个名字都有其意义
# 形为
# from mymodule import MyClass as mc, greet as gt
import mymodule as mm

# 用别名调用
mm.greet("Jack") # Hello,Jack
obj_2 = mm.MyClass(98)
print(obj_2.value) # 98
obj_2.display() # Value: 98


# 导入模块的所有内容
# 用 * （建议不要用，会导致逻辑混乱，你都不知道导入了些啥）
from mymodule import *

# 直接调用
greet("Amy") # Hello, Amy
obj_1 = MyClass(88)
print(obj_1.value) # 88
obj_1.display() # Value: 88

#################################################################################################
"""

模块的搜索路径
当导入模块时，Python 会按照以下顺序查找模块：
当前目录：Python 首先在当前脚本所在的目录中查找模块
环境变量 PYTHONPATH：如果未找到，Python 会查找 PYTHONPATH 环境变量指定的目录
标准库路径：Python 会查找标准库路径（如 site-packages）
内置模块：最后，Python 会查找内置模块

"""
#################################################################################################

# 查看模块搜索路径
import sys

print(sys.path)


# 如果模块不在默认搜索路径中，可以手动添加路径，也是用 sys这个模块
# import sys
# sys.path.append("/path/to/your/module")

#################################################################################################
"""

模块重载
默认模块只会加载一次
但只是对于已经成熟的代码，在终端运行而言
但是对于 Pycharm 来说没有这个问题，每运行一次，都会加载一次（这是为了调试）
但还是要了解，因为不可能一直活在 Pycharm 里

"""
#################################################################################################

# 使用 importlib.reload 来重载
import importlib
import mymodule

# 修改 mymodule.py 后
importlib.reload(mymodule)

#################################################################################################
"""

模块的 __name__属性 
为什么介绍这个属性？
因为这是每个模块的标识符
每个模块都有一个 __name__ 属性
如果模块是直接运行的，__name__ 的值为 "__main__"
如果模块是被导入的，__name__ 的值为模块名
这个可以让我们确定主程序的所在模块

"""
#################################################################################################

# 在 mymodule.py 来直接运行
# 其 __name__() 就是 "__main__"
# def greet(name):
#     return f"Hello, {name}!"
#
# if __name__ == "__main__":
#     print(greet("Alice"))  # 直接运行时输出: Hello, Alice!

#################################################################################################
"""

标准库函数
有很多系统自带的库，如 math 就规定了许多常用的数学函数
直接 import 就行

"""
#################################################################################################
"""

第三方库
除了标准库模块，Python 还有大量的第三方模块，可以通过 pip 安装
在该环境下的终端输入 pip install module
就可以 import 来使用

"""
#################################################################################################
"""

包的创建与导入
包（Package）是包含多个模块的目录
包必须包含一个 __init__.py 文件（可以是空文件），用于标识该目录是一个包

"""
#################################################################################################

# 这里我们创建一个目录来创建包
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
# 这是在包目录里应该有的结构
# __init__.py 文件可以包含包的初始化代码，也可以为空


# 导入包内的模块
from mypackage import module1, module2

module1.function1() # This is module1!
module2.function2() # This is module2!

#################################################################################################
"""

模块的内置函数
ython 提供了一些内置函数，用于操作模块
dir(module)：列出模块中的所有属性和方法
help(module)：查看模块的帮助文档
...

"""
#################################################################################################
"""

动态导入函数
根据用户需求，由用户决定导入那些模块

"""
#################################################################################################

# 使用 importlib
import importlib

# 模块名可以是变量
module_name = "math"
# 在这里导入
module = importlib.import_module(module_name)
print(module.sqrt(16))  # 输出: 4.0

#################################################################################################
"""

模块的属性
有许多属性都是后期维护或者开发时要用到的
__all__ 
__file__
__doc__
__version__

"""
#################################################################################################

# __all__ 属性
# __all__ 是一个特殊的模块属性，用于定义模块的公共接口
# 当使用 from module import * 时，只有 __all__ 中列出的内容会被导入

# 在 mymodule.py 里申明
# mymodule.py
# 这里来申明属性
# __all__ = ["greet"]
#
# def greet(name):
#     return f"Hello, {name}!"
#
# def secret_function():
#     return "This is a secret."
#
from mymodule import *

print(greet("Alice"))  # Hello, Alice
# 下面的代码会报错
# print(secret_function())  # NameError: name 'secret_function' is not defined


#  __file__属性
# __file__ 属性返回模块的文件路径
import os

print(os.__file__)  # 输出: os 模块的文件路径


# __doc__属性
# __file__ 属性返回模块的文件路径
import math

print(math.__doc__)  # math 模块的文档字符串


# __version__属性
# 可以为模块添加版本信息，方便用户了解模块的更新情况
# 在模块的最上面添加
# __version__ = "1.0.0"

#################################################################################################
"""

打包模块
可以将模块打包并发布到 PyPI（Python Package Index），供其他人安装和使用
帮助别人，快乐自己

"""
#################################################################################################

# 一般的包有这些结构
# mymodule/
#     mymodule/
#         __init__.py
#         module1.py
#         module2.py
#     tests/
#         __init__.py
#         test_module1.py
#         test_module2.py
#     README.md
#     LICENSE
#     setup.py

# mymodule/ 是模块的主目录
# mymodule/mymodule/ 是模块的源代码目录
# tests/ 是单元测试目录
# README.md 是模块的说明文档
# LICENSE 是模块的许可证文件
# setup.py 是打包配置文件


# 编写 setup.py
# setup.py 是打包的核心配置文件，用于定义模块的元数据和依赖项
# 例如
# from setuptools import setup, find_packages
#
# setup(
#     name="mymodule",  # 模块名称
#     version="0.1.0",  # 模块版本
#     author="Your Name",  # 作者
#     author_email="your.email@example.com",  # 作者邮箱
#     description="A short description of your module",  # 模块描述
#     long_description=open("README.md").read(),  # 长描述（通常从 README.md 读取）
#     long_description_content_type="text/markdown",  # 长描述格式
#     url="https://github.com/yourusername/mymodule",  # 项目主页
#     packages=find_packages(),  # 自动查找所有包
#     classifiers=[  # 分类信息
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires=">=3.6",  # Python 版本要求
#     install_requires=[  # 依赖项
#         "requests>=2.25.1",
#     ],
# )


# 编写 README.md
# 编写 LICENSE


# 使用 setuptools 和 wheel 打包模块
# pip install setuptools wheel
# 在模块根目录下运行以下命令
# python setup.py sdist bdist_wheel

# sdist：生成源代码分发包（.tar.gz 文件）
# bdist_wheel：生成 Wheel 分发包（.whl 文件）
# 打包完成后，会在 dist/ 目录下生成分发包文件


# 上传到 PyPI
# 安装上传工具
# pip install twine
# 上传分发包
# twine upload dist/*


# 如果是第一次上传，需要注册 PyPI 账号并获取 API Token
# 上传完成后，模块就可以通过 pip install mymodule 安装了

#################################################################################################
#################################################################################################