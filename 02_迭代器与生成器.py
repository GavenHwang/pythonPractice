# -*- coding:utf-8 -*-
import sys


print(max(['2018-01-01', '2017-12-12', '2016-12-12', '']))

# 输出迭代器的下一个元素
list = [6, 2, 3, 4]
it = iter(list)
print(next(it))

# 利用迭代器对象遍历
list = [1, 2, 3, 5]
it = iter(list)
for x in it:
    print(x, end=" ")


# 类实现迭代功能
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x, end=' ')
print()

# 生成器函数 - 斐波那契
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
