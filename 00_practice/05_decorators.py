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


def post_execution_decorator(post_func):
    def decorator(main_func):
        def wrapper(*args, **kwargs):
            # 执行主方法
            result = main_func(*args, **kwargs)
            # 执行注解方法
            post_func(*args, **kwargs)
            return result

        return wrapper

    return decorator


# 定义一个在方法执行后执行的注解方法
def my_post_execution(*args, **kwargs):
    print("方法执行后，自动执行此注解方法")
    print(f"传递给主方法的参数: args={args}, kwargs={kwargs}")


# 使用装饰器
@post_execution_decorator(my_post_execution)
def my_method(a, b):
    print(f"执行主方法: a={a}, b={b}")
    return a + b


if __name__ == '__main__':
    useful(2, 3)
    mymethod("你好")
    A().b()
    B().b()
    # 调用方法
    result = my_method(3, 4)
    print(f"主方法返回值: {result}")
