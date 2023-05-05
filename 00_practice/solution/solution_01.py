# -*- coding:utf-8 -*-

"""
1、标题:两数之和绝对值最小  
【两数之和绝对值最小】给定一个从小到大的有序整数序列(存在正整数和负整数)数组 nums，请你在该数组中找出两个数，其和的绝对值(|nums[x]+nums[y]|)为  
最小值，并返回 这个绝对值。每种输入只会对一个答案。但是，数组中同一个元素不能使用两遍。  
输入描述: 一个通过空格分割的有序整数序列字符串，最多 1000个整数，且整数数值范围是-65535~65535。  
输出描述: 两数之和绝对值最小值。  
示例:  
输入   
-3 -1 5 7 11 15  
输出  
2  
"""
import re


def min_abs(s):
    arr = [int(x) for x in str(s).split(" ")]
    a = arr[0]
    b = arr[1]
    min = abs(a + b)
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] + arr[j]) < min:
                a = arr[i]
                b = arr[j]
                min = abs(a + b)
    return a, b, min


# print(min_abs("-1 -3 7 5 11 15"))

"""
2、标题:字符串分割  
【字符串分割】给定非空字符在s，将该字符串分割成一些子串，使每个子串的ASCIIA码值的和均为水仙花数。  
1、若分割不成功则返回 0   
2、若分割成功且分割结果不唯一则返回-1   
3、若分割成功且分割结果唯一，则返回分割后的子串数目  
输入描述: 1、输入字符串的最大长度为 200  
输出描述:根据题目描述中情况返回相应的结果   
备注:“水仙花数”是指一个三位数，每位上数字的立方和等于该数字本身，如 371是“水仙花数”，因为:371=3^3+7^3+1^3。  
示例：  
输入  
abc  
输出  
0  
"""


def partition_sxhs(s):
    ord_arr = [ord(x) for x in s]

    def is_sxhs(n):
        """判断是否为水仙花数"""
        if n < 100 or n > 999:
            return False
        a = n % 10
        b = (n - a) // 10 % 10
        c = (n - a - b * 10) // 100 % 10
        if n == a ** 3 + b ** 3 + c ** 3:
            return True
        return False

    def backtrack(origin_list, tmp_list, result):
        """回溯算法"""
        if not origin_list:
            result.append(tmp_list[:])
            return
        for i in range(1, len(origin_list) + 1):
            this_list = origin_list[:i]
            # 先截取出来一个水仙花数，再递归数组剩余部分
            if is_sxhs(sum(this_list)):
                tmp_list.append(this_list)
                backtrack(origin_list[i:], tmp_list, result)
                tmp_list.pop()

    tmp_list, result = [], []
    backtrack(ord_arr, tmp_list, result)
    print(result)
    if len(result) == 0:
        return 0
    elif len(result) > 1:
        return -1
    elif len(result) == 1:
        return len(result[0])


# print(partition_sxhs("Gddd$Gddd"))

"""
3、标题:区间交集  
【区间交集】给定一组闭区间，其中部分区间存在交集。任意两个给定区间的交集，称为公共区间(如:[1,2],[2,3]的公共区间为[2,2]，[3,5],[3,6]的公共区间为  
[3,5])。公共区间之间 若存在交集，则需要合并(如:[1,3],[3,5]区间存在交集[3,3]，需合并为[1,5])。按升序排列 输出合并后的区间列表。  
输入描述: 一组区间列表，区间数为 N: 0<=N<=1000;区间元素为 X: -10000<=X<=10000。   
输出描述: 升序排列的合并区间列表   
备注:  
    1、区间元素均为数字，不考虑字母、符号等异常输入。  
    2、单个区间认定为无公共区间。   
示例:  
输入  
[[0, 3], [1, 3], [3, 5], [3, 6]]  
输出   
[[1, 5]]  
"""


def common_section_merge(arr):
    if len(arr) == 1:
        return arr[0]
    arr.sort(key=lambda x: x[0])  # 区间列表按区间开头从小到大排序
    comm_section = []  # 公共区间列表
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i][-1] >= arr[j][0]:  # 存在交集
                comm_section.append([arr[j][0], min(arr[i][-1], arr[j][-1])])
    if len(comm_section) == 1:
        return comm_section
    comm_section.sort(key=lambda x: x[0])
    l = len(comm_section)
    i = 0
    while i <= l - 2:
        if comm_section[i][-1] >= comm_section[i + 1][0]:
            comm_section[i][-1] = max(comm_section[i][-1], comm_section[i + 1][-1])
            comm_section.pop(i + 1)
            l -= 1
        else:
            i += 1
    return comm_section


# print(common_section_merge([[0, 3], [1, 3], [3, 5], [3, 6]]))

