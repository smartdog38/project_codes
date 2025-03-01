#迭代器Iterators，只能前进不能后退
#两个基本的方法
#__iter__() 返回一个迭代器对象
#__next__() 返回下一个值，如果没有更多的值，抛出StopIteration异常

#迭代器对象有一个内置函数iter()，可以将一个可迭代对象转换为迭代器对象，而next()函数可以调用迭代器对象的__next__()方法
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# print (next(it))   # 输出迭代器的下一个元素
# 1
# print (next(it))
# 2

#用for循环可以直接遍历一个可迭代对象
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
# for x in it:
#     print(x, end=" ")
# 1 2 3 4

#创造一个迭代器
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))

#终止迭代器
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# 生成器generator，使用了 yield 的函数被称为生成器

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
# # 创建生成器对象
# generator = countdown(5)
#
# # 通过迭代生成器获取值
# print(next(generator))  # 输出: 5
# print(next(generator))  # 输出: 4
# print(next(generator))  # 输出: 3
#
# # 使用 for 循环迭代生成器
# for value in generator:
#     print(value)  # 输出: 2 1