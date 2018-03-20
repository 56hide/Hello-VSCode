# a = 'abc'
# b = a
# a = 'ABC'
# print(b)
# e = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print(s3)
# a = 'ABC'.encode('ascii')
# print(a)
# for i in range(0,5):
#     print(i)
# from random import randint
# i = randint(0,2)
# a = input()
# bingo = True
# while(a==i):
#     print("Bingo")
# num = 10
# print("guess what i think?")
# answer = input()
# if answer<num:
#     print("too small")
# if answer>num:
#     print("too big")
# if answer==num:
#     print("bingo")
# num = 10
# print("Guess  what i think?")
# bingo = False
# while bingo==False:
#     s5 = input()
#     answer = int(s5)
#     if answer < num:
#         print("too small!")
#     if answer > num:
#         print("too big")
#     if answer == num:
#         print("BINGO!")
#         bingo = True

#List类型
# classmate = ['wangyang', 'wangfan', 'renyue']
# classmate.append('liuliang')#在队尾插入元素
# classmate.insert(0,'liangzhehao')#在指定位置插入元素
#classmate.pop(1)#删除指定位置的元素，无参默认删除最后一个元素
#t = (3.14, 'China', 'Jason')#此时t是Tuple类型，不可以改变的列表类型

# for i in range(0,5):
#     print(classmate[i])
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'C#', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][2])


#d是Dict类型，key-value对应的字典类型
# d = {
#     'Adam': 95,
#     'Lisa': 85,
#     'Bart': 59,
#     'Paul': 75
# }
# d['Jone'] = 99
# print (d['Adam'])
# print (d.get('Paul'))
# print(d)
# {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 75}
#遍历Dict
# for key in d : 
#     print (key, ':', d.get(key))
#要删除一个key，用pop(key)方法，对应的value也会从dict中删除d.pop('Bob')


#set类型
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#s = set([1, 2, 3])
#要创建一个set，需要提供一个list作为输入集合：
# s = set(['A', 'B', 'C'])
# >>> a = 'abc'
# >>> b = a.replace('a', 'A')
# >>> b
# 'Abc'
# >>> a
# 'abc'

# 要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：

# ┌───┐                  ┌───────┐
# │ a │─────────────────>│ 'abc' │
# └───┘                  └───────┘

# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：

# ┌───┐                  ┌───────┐
# │ a │─────────────────>│ 'abc' │
# └───┘                  └───────┘
# ┌───┐                  ┌───────┐
# │ b │─────────────────>│ 'Abc' │
# └───┘                  └───────┘

# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

# print ('A' in s) #True
# s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
#tuple
#遍历
# for x in s:
#     print (x[0],':',x[1])
#通过add和remove来添加、删除元素（保持不重复）
# months = set(['Jan','Feb','Mar','Apr','Map','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
# x1 = 'Jan';x2='Sun'
# if x1 in months:
#     print('yes')
# else:
#     print('no')
# if x2 in months:
#     print('x2 : yes')
# else:
#     print('x2 : no')

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# sum = 0
# for i in range(101):
#     sum+=i
# print(sum)

# s = list(range(5))
# for x in s:
#     print(x)#0 1 2 3 4

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)
# from function import my_abs
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
