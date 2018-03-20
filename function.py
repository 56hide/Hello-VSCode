#函数
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
# >>> a = abs # 变量a指向abs函数
# >>> a(-1) # 所以也可以通过a调用abs函数
# 1
n = 100
a = hex(n)
b = str(a)
print(b)
# 在Python中，定义一个函数要使用def语句，
# 依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs (x):
    if x >=0:
        return(x)
    else:
        return(-x)

print(my_abs(-100))
# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，
# 用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）：

# 空函数

# 如果想定义一个什么事也不做的空函数，可以用pass语句：

# def nop():
#     pass

# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

# pass还可以用在其他语句里，比如：

# if age >= 18:
#     pass

# 缺少了pass，代码运行就会有语法错误。

# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny #返回多个值

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。

#由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：

# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s

# 这样，当我们调用power(5)时，相当于调用power(5, 2)：

# >>> power(5)
# 25
# >>> power(5, 2)
# 25
#x是未知参数 n是默认参数
# 而对于n > 2的其他情况，就必须明确地传入n，比如power(5, 3)。
# 为什么要设计str、None这样的不变对象呢？
# 因为不变对象一旦创建，对象内部的数据就不能修改，
# 这样就减少了由于修改数据导致的错误。此外，由于对象不变，
# 多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
# 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


#可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# >>> nums = [1, 2, 3]
#若参数已经是一个list或者tuple则通过*num来传参
# >>> calc(*nums)
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，
# 参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

#关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
# >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
# >>> person('Jack', 24, **extra)
#输出name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)


# 命名关键字参数
# def person(name, age, *, city, job):
#     print(name, age, city, job)

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# 调用方式如下：

# >>> person('Jack', 24, city='Beijing', job='Engineer')
# Jack 24 Beijing Engineer

#*****递归函数*******#
# 如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
#最典型的递归函数

# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
# 所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：

# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

# 上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：

# def fact(n):
#     return fact_iter(n, 1)

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
# 可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
# fact(5)对应的fact_iter(5, 1)的调用如下：
# ===> fact_iter(5, 1)
# ===> fact_iter(4, 5)
# ===> fact_iter(3, 20)
# ===> fact_iter(2, 60)
# ===> fact_iter(1, 120)
# ===> 120
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
# 所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。


# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

#move(4, 'A', 'B', 'C')

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取出前三个元素
print(L[0:3])
#同样支持倒数索引，最后一个的索引是-1
#用切片实现trim
def trim(s): 
    if s[:1]==' ': #注意，必须这么写，写成s[0]会在边界条件的时候出错，因为空字符串没有s[0]。但是却可以进行切片操作。 
        return trim(s[1:]) 
    if s[-1:] == ' ': 
        return trim(s[:-1]) 
    return s

#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

# >>> d = {'a': 1, 'b': 2, 'c': 3}
# >>> for key in d:
# ...     print(key)
# ...
# a
# c
# b
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()。
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

# >>> from collections import Iterable
# >>> isinstance('abc', Iterable) # str是否可迭代
# True
# >>> isinstance([1,2,3], Iterable) # list是否可迭代
# True
# >>> isinstance(123, Iterable) # 整数是否可迭代
# False

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

# >>> for i, value in enumerate(['A', 'B', 'C']):
# ...     print(i, value)
def findMinAndMax(L):
    max = L[0]
    min = L[0]
    for i in L :
        if max<i:
            max=i
        if min>i:
            min=i
    result=[max,min]
    print(result)
# L=[1,2,3,4,5,5,6]
# findMinAndMax(L)

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))
# >>> [x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

# >>> [x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

# >>> [m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


# 生成器：generator。
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，
# 只要把一个列表生成式的[]改成()，就创建了一个generator：

# >>> L = [x * x for x in range(10)]
# >>> L
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> g = (x * x for x in range(10))
# >>> g
# <generator object <genexpr> at 0x1022ef630>

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
#遍历生成器g
# g = (x * x for x in range(10))
# for n in g:
#     print(n)

#上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# for n in fib(6):
#     print(n)
    #g = fib(6)
#不能直接print（g）
# >>> g = fib(6)
# >>> g
# <generator object fib at 0x1022ef948>
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator：
# >>> f = fib(6) #输出前六个斐波拉切数
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

# >>> g = fib(6)
# >>> while True:
# ...     try:
# ...         x = next(g)
# ...         print('g:', x)
# ...     except StopIteration as e:
# ...         print('Generator return value:', e.value)
# ...         break
# generator函数的“调用”实际返回一个generator对象：

# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象：
# >>> from collections import Iterable
# >>> isinstance([], Iterable)
# True

# 而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：

# >>> from collections import Iterator
# >>> isinstance((x for x in range(10)), Iterator)
# True
# >>> isinstance([], Iterator)
# False

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

# >>> isinstance(iter([]), Iterator)
# True
# >>> isinstance(iter('abc'), Iterator)
# True

# 你可能会问，为什么list、dict、str等数据类型不是Iterator？

# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# # 小结
# # 凡是可作用于for循环的对象都是Iterable类型；
# # 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# # 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# # Python的for循环本质上就是通过不断调用next()函数实现的，例如：
# # for x in [1, 2, 3, 4, 5]:
# #     pass

# # 实际上完全等价于：

# # # 首先获得Iterator对象:
# # it = iter([1, 2, 3, 4, 5])
# # # 循环:
# # while True:
# #     try:
# #         # 获得下一个值:
# #         x = next(it)
# #     except StopIteration:
# #         # 遇到StopIteration就退出循环
# #         break



#高阶函数：函数作为另一个函数的参数
def add(x, y, f):
    return f(x) + f(y)

#print(add(-5, 6, abs))

def f(x):
    return x * x

# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))
# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比方说对一个序列求和，就可以用reduce实现：
# >>> from functools import reduce
# >>> def add(x, y):
# ...     return x + y
# ...
# >>> reduce(add, [1, 3, 5, 7, 9])
# 25
#filter函数
# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

# def is_odd(n):
#     return n % 2 == 1

# list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

# 把一个序列中的空字符串删掉，可以这么写：

# def not_empty(s):
#     return s and s.strip()

# list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# # 结果: ['A', 'B', 'C']

    
