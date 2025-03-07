# __iter__()  规定返回迭代器对象
# __next__()  规定迭代器的返回元素的逻辑

# 可迭代对象里都申明了__iter__()
# 迭代器对象里都申明了__iter__()与__next__()
# 迭代器的__next__()方法申明了迭代对象进入迭代器后的迭代逻辑

class MyIterator:
    # data定义了进入迭代器的可迭代对象
    def __init__(self,data):
        self.data = data
        # 定义索引，在限制求取范围是会有用
        self.index = 0

    def __iter__(self):
        # 迭代器的__iter__()返回自己
        return self

    # 定义迭代逻辑
    def __next__(self):
        # 先判断索引是否超过了迭代对象的最大范围,超过就报错退出
        if self.index >= len(self.data):
            raise StopIteration
        # 找到要返回的元素
        value = self.data[self.index]
        # 更新索引，等待下次索引
        self.index += 1
        # 返回元素，即用 next(Iterable) 会获得的值
        return value

class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MyIterator(self.data)  # 指定一个迭代器

# 创建可迭代对象,利用列表、元组等可迭代类型将数据传入
# 且定义的迭代器的迭代逻辑是value = self.data[self.index]，所以是使用列表来进行
# 如果迭代逻辑改变那么传入类型也要改变,如通过字典的键取值就不是用 index
my_iterable = MyIterable([1, 2, 3])

# 创建迭代器
my_iterator = MyIterator([1, 2, 3])

# 使用 for 循环遍历，对于迭代器与迭代对象都可以
for num in my_iterable:
    print(num)
for num in my_iterator:
    print(num)

# 使用 next 来进行遍历，是迭代器的next方法
# 因为迭代器也有__iter__()方法，是他自身
my_iterator = MyIterator([1, 2, 3])
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))


# Generator（生成器）是一种特别的迭代器