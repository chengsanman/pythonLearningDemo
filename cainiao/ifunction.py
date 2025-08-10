############ 函数

# python 中有两种函数，一种是类似print这类的普通函数，一种是带双下滑的魔术函数，也叫钩子函数
#所有的钩子函数
#方法	                说明	                                                                                触发方式

# 创建和销毁
# __new__(cls, ...)	    在 __init__ 之前被调用，用于 创建实例。它是一个静态方法，必须返回一个实例。很少需要重写。	    创建对象时 MyClass()
# __init__(self, ...)	构造函数，用于初始化新创建的对象。这是最常用的。	                                        对象创建后自动调用
# __del__(self)	        析构函数，当对象的引用计数变为零时被调用。由于垃圾回收时机不确定，不推荐依赖它来做关键的清理工作。	del obj 或垃圾回收

# 字符串
# __str__(self)	        用于为对象提供一个 对用户友好的、易读的 字符串表示。	                                    print(obj), str(obj)
# __repr__(self)	    用于为对象提供一个 明确的、对开发者友好的 字符串表示，理想情况下，                             eval(repr(obj)) == obj。

# 容器和迭代器
# __len__(self)	                    返回容器中元素的数量。	                                                    len(obj)
# __getitem__(self, key)	        获取指定键或索引对应的元素。	                                                obj[key]
# __setitem__(self, key, value)	    设置指定键或索引对应的元素。	                                                obj[key] = value
# __delitem__(self, key)	        删除指定键或索引对应的元素。	                                                del obj[key]
# __iter__(self)	                返回一个迭代器对象（通常是 self）。	                                        for item in obj, iter(obj)

# 数值运算
# 算术运算符
#   __add__(self, other)	        加法	        self + other
#   __sub__(self, other)	        减法	        self - other
#   __mul__(self, other)	        乘法	        self * other
#   __truediv__(self, other)	    除法	        self / other
#   __pow__(self, other)	        幂运算	    self ** other

# 比较运算符
#   __eq__(self, other)	            等于	        self == other
#   __ne__(self, other)	            不等于	    self != other
#   __lt__(self, other)	            小于	        self < other
#   __gt__(self, other)	            大于	        self > other
#   __le__(self, other)	            小于等于	    self <= other
#   __ge__(self, other)	            大于等于	    self >= other

# 属性访问控制
#   __getattr__(self, name)	        当试图访问一个 不存在 的属性时被调用。	                    obj.non_existent_attribute
#   __getattribute__(self, name)	无条件地 拦截所有属性访问。非常强大但也容易出错，要小心使用。	    obj.any_attribute
#   __setattr__(self, name, value)	无条件地 拦截所有属性赋值。	                                obj.any_attribute = value
#   __delattr__(self, name)	        无条件地 拦截所有属性删除。	                                del obj.any_attribute

# 可调用对象
#   __call__(self, ...)	            允许一个类的实例像函数一样被调用。	                        obj(...)

# 上下文管理协议
# __enter__(self)	                            进入 with 语句块时调用，返回值会赋给 as 后面的变量。	        with obj as f:
# __exit__(self, exc_type, exc_val, exc_tb)	    退出 with 语句块时调用，用于清理资源。如果 with 块中发生异常，
#                                               异常信息会作为参数传入。	                                with 块结束或发生异常时


################## 1. py中和java一样，传入不可变类型时是不会改变的， 传入数组字典这类也可能改变内部
# def new_dict(old_dict):
#     old_dict = {}
#     return
#
# old_dict = {'key1': 'value1', 'key2': 'value2'}
# print(id(old_dict))
# new_dict(old_dict)
# print(id(old_dict))


##################2. 参数
# 必需参数
# def printme1(str):
#     print(str)
#     return

# 关键字参数（指定时可以不按顺序传参）
# def printme(str1):
#     "打印任何传入的字符串"
#     print(str1)
#     return
#
# printme(str1="菜鸟教程")

# 默认参数
# def printinfo( name, age = 35 ):
#     "打印任何传入的字符串"
#     print ("名字: ", name)
#     print ("年龄: ", age)
#     return
#
# #调用printinfo函数
# printinfo( age=50, name="runoob" )
# print ("------------------------")
# printinfo( name="runoob" )


# 不定长参数 单个星号是元组形式，两个是字典
# def printinfo1( arg1, *vartuple ):
#     "打印任何传入的参数"
#     print ("输出: ")
#     print (arg1)
#     print (vartuple)
#     print (type(vartuple))
# printinfo1(70, 60, 50)
#
# def printinfo2( arg1, **vardict ):
#     "打印任何传入的参数"
#     print ("输出: ")
#     print (arg1)
#     print (vardict)
#     print(type(vardict))
# printinfo2(1, a=2,b=3)

# lambda匿名函数
# x = lambda a : a + 10
# print(x(5))


