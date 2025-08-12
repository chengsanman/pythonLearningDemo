############ 1. 装饰器模式 （有点像是动态代理） ############

## 简单的就是说程序要使用 say_hello() 这个函数
# 正常情况下直接调用就好
# 但是我们需要在sayhello前后去做一些事，比如日志记录，入库，鉴权等等
# 简单做法就是在这块代码前后直接加对应的代码块，实际上可以把sayhello当作一个参数
# 我们设计一个函数 传参数sayhello 执行为 before-sayhello()-after，返回sayhello,有点类似 java中动态代理的实现

def my_decorator(func):
    print("在原函数之前执行")
    func()
    print("在原函数之后执行")
    return func


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
