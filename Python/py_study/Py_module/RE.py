#################################################################################################
#################################################################################################
"""

re module
提供了正则表达式操作的核心功能，用于字符串的匹配、搜索、替换和分割等操作

"""
#################################################################################################
"""

匹配语法

"""
#################################################################################################

# .：匹配任意字符（除换行符）
# \d：数字，等价于 [0-9]
# \w：字母、数字、下划线
# \s：空白字符（空格、制表符等）
# ^：字符串开头
# $：字符串结尾
# *：匹配前一个字符0次或多次
# +：匹配前一个字符1次或多次
# ?：匹配前一个字符0次或1次
# {n}：匹配前一个字符n次
# [...]：字符集（如 [a-z] 匹配小写字母）
# (abc)：分组，用于捕获匹配的部分

# 在下面的函数会进行演示

#################################################################################################
"""

常用查找函数

"""
#################################################################################################

# 第一个
# re.match(pattern, string)
# re.search(pattern, string)
# 全部
# re.findall(pattern, string)
# re.finditer(pattern, string)

import re


# re.match(pattern, string)
# 用于从<开头>进行匹配,匹配到返回 match 对象，未匹配返回 None
# 常用与检验无是否为 http 开头
string = "abc111223df"
parttern_1 = "abc"
parttern_2 = "111223"
match_1 = re.match(parttern_1,string)
match_2 = re.match(parttern_2,string)
# 检验是否匹配
if match_1:
    # 用 group() 返回匹配的字符串
    print(match_1.group())
else:
    print("None")
# abc

if match_2:
    print(match_2.group())
else:
    print("None")
# None


# re.search(pattern, string)
# 不同与 match() ，它是从全局进行搜索，同样返回 match 对象，为匹配返回None
string = "abc111223df"
# 匹配单个数字
parttern_1 = r"\d"
# 匹配多个小写字母
parttern_2 = r"[a-z]*"
match_1 = re.search(parttern_1,string)
match_2 = re.search(parttern_2,string)
if match_1:
    # 用 group() 返回匹配的字符串
    print(match_1.group())
else:
    print("None")
# 1
# 不会返回其他的数字，只会返回第一个匹配的

if match_2:
    print(match_2.group())
else:
    print("None")
# abc


# re.findall(pattern, string)
# 用于在字符串中搜索所有非重叠的匹配项
# 如果正则表达式无分组：返回所有完整匹配字符串的列表
# 无匹配时返回空列表 []
text = "a1b22c333"
# 匹配所有连续数字
matches = re.findall(r'\d+', text)
print(matches)  # 输出: ['1', '22', '333']


# re.finditer(pattern, string)
# 用于在字符串中搜索所有非重叠的匹配项，并返回一个包含所有 Match 对象的迭代器
# 与 re.findall() 不同，finditer() 不会一次性将所有匹配结果加载到内存中，而是逐个生成 Match 对象
# 适合处理大文本或需要逐项操作的场景
text = "a1b22c333"
# 返回迭代器
matches = re.finditer(r'\d+', text)
for match in matches:
    print(match.group())  # 依次输出: "1", "22", "333"

#################################################################################################
"""

替换与分割

"""
#################################################################################################

import re


# re.sub(pattern, repl, string)
# 替换所有数字为X
new_str = re.sub(r'\d+', 'X', 'a1b22c333')
print(new_str)  # aXbXcX


# re.split(pattern, string)
# 按数字分割
parts = re.split(r'\d+', 'a1b22c333')
print(parts)  # ['a', 'b', 'c', '']

#################################################################################################
"""

分组（Grouping） 和 捕获（Capturing）
允许你从匹配的文本中提取特定部分
或在替换操作中引用这些部分

"""
#################################################################################################
import re



# 基础分组 ( )

# match 对象分组
# 用圆括号 () 将部分正则表达式包裹，形成一个分组
# 分组会捕获匹配的内容，后续可通过索引或名称引用
text = "2023-10-25"
# 年、月、日分组
pattern = r'(\d{4})-(\d{2})-(\d{2})'
match = re.search(pattern, text)

