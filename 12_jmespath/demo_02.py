import jmespath


class TstJmesPath(object):

    def __init__(self):
        self.data = {
            "book": [
                {"name": "平凡的世界", "author": "路遥", "sort": 3},
                {"name": "围城", "author": "钱钟书", "sort": 2},
                {"name": "围城", "author": "钱钟书", "sort": 2},
                {"name": "活着", "author": "余华", "sort": 1},
                {"name": "麦田里的守望者", "author": "塞林格", "sort": 4},
                {"name": "挪威的森林", "author": "村上春树", "sort": 5}
            ]
        }

    def tst_keys(self):
        """提取对象的 key """
        result = jmespath.search("book[0].name", self.data)
        return result

    def tst_values(self):
        """提取对象的 value，不接受数组"""
        result = jmespath.search("book[0] | values(@)", self.data)
        return result

    def tst_sort(self):
        """根据 sort 进行排序"""
        result = jmespath.search("book[*].sort | sort(@)", self.data)
        return result

    def tst_sort2(self):
        result = jmespath.search("book[*].author | sort(@) | [join(', ', @)]", self.data)
        return result

    def tst_type(self):
        result = jmespath.search("book[*].name | type(@)", self.data)
        return result

    def tst_type2(self):
        result = jmespath.search("book[0].name | type(@)", self.data)
        return result

    def tst_to_string(self):
        result = jmespath.search('[].to_string(@)', [1, 2, 3, "number", True])
        return result

    def tst_to_number(self):
        result = jmespath.search('[].to_number(@)', ["1", "2", "3", "number", True])
        return result

    def tst_contains(self):
        result = jmespath.search("contains(`foobar`, `foo`)", {})
        return result

    def tst_contains2(self):
        result = jmespath.search("contains(`foobar`, `f123`)", {})
        return result

    def tst_join(self):
        # expected one of: ['array-string']
        # @ 为当前节点，得到的结果用逗号加空格分隔，然后放在当前节点下
        result = jmespath.search("join(`, `, @)", ["a", "b"])
        return result

    def tst_length(self):
        result = jmespath.search("length(@)", ["a", "b"])
        return result

    def tst_max(self):
        result = jmespath.search("max(@)", [10, 3, 5, 5, 8])
        return result

    def tst_min(self):
        result = jmespath.search("min(@)", [10, 3, 5, 5, 8])
        return result


if __name__ == '__main__':
    obj = TstJmesPath()
    print(1, obj.tst_keys())
    print(2, obj.tst_values())
    print(3, obj.tst_sort())
    print(4, obj.tst_sort2())
    print(5, obj.tst_type())
    print(6, obj.tst_type2())
    print(7, obj.tst_to_string())
    print(8, obj.tst_to_number())
    print(9, obj.tst_contains())
    print(10, obj.tst_contains2())
    print(11, obj.tst_join())
    print(12, obj.tst_length())
    print(13, obj.tst_max())
    print(14, obj.tst_min())
