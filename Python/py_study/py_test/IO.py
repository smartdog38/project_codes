# #################################################################################################
# #################################################################################################
# """
#
# 输入输出（IO）
#
# """
# #################################################################################################
# """
#
# 标准输入输出（Standard Input/Output）
# 标准输入输出是计算机程序中用于与用户或其他程序进行交互的基本机制
# 在 Python 中，标准输入输出通常指的是以下三个流：
# 标准输入（stdin）：用于从用户或外部程序读取输入
# 标准输出（stdout）：用于向用户或外部程序输出信息
# 标准错误（stderr）：用于输出错误信息
#
# 这些流是操作系统提供的，Python 通过 sys 模块提供了对它们的访问
#
# """
# #################################################################################################
#
# # 标准输入（stdin）
# # 标准输入是程序从用户或外部程序读取数据的默认来源
# import sys
#
# # 从标准输入读取一行数据
# data = sys.stdin.readline()
# print(f"You entered: {data.strip()}")
#
# # 从标准输入读取多行数据，直到输入 EOF（Ctrl+D）
# for line in sys.stdin:
#     print(f"Line: {line.strip()}")
#     # 刷新输入缓冲区，加入这个才能在 Ctrl+D 后退出 for 循环
#     sys.stdin.flush()
#
#
# # input 函数用于从标准输入（stdin）读取用户输入
# # 它会阻塞程序执行，直到用户输入数据并按下回车键
#
# # input(prompt=None)
# # prompt：可选参数，用于显示提示信息
#
# name = input("Enter your name: ")
# print(f"Hello, {name}!")
#
# # input 函数从标准输入读取一行数据，并返回一个字符串
# # input 与 sys.stdin 的关系
# # input 函数默认从 sys.stdin 读取数据
# # 可以通过重定向 sys.stdin 来改变 input 的输入源
# import sys
#
# with open("input.txt", "r") as f:
#     # 将标准输入重定向到文件
#     sys.stdin = f
#     # 从文件读取输入
#     data = input()
#     print(f"Read from file: {data}")
#
# # 恢复标准输入
# sys.stdin = sys.__stdin__
# name = input("Enter your name: ")
# print(f"Hello, {name}!")
#
#
#
# # 标准输出（stdout）
# # 标准输出是程序向用户或外部程序输出信息的默认目标
# import sys
#
# # 向标准输出写入数据
# sys.stdout.write("Hello, World!\n") # Hello, world!
#
#
# # print 函数用于将数据输出到标准输出（stdout）
#
# # print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# # *objects：要输出的对象，可以是多个，用逗号分隔
# # sep：对象之间的分隔符，默认是空格
# # end：输出结束时的字符，默认是换行符 \n
# # file：输出目标，默认是 sys.stdout
# # flush：是否强制刷新输出缓冲区，默认是 False
# print("Hello, World!")  # 输出: Hello, World!
# print(1, 2, 3, sep=", ")  # 输出: 1, 2, 3
# print("No newline", end="")  # 输出: No newline（不换行）
#
# # print 函数默认将输出发送到 sys.stdout，即标准输出
# # 可以通过 file 参数将输出重定向到其他流（如文件）
# import sys
#
# # 将输出重定向到文件
# with open("output.txt", "w") as f:
#     print("Hello, World!", file=f)
# # 恢复标准输出
# print("This will be printed to the console")
#
# # 对于 print 推荐一个格式
# # print(f"My name is {name:s}, and I am {age:s} years old.")#常用
# # 另外，有一个限定的方法 :
# # :d 表示整数
# # :f 表示浮点数
# # :s 表示字符串
# # :c 表示字符
# # :% 表示百分比
# # :.2f 表示保留两位小数
# # :.2% 表示保留两位小数的百分比
# # :<10 表示左对齐，字符串长度小于10时，用空格填充
# # :>10 表示右对齐，字符串长度小于10时，用空格填充
# # :^10 表示居中对齐，字符串长度小于10时，用空格填充
# # :<10.5 表示左对齐，字符串长度小于10时，用空格填充，并显示5位小数
# # :>10.5 表示右对齐，字符串长度小于10时，用空格填充，并显示5位小数
# # :*^10 表示字符串长度小于10时，用*号填充
#
# # 标准错误（stderr）
# # 标准错误是程序输出错误信息的默认目标
# import sys
#
# # 向标准错误写入数据
# sys.stderr.write("Error: Something went wrong\n") # Error: Something went wrong 红色输出
#
# # print() 函数的 file 参数默认值是 sys.stdout，即标准输出
# # 如果将 file 参数设置为 sys.stderr，则输出会发送到标准错误
# import sys
#
# # 将输出发送到标准错误
# print("This is an error message", file=sys.stderr)
#
#

#################################################################################################
"""

文件IO


"""
#################################################################################################
"""

读写文件
在Python中，使用 open() 与 close() 来打开、关闭文件
用 read() 等函数读取文件
用 write() 等函数写入文件

"""
#################################################################################################

# open(filepath, mode)
# 它需要两个参数：文件名和打开模式
# mode :
# r	只读（默认）
# w	写入（覆盖原有内容）
# a	追加（在文件末尾添加）
# r+	读写（文件指针在开头）
# w+	读写（覆盖文件）
# a+	读写（文件指针在末尾）
# b	二进制模式（如 rb, wb）

# 打开文件用于写入
file = open("example.txt", "w")
file.write("HAHA")

# file.close()
# 在打开文件后手动关闭文件
file.close()  # 关闭文件


# 对文件的读与写
# 有许多种方法
# read() 读取文件的全部内容，并以字符串形式返回。
# readline() 光标移动到下一行，读取文件，并以字符串形式返回。
# readlines() 读取文件的所有行，并以列表形式返回。
# write(string) 写入字符串到文件对象中。
# writelines(sequence) 向文件写入一个序列字符串。序列中的换行符会被转换为操作系统的默认换行符。

