# -*- coding:utf-8 -*-
import string


# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

def is_valid(s):
    n = len(s) // 2
    while n > 0:
        s = s.replace("[]", "").replace("()", "").replace("{}", "")
        n -= 1

    if not s:
        print(True)
    else:
        print(False)


s = '([])'.replace(" ", "")
arr = ["([)]", "", "{([])}"]
for i in arr:
    is_valid(i)


# 题目描述
# 定义：当一个字符串只有元音字母（aeiouAEIOU）组成，称为元音字符串。
# 现给定一个字符串，请找出其中最长的元音字符子串，并返回其长度；如果找不到，则返回0。
#
# 子串：字符串中任意个连续的字符组成的子序列称为该字符串的子串。
#
# 解答要求
# 时间限制：1000ms, 内存限制：256MB
# 输入
# 一个字符串，其长度范围： 0 < length <= 65535。
#
# 字符串仅由字符a-z和A-Z组成。
#
# 输出
# 一个整数，表示最长的元音字符子串的长度。
#
# 样例
# 输入样例 1 复制
#
# asdbuiodevauufgh
# 输出样例 1
#
# 3
# 提示样例 1
# 最长元音子串为 “uio” 或 “auu”，其长度都为3，因此输出3

def get_max_aeiou(s):
    max_length = 0
    i = 0
    while i <= len(s) - 1:
        if s[i] in "aeiouAEIOU":
            for j in range(i + 1, len(s)):
                if s[j] in "aeiouAEIOU":
                    pass
                else:
                    if j - i > max_length:
                        max_length = j - i
                        i
                    break
    return max_length


print(get_max_aeiou("asdbuiodevauufgh"))
