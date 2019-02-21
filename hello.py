
def hello():
    # print(__name__)
    print("Hello World!")

def test():
    hello()

# 在主程序中__name__的值为“__main__”，作为导入模块时值为 hello,即：模块名
if __name__ == '__main__':
    test()