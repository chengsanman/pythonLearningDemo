######## 1. with语句可以自己关闭资源池
import time

with open('/Users/apple/PycharmProjects/pythonLearningDemo/resource/a.txt', 'r') as file:
    print(file.read())

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(self.end - self.start)
        print(f"耗时：{self.end - self.start:.2f}秒")
        return True

with Timer() as t:
    sum(range(10000000))