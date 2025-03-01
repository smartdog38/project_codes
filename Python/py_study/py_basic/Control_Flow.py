##while loop
#while condition:
#    循环体
#只要condition不为False，就一直执行循环体
#例如
# while 1:
#     print(1)
#while后面的条件可以是任何表达式，只要为True就一直循环
#对于else语句，只有在循环正常结束时才会执行，如果循环被break终止，则不会执行else语句

##for loop,可以接受一个可迭代对象，如list,tuple,dict,string，与while循环相比，for循环更加简洁，range()函数可以生成一个整数序列
#for i in range(10):
#    print(i)
#range(10)表示从0到9
#for i in range(1,10):
#    print(i)
#range(1,10)表示从1到9
#for i in range(1,10,2):
#    print(i)
#range(1,10,2)表示从1到9，步长为2
#
#字典的for语句
# for user, status in users.items():#iterms()返回所有的键值对
#对于else语句，只有在循环正常结束时才会执行，如果循环被break终止，则不会执行else语句
#要循环多个序列的话，可以用zip
# for q, a in zip(questions, answers):



##if 语句
#if 条件:
#    语句1
#elif 条件:
#    语句2
#else:
#    语句3

##match 语句
#match 表达式:
#    case 模式1:
#        语句1
#    case 模式2:
#        语句2
#    case 模式3:
#        语句3
#    case _:#_ 表示任何情况
#        语句4
#match 表达式 可以是任何表达式，如果匹配成功，就执行相应的语句，如果没有匹配成功，就执行最后的语句

#常量模式 数字、字符串、布尔值、None

#变量模式 变量名

#通配符模式 _  #匹配任何情况

#类型模式 type(变量)

#元组模式 (变量1,变量2,...)#与列表模式类似

#列表模式 [变量1,变量2,...]
# def match_sequence(value):
#     match value:
#         case [1, 2, 3]:
#             print("Matched [1, 2, 3]")
#         case [x, y]:
#             print(f"Matched a two-element list: {x}, {y}")
#         case _:
#             print("No match")
#
# match_sequence([1, 2, 3])  # 输出: Matched [1, 2, 3]
# match_sequence([4, 5])      # 输出: Matched a two-element list: 4, 5

#字典模式 {变量1:变量2,...}
# def match_dict(value):
#     match value:
#         case {"name": name, "age": age}:
#             print(f"Name: {name}, Age: {age}")
#         case _:
#             print("No match")
#
# match_dict({"name": "Alice", "age": 30})  # 输出: Name: Alice, Age: 30

#类模式 类名()
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# def match_class(value):
#     match value:
#         case Person(name, age):
#             print(f"Person's name is {name}, age is {age}")
#         case _:
#             print("Not a Person")
#
# match_class(Person("Alice", 30))  # 输出: Person's name is Alice, age is 30

#模式组合
# def match_value(value):
#     match value:
#         case 1 | 2 | 3:
#             print("Value is 1, 2, or 3")
#         case _:
#             print("Other value")
#
# match_value(2)  # 输出: Value is 1, 2, or 3

#带条件的模式
# def match_with_condition(value):
#     match value:
#         case x if x > 10:
#             print(f"Value is greater than 10: {x}")
#         case x if x <= 10:
#             print(f"Value is less than or equal to 10: {x}")
#         case _:
#             print("No match")
#
# match_with_condition(15)  # 输出: Value is greater than 10: 15

#子模式
# def match_nested(value):
#     match value:
#         case (x, (y, z)):
#             print(f"Matched tuple: {x}, {y}, {z}")
#         case _:
#             print("No match")
#
# match_nested((1, (2, 3)))  # 输出: Matched tuple: 1, 2, 3
#匹配剩余部分用*rest
# def match_tuple(value):
#     match value:
#         case (x, *rest):  # 匹配元组的第一个元素并将剩余部分绑定到 rest
#             print(f"First element: {x}, Rest: {rest}")
#         case _:
#             print("No match")
#
# match_tuple((1, 2, 3, 4))  # 输出: First element: 1, Rest: [2, 3, 4]
# match_tuple((5,))           # 输出: First element: 5, Rest: []

#match不需要显式的使用break
#当类里有__match_args__()方法时，可以使用该方法来自定义匹配行为
#class Point:
#     __match_args__ = ('x', 'y')#指定匹配的参数
#     def __init__(self, x, y):#指定初始化的参数
#         self.x = x
#         self.y = y
#
# match points:
#     case []:#匹配空列表
#         print("No points")
#     case [Point(0, 0)]:#匹配原点
#         print("The origin")
#     case [Point(x, y)]:#匹配单点
#         print(f"Single point {x}, {y}")
#     case [Point(0, y1), Point(0, y2)]:#匹配两个在y轴上的点
#         print(f"Two on the Y axis at {y1}, {y2}")
#     case _:
#         print("Something else")



#match的高级应用
#匹配特殊的值
# match command.split():
#     case ["quit"]:
#         print("Goodbye!")
#         quit_game()
#     case ["look"]:
#         current_room.describe()
#     case ["get", obj]:
#         character.get(obj, current_room)
#     case ["go", direction]:
#         current_room = current_room.neighbor(direction)
#     # The rest of your commands go here
#
#匹配多个值
# match command.split():
#     case ["drop", *objects]:
#         for obj in objects:
#             character.drop(obj, current_room)
#     # The rest of your commands go here
#这里可以是*objects, 表示匹配多个值，前面是*rest，是一样的
#
#匹配特定序列范围里任意的值
# match command.split():
#     case ["go", ("north" | "south" | "east" | "west") as direction]:#这里加as是为了给下面的
#操作一个确定的方向
#         current_room = current_room.neighbor(direction)
#加上过滤条件
# match command.split():
#     case ["go", direction] if direction in current_room.exits:
#         current_room = current_room.neighbor(direction)
#     case ["go", _]:
#         print("Sorry, you can't go that way")

#模式匹配的优先级
#1.常量模式
#2.变量模式
#3.通配符模式
#4.类型模式
#5.元组模式
#6.列表模式
#7.字典模式

#pass, 空语句，什么都不做
#break, 跳出循环
#continue, 跳过本次循环

# 优先级：not>and>or