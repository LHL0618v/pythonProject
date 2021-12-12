import re

s = "gdgj\n235kfsdyha23456hsg\nd21g1215\tsfG sfsg&%630"
# 使用至少1个数字分隔，并转回列表
new_s = re.split(r'\d+', s)
print(new_s)
# 将单个数字字符替换成*
new_s = re.sub(r'\d', "*", s)
print(new_s)

#  findall(匹配内容,字符串) 返回的是一个符合匹配内容的列表
# 找出字符串中g开头，长度为2的子字符串
new_s = re.findall('g.', s)
print(new_s)
# 找出字符串中g开头，长度为2的子字符串 包括\n等
new_s = re.findall('g.', s, re.S)
print(new_s)
# 找出字符串中g开头，长度为2的子字符串 包括\n等并忽略大小写
new_s = re.findall('g.', s, re.S | re.I)
print(new_s)

# 找出字符串中g开头，匹配1个单词字符
new_s = re.findall(r'g\w', s, re.S | re.I)
print(new_s)

# 找出字符串中g开头，匹配1个非单词字符
new_s = re.findall(r'g\W', s, re.S | re.I)
print(new_s)

# 找出字符串中g开头，匹配1个非数字字符
new_s = re.findall(r'g\D', s, re.S | re.I)
print(new_s)

# 找出字符串中g开头，匹配1个空白字符
new_s = re.findall(r'g\s', s, re.S | re.I)
print(new_s)
# 找出字符串中g开头，匹配1个非空白字符
new_s = re.findall(r'g\S', s, re.S | re.I)
print(new_s)

# 找出字符串中g开头,除\n以外的长度为2的字符串
new_s = re.findall(r'g.', s)
print(new_s)

# 找出字符串中g开头,除\n以外的长度为2的字符串
new_s = re.findall(r'^g.', s)
print(new_s)

# 找出字符串中，以数字结尾的的字符串
new_s = re.findall(r'.\d$', s)
print(new_s)

s = "a12a123a4567a9fasd"
# 匹配前一个字符任意次
new_s = re.findall(r'a\d*', s)
print(new_s)
# 匹配前一个字符至少1次
new_s = re.findall(r'a\d+', s)
print(new_s)
# 匹配前一个字符0次或或者1次
new_s = re.findall(r'a\d?', s)
print(new_s)
# 匹配前一个字符n次
new_s = re.findall(r'a\d{3}', s)
print(new_s)
# 匹配前一个字符至少n次
new_s = re.findall(r'a\d{3,}', s)
print(new_s)
# 匹配前一个字符至少n次,至多m次
new_s = re.findall(r'a\d{2,4}', s)
print(new_s)
# 匹配前一个字符至多多m次
new_s = re.findall(r'a\d{,2}', s)
print(new_s)
