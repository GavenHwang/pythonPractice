from string import Template

import yaml
import os.path


class Loader(yaml.Loader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)

    def include(self, node):
        filename = os.path.join(self._root, self.construct_scalar(node))
        with open(filename, 'r') as fr:
            return yaml.load(fr, Loader)


Loader.add_constructor('!include', Loader.include)


def load_yaml(file_name):
    """Load YAML file to be dict"""
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as fr:
            dict_obj = yaml.load(fr, Loader=Loader)
        return dict_obj
    else:
        raise FileNotFoundError('NOT Found YAML file %s' % file_name)


def save_yaml(yaml_dict):
    from ruamel import yaml
    with open("result.yaml", 'w', encoding='utf-8') as fw:
        yaml.dump(yaml_dict, fw, Dumper=yaml.RoundTripDumper, allow_unicode=True)


def read_yaml_with_substitute(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as fr:
        value = fr.read()
        temp = Template(value)
        # safe_substitute可以让不想匹配的变量当正常的字符串使用，只匹配需要的变量
        res = temp.safe_substitute({
            'user': 'lily',
            'password': '123456'
        })
        yaml_data = yaml.safe_load(res)
        print(res)
        print(yaml_data)


if __name__ == '__main__':
    # yaml_dict = load_yaml("a/a.yaml")
    # print(yaml_dict)
    # yaml_dict2 = eval(str(yaml_dict))
    # print(yaml_dict2)
    # save_yaml(yaml_dict2)

    read_yaml_with_substitute("substitute.yaml")
