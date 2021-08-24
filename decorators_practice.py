# -*- coding:utf-8 -*-

# 不带参数的注解
def spamrun(fn):
    def sayspam(*args):
        print("spam,spam,spam")
        fn(*args)

    return sayspam


@spamrun
def useful(a, b):
    print(a * b)


# useful(2, 5)


# 带参数的注解
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f

    return decorate


@attrs(versionadded="2.2", author="Guido van Rossum")
def mymethod(f):
    print(getattr(mymethod, 'versionadded', 0))
    print(getattr(mymethod, 'author', 0))
    print(f)


# mymethod(2)


class A:
    @classmethod
    def b(cls):
        print(cls.__name__)


class B(A):
    @classmethod
    def b(cls):
        print("--B继承A--")
        return super(B, cls).b()


A.b()
B.b()