if match:
    print(match.group(0))  # 完整匹配: "2023-10-25"
    print(match.group(1))  # 第1组: "2023" (年)
    print(match.group(2))  # 第2组: "10" (月)
    print(match.groups())  # 所有分组元组: ('2023', '10', '25')


# 如果是findall()
# 会有两个方式
# 匹配单个分组
text = "2023-10-25, 2024-12-31"
# 正则表达式包含一个分组 (\d{4})，匹配年份
matches = re.findall(r'(\d{4})-\d{2}-\d{2}', text)
print(matches)  # ['2023', '2024'] （只返回分组内容）

# 匹配多个分组，会返回元组列表
text = "Name: Alice, Age: 30; Name: Bob, Age: 25"
# 正则表达式包含两个分组：(\w+) 和 (\d+)
matches = re.findall(r'Name: (\w+), Age: (\d+)', text)
print(matches)  # [('Alice', '30'), ('Bob', '25')]


# 非捕获分组 (?: )
# 用 (?:...) 定义分组，但不捕获内容，避免占用分组索引
# 需要分组但不需后续引用时
text = "https://www.example.com"
pattern = r'(?:http|https)://([\w.-]+)'  # 协议部分不捕获
match = re.search(pattern, text)
if match:
    print(match.group(1))  # 输出域名: "www.example.com"


 # 命名分组 (?P<name> )
# 通过 (?P<name>...) 为分组命名，提高代码可读性
# 通过名称（group('name')）或索引访问
text = "Date: 2023-10-25"
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, text)
if match:
    print(match.group('year'))   # "2023"
    print(match.group(1))        # "2023"
    # 实际是会生成一个列表来存储命名与捕获的值
    print(match.groupdict())     # {'year': '2023', 'month': '10', 'day': '25'}

#################################################################################################
"""

分组的应用

"""
#################################################################################################

import re


# 提取子内容
text = "Name: John, Age: 30"
match = re.search(r'Name: (\w+), Age: (\d+)', text)
if match:
    name = match.group(1)  # "John"
    age = match.group(2)   # "30"


# 替换匹配字符串
text = "2023-10-25"
# 将日期格式从 "YYYY-MM-DD" 改为 "MM/DD/YYYY"
new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', text)
print(new_text)  # "10/25/2023"


# 条件匹配
# 有点像 if 就进行分组捕获
# 匹配 "Mr. Smith" 或 "Ms. Smith"，但不捕获 "Mr"/"Ms"
text = "Mr. Smith"
pattern = r'(?:Mr|Ms)\. (\w+)'
match = re.search(pattern, text)
print(match.group(1))  # "Smith"


# 嵌套分组
# 分组的索引按左括号出现的顺序分配
text = "12:30:45"
# 外层分组1，内层分组2、3，分组4
pattern = r'((\d{2}):(\d{2})):(\d{2})'
match = re.search(pattern, text)
if match:
    print(match.groups())  # ('12:30', '12', '30', '45')

#################################################################################################
"""

Match 对象

"""
#################################################################################################

import re


# 刚刚的 match 对象会有下面的操作函数
# group()
# groups()
# groupdict()
# start() 和 end()
# span()


# group()
# 返回匹配的字符串或指定分组的字符串
# group=0：默认返回整个匹配的字符串
# group=N：返回第 N 个分组的字符串（分组索引从 1 开始）
# group='name'：返回命名分组的字符串（需使用 (?P<name>...) 语法）
text = "Date: 2023-10-25"
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(pattern, text)

# 获取完整匹配内容
print(match.group())      # "2023-10-25"（等价于 group(0)）
# 获取第1个分组
print(match.group(1))     # "2023"
# 获取命名分组
print(match.group('year'))  # "2023"


# groups()
# 返回所有分组的字符串组成的元组（索引从 1 开始）
# default=None：如果分组未匹配到内容，返回 default 值（默认为 None）
text = "Date: 2023-10-25"
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
print(match.groups())  # ('2023', '10', '25')


# gruopdict()
# 返回所有命名分组的字符串组成的字典
# default=None：如果分组未匹配到内容，返回 default 值
text = "Date: 2023-10-25"
pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
print(match.groupdict())  # 输出: {'year': '2023', 'month': '10', 'day': '25'}


