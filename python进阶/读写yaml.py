import yaml


class ReadConfig(object):
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_yaml(self):
        with open(self.yaml_file, 'r', encoding='utf8') as f:
            # 避免报警告需要加上Loader=yaml.FullLoader
            data = yaml.load(f, yaml.FullLoader)
            print(data)

    # 写入yaml文件
    def write_yaml(self):
        with open(self.yaml_file, 'w', encoding='utf8') as f:
            data = [{'msxy': [{'name': '百里'}, {'age': 18}]}]
            # allow_unicode="utf8"：允许编码为utf8,避免写入unicode文字
            yaml.dump(data, f, allow_unicode="utf8")
            print(data)


if __name__ == "__main__":
    # ReadConfig("config.yaml").read_yaml()
    ReadConfig("config.yaml").write_yaml()
    # ReadConfig("H:\pythonProject\接口测试\extract.yml").read_yaml()
    ReadConfig("H:\pythonProject\接口测试\yaml驱动\config.yaml").read_yaml()