"""
4、标题:判断一组不等式是否满足约束并输出最大差   
【判断一组不等式是否满足约束并输出最大差】给定一组不等式，判断是否成立并输出不等式的最大差(输出浮点数的整数部分)，  
要求:   
1)不等式系数为 double类型，是一个二维数组   
2)不等式的变量为 int类型，是一维数组;   
3)不等式的目标值为 double类型，是一维数组  
4)不等式约束为字符串数组，只能是:">",">=","<","="，  
例如，不等式组:   
a11*x1+a12*x2+a13*x3+a14*x4+a15*x5<=b1; a21*x1+a22*x2+a23*x3+a24*x4+a25*x5<=b2; a31*x1+a32*x2+a33*x3+a34*x4+a35*x5<=b3;  
最大差
=max{(a11*x1+a12*x2+a13*x3+a14*x4+a15*x5-b1),(a21*x1+a22*x2+a23*x3+a24*x4+ a25*x5-b2),(a31*x1+a32*x2+a33*x3+a34*x4+a35*x5-b3)}，  
类型为整数(输出浮点数的整数部分)   
输入描述:  
1)不等式组系数(double类型):  
a11,a12,a13,a14,a15  
a21,a22,a23,a24,a25  
a31,a32,a33,a34,a35  
2)不等式变量(int类型):  
x1,x2,x3,x4,x5 3)不等式目标值(double类型):b1,b2,b3 4)不等式约束(字符串类型):<=,<=,<=  
输入:  
a11,a12,a13,a14,a15,a21,a22,a23,a24,a25, a31,a32,a33,a34,a35,x1,x2,x3,x4,x5,b1,b2,b3,<=,<=,<=   
输出描述:true或者 false，最大差  
示例:  
输入   
2.3,3,5.6,7,6;11,3,8.6,25,1;0.3,9,5.3,66,7.8;1,3,2,7,5;340,670,80.6;<=,<=,<=   
输出  
false,458  
"""


def max_difference(str):
    l = str.split(";")
    a1 = [x.split(',') for x in l[-3:]]
    a2 = l[:-3]
    b = []
    for i in range(len(a2)):
        c = a2[i].split(',')
        s = 0
        for j in range(len(c)):
            s += float(c[j]) * float(a1[0][j])
        b.append([s, a1[-1][i], float(a1[-2][i])])
    return all([eval('%s %s %s' % (x[0], x[1], x[2])) for x in b]), int(max([x[0] - x[-1] for x in b]))


# print(max_difference("2.3,3,5.6,7,6;11,3,8.6,25,1;0.3,9,5.3,66,7.8;1,3,2,7,5;340,670,80.6;<=,<=,<="))

"""
5、标题:5键键盘的输出  
【5键键盘的输出】有一个特殊的 5键键盘，上面有 a,ctrl-c,ctrl-x,ctrl-v,ctrl-a五个键。   
a键在屏幕上输出一个字母 a;  
ctrl-c将当前选择的字母复制到剪贴板;  
ctrl-x将当前选择的 字母复制到剪贴板，并清空选择的字母;  
ctrl-v将当前剪贴板里的字母输出到屏幕;  
ctrl-a 选择当前屏幕上所有字母。  
注意:  
    1、剪贴板初始为空，新的内容被复制到剪贴板时会覆盖原来的内容  
    2、当屏幕上没有字母时，ctrl-a无效   
    3、当没有选择字母时，ctrl-c和 ctrl-x无效  
    4、当有字母被选择时，a和ctrl-v这两个有输出功能的键会先清空选择的字母，再进行输出  
给定一系列键盘输入，输出最终屏幕上字母的数量。  
输入描述:  
输入为一行，为简化解析，用数字 12345代表 a,ctrl-c,ctrl-x,ctrl-v,ctrl-a五个键的输入，数字用空格分隔  
输出描述:  
输出一个数字，为最终屏目上字母的数量。  
示例:   
输入   
111   
输出  
3  
"""


def screen_end(s):
    screen = ''
    clip = ''
    selected = False
    for i in s:
        if i == '1' and not selected:  # a
            screen += 'a'
        elif i == '1' and selected:  # a
            screen = 'a'
            selected = False
        elif i == '2' and selected and screen:  # ctrl-c
            clip = screen
        elif i == '3' and selected and screen:  # ctrl-x
            clip = screen
            screen = ''
            selected = False
        elif i == '4' and selected:  # ctrl-v
            screen = clip
            selected = False
        elif i == '4' and not selected:  # ctrl-v
            screen += clip
        elif i == '5' and screen:  # ctrl-a
            selected = True
    return len(screen)


# print(screen_end("11515244"))

