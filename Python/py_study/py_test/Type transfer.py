#  类型转换
a = 1
int(a) # 1
float(a)  # 1.0
str(a)  # '1'
bool(a)  # True
bytes(a)  # b'1'
hex(a)  # '0x1'
oct(a)  # '0o1'
bin(a)  # '0b1'
chr(a)  # '1'

# 类型判断
isinstance(a,int) # a 是 int 类型，返回 True；a 不是，返回 False
isinstance(a,(int,str)) # a 是 int 或 str 类型，返回 True；a 不是，返回 False
issubclass(a,int) # a 是 int 类型的子类，返回 True；a 不是，返回 False
issubclass(a,(int,str)) # a 是 int 或 str 类型的子类，返回 True；a 不是，返回 False

