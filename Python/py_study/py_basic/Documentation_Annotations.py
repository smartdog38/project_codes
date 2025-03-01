#Documetation(文档描述)
#函数的第一行应该放对象用途的简短摘要，不应明确说明对象的名称或类型，此行应以大写字母开头，以句点结尾
#如果文档字符串中有更多行，则第二行应为空，从而在视觉上将摘要与描述的其余部分分开
#字符串第一行之后的第一个非空行确定整个文档字符串的缩进量。（我们不能使用第一行，因为它通常与字符串的左引号相邻）

#Annontations（函数注释）
#参数注释
# def foo(a: str, b: int = 5):#
#     ...
#from typing import Tuple
#
# def foo(*args: Tuple[int, str, float]):
#     for arg in args:
#         print(arg)
#
# foo((1, 'apple', 3.14), (2, 'banana', 2.71))
#expreession 是一个表达式，它的值是参数的类型
#
#返回值注释
#def sum() -> expression(int float str,):
# ...
#若是多个类型的一种
# from typing import Union
#def sum() -> Union[int, float, str]:
# ...

