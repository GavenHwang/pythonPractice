# -*- coding:utf-8 -*-
import re

# re.match函数
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match() 就返回 none。
# 函数语法：
# re.match(pattern, string, flags=0)
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

# 正则表达式修饰符 - 可选标志
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解，忽略空格和 # 后面的注释

# re.group
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group()  : ", matchObj.group())
    print("matchObj.group(0) : ", matchObj.group(0))
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

# re.search方法
# re.search 扫描整个字符串并返回第一个成功的匹配。
# 函数语法
# re.search(pattern, string, flags=0)
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print("searchObj.group()  : ", searchObj.group())
    print("searchObj.group(0) : ", searchObj.group(0))
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")

# 检索和替换
# re.sub(pattern, repl, string, count=0, flags=0)
# pattern : 正则中的模式字符串。
# repl    : 替换的字符串，也可为一个函数。
# string  : 要被查找替换的原始字符串。
# count   : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是: ", num)


# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('number'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<number>\d+)', double, s))

# ?P<> 分组匹配
s = '4103271993XXXXXXXX'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)
print(res.groupdict())

# re.compile 函数
# compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
# 语法格式为：
# re.compile(pattern[, flags])
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print(m)
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print(m)
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print(m)
print(m.group(0))   # 可省略 0, group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
print(m.start(0))   # 可省略 0, start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
print(m.end(0))     # 可省略 0, end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
print(m.span(0))    # 可省略 0, span([group]) 方法返回 (start(group), end(group))。

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
print(m)
print(m.group(0))                            # 返回匹配成功的整个子串
print(m.span(0))                             # 返回匹配成功的整个子串的索引
print(m.group(1))                            # 返回第一个分组匹配成功的子串
print(m.span(1))                             # 返回第一个分组匹配成功的子串的索引
print(m.group(2))                            # 返回第二个分组匹配成功的子串
print(m.span(2))                             # 返回第二个分组匹配成功的子串
print(m.groups())                            # 等价于 (m.group(1), m.group(2), ...)
# print(m.group(3))                            # 不存在第三个分组

# findall
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
# 注意： match 和 search 是匹配一次 findall 匹配所有。
# 语法格式为：
# findall(string[, pos[, endpos]])
# 参数：
# string : 待匹配的字符串。
# pos : 可选参数，指定字符串的起始位置，默认为 0。
# endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)

# re.split
# split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
#
# re.split(pattern, string[, maxsplit=0, flags=0])
# 参数：
#
# 参数	描述
# pattern	匹配的正则表达式
# string	要匹配的字符串。
# maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
# flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
print(re.split('aa*', 'hello world'))    # 对于一个找不到匹配的字符串而言，split 不会对其作出分割

# 正则表达式模式
# 模式字符串使用特殊的语法来表示一个正则表达式：
# 字母和数字表示他们自身。一个正则表达式模式中的字母和数字匹配同样的字符串。
# 多数字母和数字前加一个反斜杠时会拥有不同的含义。
# 标点符号只有被转义时才匹配自身，否则它们表示特殊的含义。
# 反斜杠本身需要使用反斜杠转义。
# 由于正则表达式通常都包含反斜杠，所以你最好使用原始字符串来表示它们。模式元素(如 r'\t'，等价于 '\\t')匹配相应的特殊字符。
# 下表列出了正则表达式模式语法中的特殊元素。如果你使用模式的同时提供了可选的标志参数，某些模式元素的含义会改变。
#
# 模式	        描述
# ^	            匹配字符串的开头
# $	            匹配字符串的末尾。
# .	            匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]	        用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]	    不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# re*	        匹配0个或多个的表达式。
# re+	        匹配1个或多个的表达式。
# re?	        匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# re{ n}	    精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
# re{ n,}	    匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
# re{ n, m}	    匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a| b	        匹配a或b
# (re)	        对正则表达式分组并记住匹配的文本
# (?imx)	    正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
# (?-imx)	    正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
# (?: re)	    类似 (...), 但是不表示一个组
# (?imx: re)	在括号中使用i, m, 或 x 可选标志
# (?-imx: re)	在括号中不使用i, m, 或 x 可选标志
# (?#...)	    注释.
# (?= re)	    前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
# (?! re)	    前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
# (?> re)	    匹配的独立模式，省去回溯。
# \w	        匹配字母数字及下划线
# \W	        匹配非字母数字及下划线
# \s	        匹配任意空白字符，等价于 [ \t\n\r\f]。
# \S	        匹配任意非空字符
# \d	        匹配任意数字，等价于 [0-9].
# \D	        匹配任意非数字
# \A	        匹配字符串开始
# \Z	        匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
# \z	        匹配字符串结束
# \G	        匹配最后匹配完成的位置。
# \b	        匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B	        匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
# \n, \t, 等.	匹配一个换行符。匹配一个制表符。等
# \1...\9	    匹配第n个分组的内容。
# \10	        匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。

# 正则表达式实例
# 字符匹配
# 实例	        描述
# python	    匹配 "python".

# 字符类
# 实例	        描述
# [Pp]ython	    匹配 "Python" 或 "python"
# rub[ye]	    匹配 "ruby" 或 "rube"
# [aeiou]	    匹配中括号内的任意一个字母
# [0-9]	        匹配任何数字。类似于 [0123456789]
# [a-z]	        匹配任何小写字母
# [A-Z]	        匹配任何大写字母
# [a-zA-Z0-9]	匹配任何字母及数字
# [^aeiou]	    除了aeiou字母以外的所有字符
# [^0-9]	    匹配除了数字外的字符

# 特殊字符类
# 实例	        描述
# .	            匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
# \d	        匹配一个数字字符。等价于 [0-9]。
# \D	        匹配一个非数字字符。等价于 [^0-9]。
# \s	        匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	        匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w	        匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W	        匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。