# start() 与 end()
# 返回匹配的子字符串在原始字符串中的起始索引和结束索引
# group=0：默认针对整个匹配内容，可指定分组索引或名称
text = "abc123def"
match = re.search(r'\d+', text)  # 匹配 "123"

print(match.start())  # 3（"123" 的起始索引,即 "1" 的索引）
print(match.end())    # 6（"123" 的结束索引,即 "3" 的索引）
print(text[match.start():match.end()])  # "123"

# 指定分组
match = re.search(r'(\d)(\d+)', text)  # 分组1: "1", 分组2: "23"
print(match.start(2))  # 4（分组2 "23" 的起始索引）


# span()
# 返回匹配的子字符串在原始字符串中的范围，格式为 (start, end)
print(match.span())      # (3, 6)
print(match.span(1))    # (3, 4)（分组1 ,"1" 的范围）

#################################################################################################
"""

贪婪匹配(Greedy Matching)与非贪婪匹配(Non-Greedy Matching)
贪婪匹配和非贪婪匹配是两种不同的匹配模式，它们决定了正则表达式在匹配字符串时的行为

贪婪匹配是正则表达式的默认模式
在这种模式下，正则表达式会尝试匹配尽可能多的字符

非贪婪匹配（也称为懒惰模式或惰性模式）与贪婪匹配相反
在这种模式下，正则表达式会尝试匹配尽可能少的字符

"""
#################################################################################################

import re



# 贪婪匹配
# 量词默认是贪婪的，会尽可能匹配最长可能的字符串
# 量词形式：*、+、{n,m}（不加 ?）
text = "<div>content1</div><div>content2</div>"
text_2 = "abbbbbbbaaa"
text_3 = "acaabbbbbcccaaacccaaaacccaaa"

# 贪婪匹配：匹配从第一个 <div> 到最后一个 </div>
matches = re.findall(r'<div>.*</div>', text)
print(matches)  # ['<div>content1</div><div>content2</div>']
matches_2 = re.findall(r'a.*a',text_2)
print(matches_2) # ['abbbbbbbaaa']
matches_3 = re.findall(r'a.*c',text_3)
print(matches_3) # ['acaabbbbbcccaaacccaaaaccc']

# 可以这么理解，找到第一个 a，找到最后一个 c，来匹配


# 非贪婪匹配
# 启用方式：在量词后添加 ?，使其尽可能匹配最短可能的字符串
# 量词形式：*?、+?、??、{n,m}?
# 非贪婪匹配：匹配每个 <div>...</div> 块
text = "<div>content1</div><div>content2</div>"
text_2 = "abbbbbbbaaa"
text_3 = "acaabbbbbcccaaacccaaaacccaaa"

matches = re.findall(r'<div>.*?</div>', text)
print(matches)  # 输出: ['<div>content1</div>', '<div>content2</div>']
matches_2 = re.findall(r'a.*?a',text_2)
print(matches_2) # ['abbbbbbba', 'aa']
matches_3 = re.findall(r'a.*?c',text_3)
print(matches_3) # ['ac', 'aabbbbbc', 'aaac', 'aaaac']

# 可以这么理解找到 第一个 a，再顺着找到第一个 c，返回一个匹配
# 然后接着找下一个的第一个 a，然后再找第一个 c，继续返回匹配
# 'aaac' 就是这个逻辑

#################################################################################################
"""

Flags
标志（Flags） 用于控制正则表达式的匹配行为
例如是否区分大小写、是否支持多行匹配等

"""
#################################################################################################

# 常见的 Flag

# re.IGNORECASE	re.I	忽略大小写匹配
# re.MULTILINE	re.M	使 ^ 和 $ 匹配每行的开头和结尾（而非整个字符串的开头和结尾）
# re.DOTALL	    re.S    让 . 匹配包括换行符 \n 在内的所有字符
# re.VERBOSE	re.X	允许在正则中添加注释和换行（提高可读性）
# re.ASCII	    re.A    让 \w, \d, \s 等仅匹配 ASCII 字符（默认可能匹配 Unicode，如中文）
# re.UNICODE	re.U	明确让 \w, \d 等匹配 Unicode 字符（Python 3 默认启用，可忽略此标志）

