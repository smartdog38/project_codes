# match 是控制流里用法最活的，要与解包一起来理解，建议先看 unpacked
# 基本用法
# match 表达式:
#     case 模式1:
#         语句1
#     case 模式2:
#         语句2
#     case 模式3:
#         语句3
#     case _: #_ 所有模式都不匹配，就执行这个语句，有点像 if 里的 else
#         语句4
# 表达式可以是任何表达式，如果匹配成功，就执行相应的语句


# 常量模式 数字、字符串、布尔值、None
a = 1
match a:
    case 1:
        print(a)
    case 2:
        print(a)
    case 3:
        print(a)
    case _:
        print(a)

# 匹配多个值
a = 'sss'
match a:
    case 1 | 2 | 3:
        print(a)
    case _:
        print(a)


# 匹配列表
a = [1,2,3,4]
match a:
    case [1,2]:
        print(a)
    case x,y,z,w: # 相当于解包，即x, y, z, w = a
        print(x,y,z,w)
    case _:
        print(a)

match a:
    case x,*y:
        print(x,y)  # x 是第一个元素，y 是剩下的元素 1,[2,3,4]

b = [1, 2, 3, 4, [6, 7, 8]]
match b:
    case x,y,*z,[*w]: # 注意，这里不能[]与()混用,只能用 []
        print(x,y,z,w)  # x 是第一个元素，y 是第二个元素
        # z 是首个列表剩下的元素，w 是第二个列表剩下的元素
    case _:
        print(b)


# 匹配元组
a = (1,2,3,4)
match a:
    case (1,2):
        print(a)
    case x,y,z,w:
        print(x,y,z,w)
    case _:
        print(a)

# 匹配嵌套元组
b = (1,2,3,4,(6,7,8))
match b:
    case (1,2,):
        print(b)
    case (x,y,*z,[*w]): # x 是第一个元素，y 是第二个元素
        # z 是首个元组剩下的元素（如果是多个元素，变为列表）
        # w 是第二个元组剩下的元素，只能用 [] 来表示嵌套，不然会报错
        print(x,y,*z,*w)


# 匹配字典
# 只要字典里包含case里的键就能匹配
person = {"name": "Wang", "age": 25, "addr": "aaa"}
match person:
    case {"name": "Alice", "age": age}: # 值也要匹配
        print(f"Alice 的年龄是 {age}")
    case {"name": name, "age": age}: # 只匹配键
        print(f"{name} 的年龄是 {age}")
    case _:
        print("未匹配")


# 匹配枚举
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
color = Color.GREEN
match color:
    case Color.RED:
        print("红色")
    case Color.GREEN:
        print("绿色")
    case Color.BLUE:
        print("蓝色")
    case _:
        print("未知颜色")


# 匹配类型
value = 3.14
match value:
    case int():
        print("整数")
    case float():
        print("浮点数")
    case str():
        print("字符串")
    case _:
        print("未知类型")


# 匹配类的实例
# match 对象:
#     case 类名(属性1=值1, 属性2=值2):
#         代码块
class Point:
    def __init__(self, x, y): # 三个属性
        self.x = x
        self.y = y

p = Point(1, 2)
match p:      # 匹配成功可以提取类的属性，不需匹配所有的属性，特定就行
    case Point(x=0, y=0):
        print("原点")
    case Point(x=x, y=y):
        print(f"点的坐标是 ({x}, {y})")
    case _:
        print("未匹配")

# 匹配特定属性
p = Point(1, 2)
match p:
    case Point(x=1):
        print("x 坐标是 1")
    case Point(y=2):
        print("y 坐标是 2")
    case _:
        print("未匹配")

# 匹配类型
p = Point(1, 2)
match p:
    case Point():
        print("这是一个 Point 对象")
    case _:
        print("未匹配")

# 匹配嵌套类
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
p1 = Point(0, 0)
p2 = Point(1, 1)
line = Line(p1, p2)
match line:
    case Line(start=Point(x=0, y=0), end=Point(x=1, y=1)):
        print("从原点到 (1, 1) 的线段")
    case Line(start=Point(x=x1, y=y1), end=Point(x=x2, y=y2)):
        print(f"从 ({x1}, {y1}) 到 ({x2}, {y2}) 的线段")
    case _:
        print("未匹配")

# 匹配继承的类
class Shape:
    pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
shape = Circle(5)
match shape:
    case Circle(radius=r):
        print(f"这是一个半径为 {r} 的圆")
    case Shape():
        print("这是一个形状")
    case _:
        print("未匹配")

# match 的应用
# match的高级应用
# 匹配特殊的值
command = 'look'
match command.split():
    case "quit":
        print("Goodbye!")
        # quit_game()
    case ["look"]:
        print("Look!")
        # current_room.describe()
    case "get", *obj:
        print("Pick " + obj[0] + " up")
        # character.get(obj, current_room)
    case "go", ("north" | "south" | "east" | "west") as direction:
        print("go " + direction)
        # current_room = current_room.neighbor(direction)