"""
6、标题:找到它  
【找到它】找到它是一个小游戏，你需要在一个矩阵中找到给定的单词。假设给定单词 HELLOWORD， 在矩阵中只要能找到 H->E->L->L->O->W->O->R->L->D连成  
的单词，就算通过。注意区分英文字母大小写，并且您只能上下左右行走，不能走回头路  
输入描述:  
输入第1行包含两个整数 n、m(0<n,m<21)分别表示 n行m列的矩阵，  
第2行是长度不超过100的单词W(在整个矩阵中给定单词 W 只会出现一次)，  
从第3行到第n+2行是指包 含大小写英文字母的长度为 m的字符串矩阵。  
输出描述:   
如果能在矩阵中连成给定的单词，则输出给定单词首字母在矩阵中的位置(第几行 第几列)，否则输出“NO”。   
示例:  
输入  
5 5  
HELLOWORLD  
CPUCY   
EKLQH   
CHELL   
LROWO   
DGRBC   
输出   
3 2  
"""


def find_it():
    # 给数据一个固定的默认值方便调试
    n, m = 5, 5
    s = "HELLOWORLD"
    arr = ["CPUCY", "EKLQH", "CHELL", "LROWO", "DGRBC"]

    # n, m = tuple([int(x) for x in input().strip().split(" ")])
    # s = input().strip()
    # arr = []
    # for i in range(n):
    #     arr.append(input().strip())

    def loc_surroundings(loc):
        """按上、右、下、左顺序输出坐标周围的合法坐标"""
        loc_up = (loc[0] - 1, loc[1])
        loc_right = (loc[0], loc[1] + 1)
        loc_below = (loc[0] + 1, loc[1])
        loc_left = (loc[0], loc[1] - 1)
        surroundings = []
        for location in [loc_up, loc_right, loc_below, loc_left]:
            if 0 <= location[0] <= n - 1 and 0 <= location[1] <= m - 1:
                surroundings.append(location)
        return surroundings

    def search_path(start_loc, s_index, tmp_result, result):
        """回溯"""
        if s_index > len(s) - 2:
            result.append(tmp_result[:])
            return
        for surround_loc in loc_surroundings(start_loc):
            # 不能走回头路
            if surround_loc != start_loc and surround_loc not in tmp_result and \
                    arr[surround_loc[0]][surround_loc[1]] == s[s_index + 1]:
                tmp_result.append(surround_loc)
                search_path(surround_loc, s_index + 1, tmp_result, result)
                tmp_result.pop()

    tmp_result, result = [], []
    # 找到起点符合的坐标，开始回溯
    for i in range(m):
        for j in range(n):
            if arr[i][j] == s[0]:
                tmp_result.append((i, j))
                search_path((i, j), 0, tmp_result, result)
                if result:
                    return i + 1, j + 1


# print(find_it())

"""
7、标题:报数问题  
【报数问题】有n个人围成一圈，顺序排号为1-n，从第1个人开始报数(从1到3报数)，凡报到3的人退出圈子，问最后留下的是原来第几号的那位。   
输入描述:  
输入人数n(n<1000)  
输出描述:  
输出最后留下来的是原来第几号  
示 例:   
输入  
2  
输出  
2  
"""


def baoshu(n):
    arr = [x for x in range(1, n + 1)]
    i = 1
    j = 0
    while len(arr) > 1:
        if i == 3:
            arr.pop(j)
            i = 1
        else:
            i += 1
            j += 1
        if j > len(arr) - 1:
            j = 0
    return arr[0]


# print(baoshu(5))


"""
8、标题:最长的顺子   
【最长的顺子】斗地主起源于湖北十堰房县，据说是一位叫吴修全的年轻人根据当地流行的扑克玩法“跑得快”改编的，如今已风靡整个中国，并流行于互联网上。   
牌型:单顺，又称顺子，最少5张牌，最多12张牌(3...A)不能有2，也不能有大小王，不计花色。  
例如 3-4-5-6-7-8，7-8-9-10-J-Q，3-4-5-6-7-8-9-10-J-Q-K-A  
可用的牌 3<4<5<6<7<8<9<10<J<Q<K<A<2<B(小王)<C(大王)，每种牌除大小王外有四种花色(共有13*4+2张牌)  
输入：1、手上有的牌 2、已经出过的牌(包括对手出的和自己出的牌)  
输出：对手可能构成的最长的顺子(如果有相同长度的顺子，输出牌面最大的那个那一个)，如果无法构成顺子，则输出 NO-CHAIN  
输入描述:  
输入的第一行为当前手中的牌  
输入的第二行为已经出过的牌  
输出描述:  
最长的顺子  
示例:  
输入   
3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A   
4-5-6-7-8-8-8  
输出  
9-10-J-Q-K-A  
"""


