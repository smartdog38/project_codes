# match 是控制流里用法最活的，要与解包一起来理解，建议先看 unpacked
# 基本用法
# match 表达式:
#     case 模式1:
#         语句1
#     case 模式2:
#         语句2
#     case 模式3:
#         语句3
#     case _: #_ 表示任何情况
#         语句4
# 表达式可以是任何表达式，如果匹配成功，就执行相应的语句
# 如果没有匹配成功，就执行最后的语句



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
    case [x,y,z,w]: # 相当于解包
        print(x,y,z,w)
    case _:
        print(a)
match a:
    case [x,*y]:
        print(x,y)  # x 是第一个元素，y 是剩下的元素 1,[2,3,4]
b = [1,2,3,4,[6,7,8]]
match b:
    case [x,y,*z,[*w]]:
        print(x,y,z,w)  # x 是第一个元素，y 是第二个元素
        # z 是首个列表剩下的元素，w 是第二个列表剩下的元素
    case _:
        print(b)

# 匹配元组
a = (1,2,3,4)
match a:
    case (1,2):
        print(a)
    case (x,y,z,w): # 相当于解包
        print(x,y,z,w)
    case _:
        print(a)

b = (1,2,3,4,(6,7,8))
match b:
    case (1,2,):
        print(b)
    case (x,y,*z,w): # x 是第一个元素，y 是第二个元素
        # z 是首个元组剩下的元素（如果是多个元素，变为列表），w 是第二个元组剩下的元素
        print(x,y,z,*w) #

