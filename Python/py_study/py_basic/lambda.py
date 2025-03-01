#匿名表达式lambda

# lambda arguments: expression
#lambda 参数列表:表达式
#lambda 参数1,参数2,...:表达式
#lambda 参数1=默认值,参数2=默认值,...:表达式
#lambda 参数1,参数2,...:表达式
#lambda 参数1,参数2,...:表达式

# x = lambda a : a + 10
# print(x(5))

#与其他函数一起用
#map() #map(function, iterable)
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)  # 输出: [1, 4, 9, 16, 25]
#
# filter() #filter(function, iterable)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # 输出：[2, 4, 6, 8]