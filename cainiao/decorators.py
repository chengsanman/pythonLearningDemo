############ 1. 装饰器模式 （有点像是动态代理） ############

def my_decorator(func):
    def wrapper():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