def the_longest_chain(my_poker, history_poker):
    # 定义一个扑克转数字字典和一个数字转扑克字典
    s1 = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    s2 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    poker = {}
    poker_reverse = {}
    for i in range(len(s1)):
        poker[s1[i]] = s2[i]
        poker_reverse[s2[i]] = s1[i]
    # 计算未出的扑克，去重并排序
    my_poker = [poker.get(x) for x in str(my_poker).split('-')]
    history_poker = [poker.get(x) for x in str(history_poker).split('-')]
    all_poker = [x for x in range(3, 15)] * 4
    for i in my_poker + history_poker:
        if all_poker.index(i):
            all_poker.remove(i)
    remain_poker = list(set(all_poker))
    remain_poker.sort()
    # 找出最长递增子串
    tmp_result = []
    result = []
    for i in range(len(remain_poker) - 1):
        tmp_result.append(remain_poker[i])
        for j in range(i + 1, len(remain_poker)):
            if remain_poker[j] - remain_poker[j - 1] == 1:
                tmp_result.append(remain_poker[j])
            else:
                break
        if len(tmp_result) > len(result):
            result = tmp_result[:]
        tmp_result.clear()
    return '-'.join([poker_reverse[x] for x in result])


# print(the_longest_chain("3-3-3-3-4-4-5-5-6-7-8-9-10-J-Q-K-A", "4-5-6-7-8-8-8"))


"""
9、标题:最长元音子串的长度   
【最长元音子串的长度】定义:当一个字符串只有元音字母(aeiouAEIOU)组成，称为元音字符串。现给定一个字 符串，请找出其中最长的元音字符串，并返回其长度;  
如果找不到，则返回 0。子串:字符串中任意一个连续的字符组成的子序列称为该字符串的子串。   
输入描述:  
一个字符串，其长度范围:0<length<65535。  
字符串仅由字母a-z和A-Z组成。  
输出描述:  
一个整数，表示最长的元音字符串的长度。  
示例:  
输入   
asdbuiodevauufgh   
输出  
3  
"""


def max_aeiou(s):
    result = ''
    for i in range(len(s) - 1):
        if s[i] not in 'aeiouAEIOU':
            continue
        for j in range(i + 1, len(s)):
            if s[j] in 'aeiouAEIOU':
                if len(s[i:j + 1]) > len(result):
                    result = s[i:j + 1]
            else:
                break
    return result


# print(max_aeiou("asdbuiodevauufgh"))


"""
10、标题:贪吃蛇  
【贪吃蛇】贪吃蛇是一个经典游戏，蛇的身体由若干方格连接而成，身体随蛇头移动。蛇头触碰到食物时，蛇的长度会增加一格。蛇头和身体的任一方格或者游戏版图边  
界碰撞时，游戏结束。  
下面让我们来完成贪吃蛇游戏的模拟。给定一个N*M的数组ar，代表N*M个方格组成的版图，贪吃蛇每次移动一个方格。
若ar[i][j]=='H'，表示该方可为贪吃蛇的起始位置;  
若ar[i][j]=='F'，表示该方格为食物;  
若ar[i][j]=='E'，表示该方格为空格。  
贪吃蛇初始长度为1，初始移动方向为向左。输入为给定一系列贪吃蛇的移动操作，返回操作后蛇的长度，如果在操作执行完之前已经游戏结束，返回游戏结束时贪吃蛇的  
长度。  
输入描述:  
输入第1行为空格分隔的字母，代表贪吃蛇的移动操作。字母取值为U、D、L、R、G，分别表示贪吃蛇往上、下、左、右转向，转向时贪吃蛇不移动，G表示贪吃蛇按当前  
的方向移动一格。用例保证输入的操作正确。  
第2行为空格分隔的两个数，指定为N和M，为数组的行和列数。余下N行每行是空格分隔的M个字母。字母取值为H、F和E，H表示贪吃蛇的起始位置，F表示食物，E表示该  
方格为空。用例保证有且只有一个H，而F和E会有多个。  
输出描述:  
输出一个数字为蛇的长度。   
示例:  
输入  
D G G  
3 3  
F F F   
F F H   
E F E   
输出  
1  
"""


