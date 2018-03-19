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
classmate = ['wangyang', 'wangfan', 'renyue']
classmate.append('liuliang')#在队尾插入元素
classmate.insert(0,'liangzhehao')#在指定位置插入元素
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
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 75
}
d['Jone'] = 99
print (d['Adam'])
print (d.get('Paul'))
# print(d)
# {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 75}
#遍历Dict
for key in d : 
    print (key, ':', d.get(key))

#set类型
# s = set(['A', 'B', 'C'])
# print ('A' in s) #True
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
#tuple
#遍历
for x in s:
    print (x[0],':',x[1])
#通过add和remove来添加、删除元素（保持不重复）
months = set(['Jan','Feb','Mar','Apr','Map','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Jan';x2='Sun'
if x1 in months:
    print('yes')
else:
    print('no')
if x2 in months:
    print('x2 : yes')
else:
    print('x2 : no')

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

