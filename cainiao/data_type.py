########## 1. 数据类型： python 大类型有，number，string，boolean，list，dictionary，tuple

# number 两种类型 int 和 float complex
# a, b, c = 1, 1.1, 1 + 2j
# print(type(a), type(b), type(c))

# str
#a, b = '123', "456"
#print(a, b, type(a))

# bool bool是int的子类,这里不能使用isinstance（不能判断基本类型）判断，需要使用is
# a, b = True, False
# print(a, b, type(a))


# list
# list = ['runoob', 786, 2.23, 'john', 70.2]
# tinylist = [123, 'john']
# print(list)  # 输出完整列表
# print(list[0])  # 输出列表的第一个元素
# print(list[1:3])  # 输出第二个至第三个元素
# print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
# print(tinylist * 2)  # 输出列表两次
# print(list + tinylist)  # 打印组合的列表
# print(type(list))
# print("###########################")

#tuple
# tupletuple = ('runoob', 786, 2.23, 'john', 70.2)
# tinytuple = (123, 'john')
# print(tuple)  # 输出完整元组
# print(tuple[0])  # 输出元组的第一个元素
# print(tuple[1:3])  # 输出第二个至第四个（不包含）的元素
# print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素
# print(tinytuple * 2)  # 输出元组两次
# print(tuple + tinytuple)  # 打印组合的元组
# print(type(tuple))
# print("###########################")

#dict
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
# tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}
# print(dict['one'])  # 输出键为'one' 的值
# print(dict[2])  # 输出键为 2 的值
# print(tinydict)  # 输出完整的字典
# print(tinydict.keys())  # 输出所有键
# print(tinydict.values())  # 输出所有值
# print(type(dict))
# print("###########################")

################# 2. type 和 isinstance区别在于type区别同类，isinstance不区别
# class a:
#     pass
# class b(a):
#     pass
#
# print(type(b) == type(a))
# print(isinstance(b, a))

################## 3. 数值运算
##### + - * /
# print(1 + 2)
# print(1 - 2)
# print(2 * 2)
# print(int(10 / 3))


################# 4. 数据转化
print(int(3.30001))
print(float(3))

print(str(3.30001))
print(eval('5 + 6'))
print(tuple('123123'))
print(list('123123'))
print(set('123123'))
print(dict([('one', 1), ('two', 2), ('three', 3)]) )

#### 不可变集合
print(frozenset(list('123123')))
print(chr(65))
print(ord('A'))
print(hex(100000))
print(oct(13))


