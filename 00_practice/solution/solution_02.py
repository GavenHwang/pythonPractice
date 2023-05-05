# -*- coding:utf-8 -*-


# 去除数组中的重复元素
import time


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    elif len(nums) == 1:
        return 1
    else:
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
    return nums[:j + 1]


print("去除数组中的重复元素", removeDuplicates([1, 1, 2, 2, 3, 3, 3]))


# 股票收益最大
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    new_price = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    return sum([x if x > 0 else 0 for x in new_price])


print("股票收益最大", maxProfit([7, 1, 5, 3, 6, 4]))


# 二维数组中是否存在目标元素
def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # 高
    m = len(matrix) - 1
    # 宽
    n = 0
    while True:
        if m < 0 or n > len(matrix[0]) - 1:
            return False
        if target == matrix[m][n]:
            return True
        elif target > matrix[m][n]:
            n += 1
        elif target < matrix[m][n]:
            m -= 1


print("二维数组中是否存在目标元素", searchMatrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))


# 数组合并，并从小到大排列
def merge(nums1, nums2):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    m = len(nums1) - len(nums2)
    n = len(nums2)
    o = len(nums1)
    while n > 0:
        if m > 0 and nums1[m - 1] > nums2[n - 1]:
            nums1[o - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[o - 1] = nums2[n - 1]
            n -= 1
        o -= 1
    return nums1


print("数组合并，并从小到大排列", merge([1, 2, 5, 0, 0, 0], [0, 3, 6]))


# 判断是否为水仙花数
def is_sxhs(num):
    if num < 100 or num > 999:
        return False
    a = num % 10
    b = (num % 100 - a) / 10
    c = (num - b * 10 - a) / 100
    if num == a ** 3 + b ** 3 + c ** 3:
        return True
    else:
        return False


print("判断是否为水仙花数", is_sxhs(371))


# 判断是否为回文
def is_huiwen(ss):
    middle = len(ss) // 2
    for i in range(middle):
        if ss[i] != ss[len(ss) - i - 1]:
            return False
    return True


print("判断是否为回文", is_huiwen("abaaba"))


# 判断是否为回文
def is_huiwen2(sss):
    if sss == sss[::-1]:
        return True
    return False


print("判断是否为回文2", is_huiwen2("abcba"))


# 【字符串分割】给定非空字符s，将该字符串分割成一些子串，使每个子串均为回文
def partition(s: str):
    if not s:
        return []
    auxiliary = []
    result = []

    def backtrack(s, auxiliary, result):
        if not s:
            result.append(auxiliary[:])
            return
        for index in range(1, len(s) + 1):
            if is_huiwen2(s[:index]):
                auxiliary.append(s[:index])
                backtrack(s[index:], auxiliary, result)
                auxiliary.pop()

    backtrack(s, auxiliary, result)
    return result


print("字符串分割成均为回文的子串", partition("abcbad"))


# 【字符串分割】给定非空字符s，将该字符串分割成一些子串，使每个子串的ASCIIA码值的和均为水仙花数。


# 最长回文串
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    def is_huiwen(ss):
        if ss == ss[::-1]:
            return True
        else:
            return False

    max_s = s[0]
    max_len = 1
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(s[i:j]) > max_len and is_huiwen(s[i:j]):
                max_s = s[i:j]
                max_len = len(s[i:j])
    return max_s, max_len


print("最长回文串", longestPalindrome(
    "vyzonecajxxdvswhftixmzgjbfoeilbnchqmdgoxfmkkkkcqguavfozmplhzgothrwpukzgkctdacbxefrzrmbgwwrrhpcvqwvgwgknyrtxxoligsqpbqoucltakbkywwssyodzydsjxeuvgiqqitkfkqnxsfflgbjvbxdrworsdkowtkgabnszgsmgytupybdclmmsmougfendwvzarfdfbixjnlxvevqfoohcgrrysofifdfulygrmkwpimduzzluojeqixdtcxhcqnfsdbunmhsglhiplgbhrqrrrprffjfradvbifxxhoqylkejyprxdtianietnjumltxywfowopghurofvwtxvaxtqnjbzwvljjwfmmlhixogwwyaoysvrpgfymyqjschhqcwvytkreirdxfapaomayebhkzxgmlthoxialmtnilfopvhhqlocytyrtpfmpgqakdbrsteurcpfvruicuxzukfpwjwgnuaaungwjwpfkuzxuciurvfpcruetsrbdkaqgpmfptrytycolqhhvpoflintmlaixohtlmgxzkhbeyamoapafxdrierktyvwcqhhcsjqymyfgprvsyoaywwgoxihlmmfwjjlvwzbjnqtxavxtwvforuhgpowofwyxtlmujnteinaitdxrpyjeklyqohxxfibvdarfjffrprrrqrhbglpihlgshmnubdsfnqchxctdxiqejoulzzudmipwkmrgylufdfifosyrrgchoofqvevxlnjxibfdfrazvwdnefguomsmmlcdbyputygmsgzsnbagktwokdsrowrdxbvjbglffsxnqkfktiqqigvuexjsdyzdoysswwykbkatlcuoqbpqsgiloxxtrynkgwgvwqvcphrrwwgbmrzrfexbcadtckgzkupwrhtogzhlpmzofvaugqckkkkmfxogdmqhcnblieofbjgzmxitfhwsvdxxjacenozyv"))


def longestPalindrome2(s):
    """
    :type s: str
    :rtype: str
    """

    def get_huiwei(left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return s[left + 1: right]

    max_s = s[0]
    for i in range(len(s)):
        s1 = get_huiwei(i, i)
        s2 = get_huiwei(i, i + 1)
        if max(len(s1), len(s2)) > len(max_s):
            max_s = s1 if len(s1) > len(s2) else s2
    return max_s, len(max_s)


print(
    "最长回文串",
    longestPalindrome2(
        "vyzonecajxxdvswhftixmzgjbfoeilbnchqmdgoxfmkkkkcqguavfozmplhzgothrwpukzgkctdacbxefrzrmbgwwrrhpcvqwvgwgknyrtxxoligsqpbqoucltakbkywwssyodzydsjxeuvgiqqitkfkqnxsfflgbjvbxdrworsdkowtkgabnszgsmgytupybdclmmsmougfendwvzarfdfbixjnlxvevqfoohcgrrysofifdfulygrmkwpimduzzluojeqixdtcxhcqnfsdbunmhsglhiplgbhrqrrrprffjfradvbifxxhoqylkejyprxdtianietnjumltxywfowopghurofvwtxvaxtqnjbzwvljjwfmmlhixogwwyaoysvrpgfymyqjschhqcwvytkreirdxfapaomayebhkzxgmlthoxialmtnilfopvhhqlocytyrtpfmpgqakdbrsteurcpfvruicuxzukfpwjwgnuaaungwjwpfkuzxuciurvfpcruetsrbdkaqgpmfptrytycolqhhvpoflintmlaixohtlmgxzkhbeyamoapafxdrierktyvwcqhhcsjqymyfgprvsyoaywwgoxihlmmfwjjlvwzbjnqtxavxtwvforuhgpowofwyxtlmujnteinaitdxrpyjeklyqohxxfibvdarfjffrprrrqrhbglpihlgshmnubdsfnqchxctdxiqejoulzzudmipwkmrgylufdfifosyrrgchoofqvevxlnjxibfdfrazvwdnefguomsmmlcdbyputygmsgzsnbagktwokdsrowrdxbvjbglffsxnqkfktiqqigvuexjsdyzdoysswwykbkatlcuoqbpqsgiloxxtrynkgwgvwqvcphrrwwgbmrzrfexbcadtckgzkupwrhtogzhlpmzofvaugqckkkkmfxogdmqhcnblieofbjgzmxitfhwsvdxxjacenozyv")
)