def snake():
    a1 = ['D', 'G', 'L', 'G', 'G', 'U', 'G', 'G', 'R', 'G', 'G', 'D', 'G', 'L', 'G']
    n, m = 3, 3
    a2 = [['F', 'F', 'F'], ['F', 'F', 'H'], ['E', 'F', 'E']]
    # a1 = input().split(" ")
    # n, m = [int(x) for x in input().split(" ")]
    # a2 = []
    for i in range(n):
        a2.append(input().split(" "))
    # 找到起始位置
    start = (0, 0)
    for i in range(n):
        for j in range(m):
            if a2[i][j] == 'H':
                a2[i][j] = 'E'  # 头开始移动之后变为空格
                start = (i, j)
    body = [start]
    direction = 'L'
    for i in a1:
        if i == 'U':
            direction = 'U'
        elif i == 'D':
            direction = 'D'
        elif i == 'L':
            direction = 'L'
        elif i == 'R':
            direction = 'R'
        elif i == 'G':
            if direction == 'U':
                next = (body[0][0] - 1, body[0][1])
            elif direction == 'D':
                next = (body[0][0] + 1, body[0][1])
            elif direction == 'L':
                next = (body[0][0], body[0][1] - 1)
            else:
                next = (body[0][0], body[0][1] + 1)
            if next[0] < 0 or next[1] < 0 or next[0] > n - 1 or next[1] > m - 1 or next in body[:-1]:
                return len(body)
            if a2[next[0]][next[1]] == 'E':
                body = [next] + body[:-1]
            elif a2[next[0]][next[1]] == 'F':
                body = [next] + body[:]
                a2[next[0]][next[1]] = 'E'  # 吃完之后，变为空格
    return len(body)


# print(snake())

"""
11、标题:找车位  
【找车位】停车场有一横排车位，0代表没有停车，1代表有车。至少停了一辆车在车位上，也至少有一个空位没有停车。为了防刮蹭，需为停车人找到一个车位，使得距  
停车人的车最近的车辆的距离是最大的，返回此次的最大距离。  
输入描述:  
1、一个用半角逗号分割的停车标识字符串，停车标识为0或1，0为空位，1为已停车。  
2、停车位最多100个。输出描述:  
输出一个整数记录最大距离。  
示例1:  
输入  
1,0,0,0,0,1,0,0,1,0,1  
输出  
2  
"""


def parking(s):
    arr = [int(x) for x in s.split(",")]
    max_distance = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            left_max_distance = 0
            right_max_distance = 0
            j = i - 1
            while j >= 0:
                left_max_distance = i - j
                if arr[j] == 1:
                    break
                j -= 1
            k = i + 1
            while k <= len(arr) - 1:
                right_max_distance = k - i
                if arr[k] == 1:
                    break
                k += 1
            max_distance = max(max_distance, min(left_max_distance, right_max_distance))
    return max_distance


# print(parking("1,0,0,0,0,1,0,0,1,0,1"))

"""
12、标题:敏感字段加密  
【敏感字段加密敏】给定一个由多个命令字组成的命令字符串:  
1、字符串长度小于等于127字节，只包含大小写字母、数字、下划线和偶数个双引号;  
2、命令字之间以一个或多个下划线_进行分割;  
3、可以通过两个双引号来"标识包含下划线_的命令字或空命令字(仅包含两个引双引号的命令字)双引号不会在命令字内部出现;  
仅对指定索引的敏感字段进行加密，替换为*(6个*)，并删除命令字前后多余的下划线_。如果无法找到指定索引的命令字，输出字符串ERROR。  
输入描述:  
输入为两行，第一行为命令字索引K(从0开始)，第二行为命令字符串S。  
输出描述:  
输出处理后的命令字符串，如果无法找到指定索引的命令字，输出字符串ERROR  
示例:  
输入  
1
pasword_a12345678__timeout_100
输出  
pasword_*_timeout_100   
"""


def password_encrypt():
    index = int(input().strip())
    arr = input().strip().split("_")
    while "" in arr:
        arr.remove("")
    if index * 2 <= len(arr):
        arr[index * 2 - 1] = "*"
    else:
        return "ERROR"
    return '_'.join(arr)


# print(password_encrypt())


"""
13、标题:任务最优调度  
【任务最优调度】给定一个正整数组表示待系统执行的任务列表，数组的每一个元素代表一个任务，元素的值表示该任务的类型。请计算执行完所有任务所需的最短时间。  
任务执行规则如下:  
1、任务可以按任意顺序执行，且每个任务执行耗时间均为1个时间单位。  
2、两个同类型的任务之间必须有长度为N个单位的冷却时间，比如N为2时，在时间K执行了类型3的任务，那么K+1和K+2两个时间不能执行类型3任务。  
3、系统在任何一个单位时间内都可以执行一个任务，或者等待状态。说明:数组最大长度为1000，速度最大值1000。  
输入描述:  
第一行记录一个用半角逗号分隔的数组，数组长度不超过1000，数组元素的值不超过1000第二行记录任务冷却时间，N为正整数，N<=100。  
输出描述:  
输出为执行完所有任务所需的最短时间。  
示例1:  
输入  
2,2,2,3  
2  
输出  
7  
"""


