s = ' STR INGS '
s_1 = "String"
s_2 = '''
d
a
b
c
'''
s_4 = r"C/dsad/dasd/" # r 表示原始字符串，不会进行转义
# \n \t \r


print(s) # STRING
print(s_1)  # string
print(s_2)  # a
            # b
            # c
            # d
'''
多行的注释，不是多行字符串
'''
print(s_4)  # C/dsad/dasd/

# 格式化
print(f"String{s_1}") # StringString  !!
print("String{0}".format(s_1)) # StringString
print("String {name}".format(name=s_1)) # String string


# 切片
print(s_1[0:2]) # St ,切片
print(s_1[0:]) # string
print(s_1[:2]) # St
print(s_1[0]) # S
print(s_1[-1]) # g
print(s_1[0:4:2]) # Sr, 步长为2

# 函数
print(s.find('S')) # 有，给出第一个的位置，无返回-1
print(s.index('S')) # 有，给出第一个的位置，无报错
print(s.startswith("S"))  # True,以 S 开头
print(s.endswith('NG')) # True,以 NG 结尾
print(s.count('R')) # 1

print(s.isalnum()) # True
print(s.isalpha()) # True
print(s.isdigit()) # False
print(s.islower()) # False
print(s_1.isupper()) # 全为大写才为True

print('x'.join(['a','b','c'])) # axbxc
print(s.split(' ')) # ['','STR', 'INGS','']

print(s_1.upper()) # STRING
print(s.lower()) # string
print(s_1.swapcase()) # sTRING
print(s.title()) # 首字母大写，其余转换为小写

print(s.lstrip()) # 去除左边的空格
print(s.rstrip()) # 去除右边的空格
print(s.strip())  # 去除两边的空格

print(s.replace('S','s'))

print(s+s_1+' ss') # 默认+不添加空格
print(s==s_1) # False,按 ASCLL码 比较
print("ss" in s)  # False