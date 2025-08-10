print('\n')
########## 1. 条件语句 if elif else
# a = 1
# if a == 1:
#     print('\na == 1')
# elif a == 2:
#     print('\na == 2')
# else:
#     print('\na == 3')

######## 2. 循环 while， for
# tup = (13, 21, 31)
#
# for i in tup:
#     print(i)
#
# for i in range(len(tup)):
#     print(tup[i])
#
# a = 0
# while a < len(tup):
#     print(tup[a])
#     a += 1

######### 3. 推导式
print([i for i in range(50) if i % 5 == 0])

listmode = ["shi", "quan", "sen"]
newdict = {key: len(key) for key in listmode if len(key) > 3}
print(newdict)