def task_schedule():
    arr = input().strip().split(",")
    n = int(input().strip())
    d = {}  # 记录各个任务出现的次数
    d_max = 0  # 任务次数最大值3
    d_max_n = 0  # 任务次数最大值对应的任务个数1
    for i in arr:
        d[i] = d.get(i, 0) + 1
        if d[i] > d_max:
            d_max = d[i]
    for k, v in d.items():
        if d[k] == d_max:
            d_max_n += 1
    return max((d_max - 1) * (n + 1) + d_max_n, len(arr))


# print(task_schedule())

"""
14、标题:非严格递增连续数字序列  
【非严格递增连续数字序列】输入一个字符串仅包含大小写字母和数字，求字符串中包含的最长的非严格递增连续输数字序列的长度(比如12234属于非严格递增连续数字序列)。  
输入描述:  
输入一个字符串仅包含大小写字母和数字，输入的字符串最大不超过255个字符。  
输出描述:  
最长的非严格递增连续数字序列的长度。  
示例:  
输入  
abc2234019A334bc  
输出  
4  
"""


def max_increase_number(s):
    import re
    pattern = re.compile(r'\d+')
    arr = pattern.findall(s)
    max_n = 0
    for num in arr:
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                if num[j] < num[j - 1]:
                    break
                if j - i + 1 > max_n:
                    max_n = j - i + 1
    return max_n


# print(max_increase_number("abc223401A334bc"))


"""
15、标题:求解连续数列  
【求解连续数列】已知连续正整数数列{K}=K1,K2,K3...Ki的各个数相加之和为S，i=N(0<S<100000,0<N<100000),求此数列K。  
输入描述:  
输入包含两个参数，1)连续正整数数列和S，2)数列里数的个数N。  
输出描述:  
如果有解输出数列K，如果无解输出-1。  
示例1:  
输入  
525  
6  
输出  
85 86 87 88 89 90  
"""


def shulie(s, n):
    import math
    arr = [0] * n
    middle = int(s / n + 0.5) if n % 2 == 0 else int(s / n)
    start = middle - math.floor(n / 2)
    for i in range(len(arr)):
        arr[i] = start + i
    if arr[0] <= 0:
        return -1
    return arr


# print(shulie(525, 5))
# print(shulie(525, 6))


"""
16、篮球比赛  
【篮球比赛】篮球(5V5)比赛中，每个球员拥有一个战斗力，每个队伍的所有球员战斗力之和为该队伍的总体战斗力。现有10个球员准备分为两队进行训练赛，教练希望2  
个队伍的战斗力差值能够尽可能的小，以达到最佳训练效果。给出10个球员的战斗力，如果你是教练，你该如何分队，才能达到最佳训练效果?请说出该分队方案下的最小  
战斗力差值。  
输入描述:  
10个篮球队员的战斗力(整数，范围[1,10000]),战斗力之间用空格分隔，如:10987654321   
不需要考虑异常输入的场景。  
输出描述:  
最小的战斗力差值，如:1  
示例1:  
输入  
10 9 8 7 6 5 4 3 2 1  
输出  
1  
"""


