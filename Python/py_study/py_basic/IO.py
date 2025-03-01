#输入与输出

#输出用print()函数
# print("Hello, World!")
# print(1, 2, 3, 4, sep=' ')#输出1 2 3 4，即sep指定的分隔符
# print("helloWOrld", end=" ")#输出helloWOrld，即end指定的结尾符,不换行
#str.format()的格式化输出
# name = "Alice"
# age = 30
# print("My name is {0}, and I am {1} years old.".format(name, age))

#f-string
# name = "Alice"
# age = 30
# print(f"My name is {name}, and I am {age} years old.")#常用
# print(f'{name:10} ==> {phone:10d}') #对齐
# '!a' 应用 ascii() 、 '!s' 应用 str() 和 '!r' 应用 repr()
# print(f'My hovercraft is full of {animals!r}.')
# 使用 = 来表达式给直接表示
# bugs = 'roaches' ->{bugs=} -> bugs='roaches'


# 位置及关键字参数可以任意的结合:
# print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# 站点列表 Google, Runoob, 和 Taobao。
# 传入字典作为关键字参数:
# print('站点列表 {google}，{runoob}，和 {taobao}。'.format(**{'google': 'Google', 'runoob': 'Runoob', 'taobao': 'Taobao'}))
# 站点列表 Google，Runoob，和 Taobao。
# table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
# print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table)) #0表示format的第一个值

# :d 表示整数
# :f 表示浮点数
# :s 表示字符串
# :c 表示字符
# :% 表示百分比
# :.2f 表示保留两位小数
# :.2% 表示保留两位小数的百分比
# :<10 表示左对齐，字符串长度小于10时，用空格填充
# :>10 表示右对齐，字符串长度小于10时，用空格填充
# :^10 表示居中对齐，字符串长度小于10时，用空格填充
# :<10.5 表示左对齐，字符串长度小于10时，用空格填充，并显示5位小数
# :>10.5 表示右对齐，字符串长度小于10时，用空格填充，并显示5位小数
# :*^10 表示字符串长度小于10时，用*号填充


#输入用input()函数
# name = input("What is your name? ")

#读写文件
# open（）#返回一个文件对象
# open(filename, mode) #mode 参数指定打开文件的模式
# r 以只读模式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# r+ 打开一个文件用于读写。如果该文件不存在，则会创建一个新文件。
# w 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+ 打开一个文件用于读写。如果该文件不存在，创建新文件。
# a 打开一个文件用于追加。如果该文件不存在，创建新文件。
# a+ 打开一个文件用于读写。如果该文件不存在，创建新文件。
# b 二进制模式。默认为文本模式。
# t 文本模式。默认为文本模式。
# + 打开文件用于读写。
# x 打开文件只用于写入。如果该文件已存在，则会引发异常。如果该文件不存在，创建新文件。
# x+ 打开文件用于读写。如果该文件已存在，则会引发异常。如果该文件不存在，创建新文件。

# 用 with open(filename, mode) as f: # 来自动关闭文件

#对文件对象进行操作
# read() 读取文件的全部内容，并以字符串形式返回。
# readline() 光标移动到下一行，读取文件，并以字符串形式返回。
# readlines() 读取文件的所有行，并以列表形式返回。
# write(string) 写入字符串到文件对象中。
# writelines(sequence) 向文件写入一个序列字符串。序列中的换行符会被转换为操作系统的默认换行符。
# close() 关闭文件。
# flush() 把缓冲区的内容写入磁盘。
# isatty() 返回 True 表示文件是一个终端。
# seek(offset, whence=0) 把文件指针移动到文件的 offset 位置，whence 表示如何计算 offset，0 表示开头，1 表示当前位置，2 表示结尾。
# tell() 返回文件指针当前的位置。
# truncate([size]) 截断文件，参数 size 表示要保留的字节数。
# closed 返回 True 表示文件已关闭。
# encoding 返回文件的编码。
# mode 返回文件的模式。
# name 返回文件名。

# 使用 json 来转换格式
# import json
# 将python文件来转换为json文件
# json.dump(python_object, json_file)
# 将json文件转换为python文件
# json_object = json.load(json_file)

