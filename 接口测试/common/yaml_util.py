import os
import yaml


class YamlUtil(object):
    def __init__(self, yaml_file):
        self.yaml_file = '/' + yaml_file

    # 读取yaml文件
    def read_yaml(self):
        path = os.getcwd()
        with open(path + self.yaml_file, 'r', encoding='utf8') as f:
            # 避免报警告需要加上Loader=yaml.FullLoader
            data = yaml.load(f, yaml.FullLoader)
            return data

    # 写入yaml文件
    def write_yaml(self, data):
        path = os.getcwd()
        with open(path + self.yaml_file, 'a', encoding='utf8') as f:
            # allow_unicode="utf8"：允许编码为utf8,避免写入unicode文字
            yaml.dump(data, f, allow_unicode="utf8")

    # 清空文件数据
    def clear_yaml(self):
        path = os.getcwd()
        with open(path + self.yaml_file, 'w', encoding='utf8') as f:
            f.truncate()


if __name__ == "__main__":
    os.chdir('..')
    data = YamlUtil("extract.yml").read_yaml()
    print(data)
    # YamlUtil("extract.yml").write_yaml()