def basketball(s):
    from itertools import combinations
    a1 = [int(x) for x in str(s).split(" ")]
    a2 = list(combinations(a1, len(a1) // 2))  # 排列组合：C(10, 5)
    min_diff = abs(sum(a1) - 2 * sum(a2[0]))
    for arr in a2:
        if abs(sum(a1) - 2 * sum(arr)) < min_diff:
            min_diff = abs(sum(a1) - 2 * sum(arr))
    return min_diff


# print(basketball("10 9 8 7 6 5 4 3 2 1"))

"""
17、标题:字符串变换最小字符串  
【字符串变换最小字符串】给定一个字符串s，最多只能进行一次变换，返回变换后能得到的最小字符串(按照字典序进行比较)。变化规则:交换字符串中任意两个不同位  
置字符。  
输入描述: 一串小写字母组成的字符串s  
输出描述: 按照要求进行变换得到最小字符串  
备注: s是都是小写字符组成1<=s.length<=1000  
示例1:  
输入  
abcdef  
输出  
abcdef  
"""


def minStr(s):
    """我理解这就是个选择排序法，找出最小的字符，替换到尽可能靠前的位置，只替换一次"""
    s = [x for x in s]
    for i in range(len(s) - 1):
        min_index = i
        for j in range(i + 1, len(s)):
            if s[j] < s[min_index]:
                min_index = j
        if min_index != i:
            s[min_index], s[i] = s[i], s[min_index]
            break
    return ''.join(s)


# print(minStr("bcdaef"))


"""
18、标题:构成的正方形数量  
【构成正方形数量】输入N个互不相同的二维整数坐标，求这N个坐标可以构成的正方形数量。(内积为零的的两个向量垂直)  
输入描述:  
第一行输入为N，N代表坐标数量，N为正整数。N<=100之后的K行输入为坐标xy以空格分隔，xy为整数，-10<=x,y<=10  
输出描述:  
输出可以构成的正方形数量。  
示例1:输入  
3  
1 3  
2 4  
3 1  
输出  
0  
"""


def square(s):
    from itertools import combinations, permutations
    def is_square(s):
        arrs = permutations(s, 4)  # 因为不知道四个坐标的顺序，所以只好排列一下穷举所有可能的顺序，四个坐标排列，共有A(4, 4) = 24种情况
        for arr in arrs:
            ac = (arr[2][0] - arr[0][0], arr[2][1] - arr[0][1])
            bd = (arr[3][0] - arr[1][0], arr[3][1] - arr[1][1])
            ab = (arr[1][0] - arr[0][0], arr[1][1] - arr[0][1])
            bc = (arr[2][0] - arr[1][0], arr[2][1] - arr[1][1])
            dc = (arr[2][0] - arr[3][0], arr[2][1] - arr[3][1])
            ad = (arr[3][0] - arr[0][0], arr[3][1] - arr[0][1])
            # 对角线垂直，临边均相互垂直的四边形为正方形，即：ac⊥bd、ab⊥bc、bc⊥dc、dc⊥ad、ad⊥ab
            if ac[0] * bd[0] + ac[1] * bd[1] == 0 and ab[0] * bc[0] + ab[1] * bc[1] == 0 and \
                    bc[0] * dc[0] + bc[1] * dc[1] == 0 and dc[0] * ad[0] + dc[1] * ad[1] == 0 and \
                    ad[0] * ab[0] + ad[1] * ab[1] == 0:
                return True

    if len(s) < 4:
        return 0
    num = 0
    for arr in combinations(s, 4):  # 排列组合：C(len(s), 4)
        arr = list(arr)
        if is_square(arr):
            num += 1
    return num


# 下列9个点，可以组成6个正方形
#   * * *
#   * * *
#   * * *
# print(square([(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]))

"""
19、标题:矩形相交的面积  
【矩形相交的面积】在坐标系中，给定3个矩形，求相交区域的面积。  
输入描述:  
3行输入分别为3个矩形的位置，分别代表“左上角x坐标”，“左上角y坐标”，“矩形宽”，“矩形高” -1000<=x,y<1000  
输出描述:  
输出3个矩形相交的面积，不相交的输出0  
示例:  
输入  
1 6 4 4  
3 5 3 4  
0 3 7 3  
输出  
2  
"""


def square_intersection_area(s1, s2, s3):
    a1 = [int(x) for x in s1.split(" ")]
    a2 = [int(x) for x in s2.split(" ")]
    a3 = [int(x) for x in s3.split(" ")]

    def have_comm(aaa1, aaa2):
        """返回两个区间的交集"""
        if aaa1[0] <= aaa2[0] and aaa1[1] >= aaa2[0]:
            return [aaa2[0], min(aaa1[1], aaa2[1])]
        elif aaa2[0] <= aaa1[0] and aaa2[1] >= aaa1[0]:
            return [aaa1[0], min(aaa1[1], aaa2[1])]
        return False

    def area(aa1, aa2):
        """返回相交部分矩形的信息数组：[“左上角x坐标”，“左上角y坐标”，“矩形宽”，“矩形高”]"""
        a = [aa1[0], aa1[0] + aa1[2]]  # 矩形1的x坐标区间
        b = [aa2[0], aa2[0] + aa2[2]]  # 矩形2的x坐标区间
        c = [aa1[1] - aa1[3], aa1[1]]  # 矩形1的y坐标区间
        d = [aa2[1] - aa2[3], aa2[1]]  # 矩形2的y坐标区间
        # 当区间a、b有交集，且区间d、d有交集的时候，说明矩形1、2相交
        if have_comm(a, b) and have_comm(c, d):
            xx = have_comm(a, b)
            yy = have_comm(c, d)
            return [xx[0], yy[1], xx[1] - xx[0], yy[1] - yy[0]]
        return False

    area1 = area(a1, a2)
    area2 = area(area1, a3) if area1 else False
    if area2:
        return area2[2] * area2[3]
    return 0


# print(square_intersection_area("1 6 4 4", "3 5 3 4", "0 3 7 3"))


"""
20、标题:字符统计及重排  
【字符统计及重排】给出一个仅包含字母的字符串，不包含空格，统计字符串中各个字母(区分大小写)出现的次数，并按照字母出现次数从大到小的顺序输出各个字母及  
其出现次数。如果次数相同，按照自然顺序进行排序，且小写字母在大写字母之前。  
输入描述:  
输入一行，为一个仅包含字母的字符串。  
输出描述:  
按照字母出现次数从大到小的顺序输出各个字母和字母次数，用英文分号分隔，注意末尾的分号;字母和次数间用英文冒号分隔。  
示例1:  
输入  
xyxyXX  
输出  
x:2;y:2;X:2;  
"""


def zi_fu_tong_ji(s):
    d1 = {}  # 统计小写字符次数
    d2 = {}  # 统计大写字符次数
    for c in s:
        if c.islower():
            d1[c] = d1.get(c, 0) + 1
        else:
            d2[c] = d2.get(c, 0) + 1
    ss = ''
    for k, v in sorted(d1.items(), key=lambda x: [x[1], x[0]]):
        ss += '%s:%s;' % (k, v)
    for k, v in sorted(d2.items(), key=lambda x: [x[1], x[0]]):
        ss += '%s:%s;' % (k, v)
    return ss


# print(zi_fu_tong_ji("xyxyXX"))

"""
21、转骰子  
【转骰子】骰子是一个立方体，每个面一个数字，初始为左1，右2，前3(观察者方向)，后4，上5，下6，用123456表示这个状态，放置在平面上，可以向左翻转(用L  
表示向左翻转1次)，可以向右翻转(用R表示向右翻转1次)，可以向前翻转(用F表示向前翻转1次)，可以向后翻转(用B表示向后翻转1次)，可以逆时针旋转(用A表示逆  
时针旋转90度)，可以顺时针旋转(用C表示顺时针旋转90度)，现从123456这个初始状态开始，根据输入的动作序列，计算得到最终的状态。骰子的初始状态和初始状  
态转动后的状态如图所示  
输入描述: 输入一行，为只包含LRFBAC的字母序列，最大长度为50，字母可重复  
输出描述: 输出最终状态  
示例1:  
输入  
L R  
输出  
123456  
"""


def throw_dice(s):
    arr = ['1', '2', '3', '4', '5', '6']

    def throw(operator):
        if operator == "L":
            arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[4], arr[5], arr[2], arr[3], arr[1], arr[0]
        elif operator == 'R':
            arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[5], arr[4], arr[2], arr[3], arr[0], arr[1]
        elif operator == 'F':
            arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[0], arr[1], arr[4], arr[5], arr[3], arr[2]
        elif operator == 'B':
            arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[0], arr[1], arr[5], arr[4], arr[2], arr[3]
        elif operator == 'A':
            arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[3], arr[2], arr[0], arr[1], arr[4], arr[5]
        elif operator == 'C':
            arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[2], arr[3], arr[1], arr[0], arr[4], arr[5]
        return arr

    for i in s:
        throw(i)
    return ''.join(arr)


# print(throw_dice("LRFBAC"))


"""
22、数字涂色  
【数字图色】疫情过后，希望小学终于又重新开学了，三年二班开学第一天的任务是将后面的黑板报重新制作。黑板上已经写了N个正整数，同学们需要给这每个数分别上  
一种颜色。为了让黑板报既美观又有学习意义，老师要求同种颜色的所有数都可以被这种颜色中最小的那个数整除。现在请你帮帮小朋友们，算算至少需要多少种颜色才能  
给这N个数进行上色。  
输入描述:  
第一行有一个正整数N，其中1<=N<=100。  
第二行有个N个int型整数(保证输入数据在[1,100]范围内)，表示黑板上各个正整数的值。  
输出描述:  
输出只有一个整数，为最少需要的颜色种数。  
示例1:  
输入  
3  
2 4 6  
输出  
1  
"""


def paint_nums(s):
    """
    每次遍历所有元素，并移除所有能被第一个元素整除的元素
    :param s:
    :return:
    """
    arr = [int(x) for x in s.split(" ")]
    arr.sort()
    l = len(arr)
    i = 0
    start = arr[0]
    color = 1
    while arr:
        if i > l - 1:
            i = 0
            color += 1  # 每轮遍历完，颜色加一
            start = arr[i]
        elif arr[i] % start == 0:
            arr.pop(i)
            l -= 1
        else:
            i += 1
    return color


# print(paint_nums("2 5 4 7 6"))


print("a", end=" ")


########################################################################################################
def min_operate(n):
    """
    2. 最少操作次数
    题目描述
    输入一个数字，对当前数字
    加一；
    减一；
    除以二(如果当前是偶数的话)各算一次操作，
    求把它变成 1 的最少操作次数。
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return min_operate(n // 2) + 1
    else:
        return min(min_operate(n - 1) + 1, min_operate(n + 1) + 1)

# print(min_operate(15))