# read()
# 一定要可读啊
file = open("example.txt","r")
content = file.read()
print(content) # 空的，因为我们没写东西
# 记得关闭文件
file.close()

# readline()
# 从第一行开始，每调用一次读一行的内容
file = open("example.txt","r")
content_1 = file.readline()
print(content) # 返回第一行的内容
content_2 = file.readline()
print(content_2) # 返回第二行的内容
file.close()
# for 来遍历
# for line in f:
#     print(line.strip())  # 去除首尾空白及换行符

# readlines()
# 将每行的内容写进列表并返回该列表
file = open("example.txt","r")
content_list = file.readlines()
print(content_list[0])
# 第一行的内容,要有数据才能索引
# IndexError: list index out of range，因为没数据
file.close()

# write("message")
# 要有可写的权限且模式要为可写
file = open("example.txt","w")
file.write("Hello\nI love you")
# 文件里为
# Hello
# I love you
file.close()
# \n 换行符
# \t 制表符


#################################################################################################
"""

文件的其他操作


"""
#################################################################################################

# flush() 
# 调用write()方法时，数据并不会立即写入磁盘，而是先写入到内存中的一个缓冲区（buffer）
# 这种机制可以提高性能，因为磁盘I/O操作相对较慢，而内存操作速度更快
# 缓冲区可以暂时存储写入的数据，当缓冲区满了或者文件关闭时，数据才会被写入磁盘
file = open("example.txt","r+")
file.flush()
file.close()

# 文件信息
#
# encoding 返回文件的编码
# mode 返回文件的模式
# name 返回文件名
# tell() 返回文件指针当前的位置
# isatty() 返回 True 表示文件是一个终端
# closed 返回 True 表示文件已关闭
file = open("example.txt","r")
print(file.encoding, file.name, file.mode, file.tell(), file.isatty(), file.closed)
# cp936 example.txt w 0 False
file.close()
print(file.closed) # True


# seek(offset, whence=0)
# offset：偏移量，表示要移动的字节数。
# whence：可选参数，用于指定offset的计算基准
# 0：从文件开头计算（默认值）。
# 1：从当前位置计算。
# 2：从文件末尾计算。
# 如果文件以 'w' 或 'a' 模式打开，尽量避免使用 whence=1
# 如果需要从当前位置移动指针，可以先切换到支持的模式，如 'r+' 或 'a+'
file = open("example.txt","r+")
print(file.tell()) # 0
# 从开始位置向后移动 2 个位置
file.seek(2,0)
# 检查一下
print(file.tell()) # 2
file.close()


# truncate(size=None)
# size：可选参数，表示截断后文件的大小（以字节为单位）
# 如果 size 大于文件当前大小，则文件会被扩展，扩展部分的内容通常为零字节（\x00）
# 如果 size 小于文件当前大小，则文件会被截断，超出 size 的部分会被删除
# 如果不指定 size，则默认使用当前文件指针的位置作为截断点

# 截断
file = open("example.txt", "r+")
# 写入一些内容
file.write("Hello, world!")
# 将文件指针移动到文件开头
file.seek(0) # 即为 file(0,0)
# 截断文件，保留前5个字节的内容
file.truncate(5)
# 将文件指针移动到文件开头，读取内容
file.seek(0)
print("文件内容：", file.read()) # Hello
# 手动关闭文件
file.close()

# 拓展
file = open("example.txt", "r+")
# 写入5个字节的内容
file.write("Hello")
# 将文件指针移动到文件开头
file.seek(0)
# 扩展文件大小到10字节
file.truncate(10)
# 手动关闭文件
file.close()

file = open("example.txt","rb")
print(file.read()) # b'Hello\x00\x00\x00\x00\x00'
file.close()

#################################################################################################
"""

上下文管理
使用 with 来开启文件，这样就不用自己去关闭
程序自己会看情况关闭

"""
#################################################################################################

with open("example.txt", "r") as file:
    content = file.read()
print(content)

#################################################################################################
"""

文件的编码（encoding）
有时输入输出乱码就是因为编码的问题
在读写文件时，尽量明确指定编码，避免依赖默认编码
在项目中尽量统一使用 UTF-8 编码，因为它支持多语言且兼容性较好
如果需要处理二进制文件（如图片、音频等），应使用二进制模式（"rb" 或 "wb"），并避免指定编码

"""
#################################################################################################

# 常见的编码格式
# ASCII
# 仅支持英文字母、数字和符号（共128个字符）。
# 每个字符占1字节，无法表示中文、日文等非拉丁字符。
# UTF-8
# Unicode的实现方式，兼容ASCII，支持全球所有语言
# 英文字符为1字节，中文字符通常3字节（动态长度），互联网标准编码，推荐优先使用。
# GBK/GB2312
# 中文编码标准（GB2312支持简体，GBK扩展支持更多字符）
# 中文字符占2字节，中文Windows系统旧文件常见。
# Latin-1 (ISO-8859-1)
# 西欧语言字符，字节长度为1字节，不支持中文。
# UTF-16/UTF-32
# 定长编码（UTF-16用2或4字节，UTF-32固定4字节）。
# 内存操作优化场景（如Java/C#内部处理）。


# 指定文件编码
# 读取UTF-8文件
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 写入GBK文件
with open("output.txt", "w", encoding="gbk") as f:
    f.write("你好，世界！")


# 编码错误处理
# 当文件编码与指定编码不匹配时，会抛出UnicodeDecodeError。可通过errors参数处理
# 忽略无法解码的字符
with open("file.txt", "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# 替换无法解码的字符为问号
with open("file.txt", "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

#################################################################################################
#################################################################################################