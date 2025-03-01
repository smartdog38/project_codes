#模块是指.py文件,而不是目录
#导入库的方式
#1.import#导入整个库
#2.from xxx import xxx#导入某个函数
#3.from xxx import *#导入所有的函数
#4.from xxx import xxx as yyy#导入某个函数，并起别名
#5.import xxx as yyy#导入整个库，并起别名
#6.import xxx,yyy,zzz#导入多个库，是  ,
#7.import xxx.yyy.zzz#导入子模块，是  .

#1.import
#import math
#print(math.pi)

#2.from xxx import xxx
#from math import pi
#print(pi)

#3.from xxx import *
#from math import *
#print(pi)

#可以起别名
# from math import pi as PI
# 如果经常使用的模块可以给一个名字
# fib = fibo.fib


#当引入另一模块，不希望其中的某一程序在当前模块中运行，使用__name__属性来使该程序块仅在该模块自身运行时执行
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')

#dir()#查看当前模块的所有变量
#dir(fibo)
#如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称

#创建总模块与子模块（另,这在python3.3后并不直接需要init文件来识别，可以直接导入）
#在文件夹下创建子文件夹并创建一个__init__.py文件，为了将其识别为一个模块文件。子文件夹也是需要创建__init__.py文件的。
#__init__.py文件是一个空文件，但是它必须存在，否则Python将无法导入该模块。但其可以包含一些属实话所需要的东西

#__all__ = ['fibo', 'fibo2']
# __all__ 只能在 * 的条件下才能限制
#__all__代表被导入的模块可以被外部访问的东西，
# 如果在模块内没有设置__all__，默认情况下，所有的函数都可以被外部访问
#在总模块中，可以使用from xxx import *来导入子模块中的函数
#这样就可以在总模块中使用子模块中的函数了
#即当调用总模块时可以直接调用子模块中的函数，不需要再加.来调用子模块


# 需要这些文件 __init__.py 才能使 Python 将包含该文件的目录视为包（不再适用，但有些需要初始化的时候可以用）
# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py

#导入单个模块
# import sound.effects.echo

# 使用 from package import item 时，
# 项可以是包的子模块（或子包），也可以是包中定义的其他名称，如函数、类或变量。

# 当使用类似 import item.subitem.subsubitem 的语法时，
# 除最后一个项外，每个项都必须是一个包;最后一项可以是模块或包，但不能是上一项中定义的类、函数或变量

