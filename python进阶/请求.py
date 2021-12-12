import requests
import re

method = 'get'
url = 'https://movie.douban.com/chart'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
data = {}

rep = requests.request(method, url, headers=header)
print(rep)
res = rep.text
print(res)
# res = rep.content
# print("返回字节格式的页面源码",res)
# res = rep.json()
# print(res)
movice = re.findall(r'subject/\d+/"  title="(.*?)">.*?<span class="rating_nums">(.*?)</span>', res, re.S)
print(movice)
# 根据列表中的第二维数据进行排序
movice.sort(key=lambda x: x[1], reverse=True)
print(movice)