import re



# re.IGNORECASE	re.I
text = "Python python PYTHON"
# 不区分大小写匹配 "python"
matches = re.findall(r'python', text, flags=re.I)
print(matches)  # ['Python', 'python', 'PYTHON']


# re.MULTILINE (re.M)
text = "Line 1\nLine 2\nLine 3"
# 匹配每行开头的 "Line"
matches = re.findall(r'^Line', text, flags=re.M)
print(matches)  # ['Line', 'Line', 'Line']

# 匹配每行结尾的数字
matches = re.findall(r'\d$', text, flags=re.M)
print(matches)  # ['1', '2', '3']


# re.DOTALL (re.S)
text = "start\nend"
# 默认情况下，. 不匹配换行符
match = re.search(r'start.*end', text)
print(match)  # None

# 启用 DOTALL 标志
match = re.search(r'start.*end', text, flags=re.S)
print(match.group())  # "start\nend"


# re.VERBOSE (re.X)
# 复杂正则表达式添加注释
pattern = re.compile(r'''
    ^(\d{4})       # 年份（4位数字）
    -(\d{2})        # 月份（2位数字）
    -(\d{2})        # 日期（2位数字）
    \s+             # 空白字符
    (\d{2}:\d{2})   # 时间（HH:MM）
''', flags=re.X)

text = "2023-10-25 14:30"
match = pattern.search(text)
if match:
    print(match.groups())  # ('2023', '10', '25', '14:30')


# re.ASCII (re.A)
text = "中国 123"
# 默认匹配 Unicode 字符（\w 包含中文）
matches = re.findall(r'\w+', text)
print(matches)  # 输出: ['中国', '123']

# 启用 ASCII 标志（\w 仅匹配英文、数字、下划线）
matches = re.findall(r'\w+', text, flags=re.A)
print(matches)  # 输出: ['123']


# re.UNICODE (re.U)
# Python 3 默认行为（无需显式指定）
text = "日本語 123"
matches = re.findall(r'\w+', text)
print(matches)  # 输出: ['日本語', '123']



# 使用 | 运算符组合多个标志
text = "Start\nLine 1\nLine 2"
# 同时启用 MULTILINE 和 IGNORECASE
matches = re.findall(r'^line', text, flags=re.M | re.I)
print(matches)  # ['Line', 'Line']

#################################################################################################
"""

预编译
re.compile() 是一个关键函数，用于预编译正则表达式，生成一个正则表达式对象（Pattern 对象）
预编译后的对象可以重复使用，提高效率，尤其在多次调用同一正则表达式时效果显著

如果正则表达式只使用一次，直接使用 re.match()、re.search() 等函数更简洁

"""
#################################################################################################

# 基本用法
# re.compile(pattern, flags=0)
# pattern: 正则表达式字符串（建议使用原始字符串 r''）
# flags: 可选标志（如 re.IGNORECASE、re.MULTILINE 等），控制匹配行为

import re



# 预编译正则表达式（匹配邮箱）
pattern = re.compile(r'\b[\w.-]+@[\w.-]+\.\w+\b')

text = "Contact: user@example.com, backup: admin@site.org"
# 使用编译后的对象进行搜索
match = pattern.search(text)
if match:
    print(match.group())  # "user@example.com"

# 查找所有匹配
emails = pattern.findall(text)
print(emails)  # ['user@example.com', 'admin@site.org']


# 结合 Flag
# 预编译正则（忽略大小写 + 多行模式）
pattern = re.compile(r'^hello', flags=re.IGNORECASE | re.MULTILINE)

text = "HELLO\nhello\nhi"
matches = pattern.findall(text)
print(matches)  # 输出: ['HELLO', 'hello']



# 应用

texts = ["abc123", "def456", "ghi789"] * 1000  # 3000 条数据

for text in texts:
    re.search(r'\d+', text)  # 每次调用都解析正则
# 预编译
pattern = re.compile(r'\d+')  # 仅解析一次

for text in texts:
    pattern.search(text)      # 直接使用编译后的对象

#################################################################################################
#################################################################################################