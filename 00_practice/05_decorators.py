# -*- coding:utf-8 -*-


# 不带参数的注解
def spamrun(fn):
    def sayspam(a, b):
        a += 1
        b += 1
        fn(a, b)
    return sayspam


@spamrun
def useful(a, b):
    print(a * b)


# 带参数的注解
def attrs(**kwargs):
    def decorate(f):
        for k in kwargs:
            setattr(f, k, kwargs[k])
        return f
    return decorate


@attrs(versionadded="2.2", author="Guido van Rossum")
def mymethod(f):
    print('versionadded: ', getattr(mymethod, 'versionadded', 0))
    print('author: ', getattr(mymethod, 'author', 0))
    print(f)


class A:
    @classmethod
    def b(cls):
        print(cls.__name__)


class B(A):
    @classmethod
    def b(cls):
        print("--B继承A--")
        return super(B, cls).b()


if __name__ == '__main__':
    useful(2, 3)
    mymethod("你好")
    A().b()
    B().b()