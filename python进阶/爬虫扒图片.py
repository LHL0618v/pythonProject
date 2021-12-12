import requests
import re

method = 'get'
url = 'https://www.dgtle.com/article-1659915-1.html'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
rep = requests.request(method, url, headers=header)
res = rep.text
imgs = re.findall(r'data-original="(.*?)"', res)
print("下载%d张图片" % len(imgs))
for i, j in enumerate(imgs):
    print(f"正在下载{i + 1}张图片")
    with open(f"./imgs/{i + 1}.jpeg", "wb") as f:
        rep_jpg = requests.request(method, j, headers=header)
        f.write(rep_jpg.content)
else:
    print("下载完成")
