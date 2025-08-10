############## 1. 迭代器和生成器 ############# iter - yield
# list1 = [1, 2, 3, 8, 10]
# it = iter(list1)
#
# ### 迭代
# # for e in it:
# #     print(e)
# print(next(it), next(it), next(it), next(it), next(it), next(it))

def countdown(n):
    while n > 0:
        yield n
        n -= 1

# 创建生成器对象
generator = countdown(5)

# 通过迭代生成器获取值
print(next(generator))  # 输出: 5
print(next(generator))  # 输出: 4
print(next(generator))  # 输出: 3
print(next(generator))  # 输出: 3
print(next(generator))  # 输出: 3

# 使用 for 循环迭代生成器
# for value in generator:
#     print(value)  # 输出: 2 1