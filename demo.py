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
num = 10
print("Guess  what i think?")
bingo = False

while bingo==False:
    answer = input()
    if answer < num:
        print("too small!")
    if answer > num:
        print("too big")
    if answer == num:
        print("BINGO!")
        bingo = True
    

