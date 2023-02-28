# -*- coding:utf-8 -*-
import argparse
import requests
from datetime import datetime
from time import sleep


def login(phone, password):
    """登陆"""
    while True:
        res = requests.post('https://ypt.bjyipai.cn/api/login/login', data={'phone': phone, 'password': password})
        if res.json().get("code") != 1:
            print("登陆失败：%s，1秒后重试！" % res.json().get("msg"))
            sleep(1)
        else:
            print("%s登陆成功！" % phone)
            return res.json().get("data", {})


def get_cid(headers, start_time):
    """通过场馆开馆时间，获得场馆ID"""
    while True:
        res = requests.post('https://ypt.bjyipai.cn/api/index/bidlist', headers=headers)
        if res.json().get("code") != 1:
            print("查询场馆ID失败：%s，1秒后将重试！" % res.json().get("msg"))
            sleep(1)
        else:
            bid_list = res.json().get("data")
            for b in bid_list:
                if b.get("starttime") == start_time:
                    print("匹配到【%s】场次，开馆时间：%s" % (b.get('title'), b.get("starttime")))
                    return b.get("cid")
            print("%s无匹配场馆！" % str(start_time))
            return False


def get_goods_list(headers, cid, page):
    """查询商品列表信息"""
    res = requests.post("https://ypt.bjyipai.cn/api/bid/goodslist", data={'cid': cid, 'page': page}, headers=headers)
    if res.json().get("code") != 1:
        print(res.json().get("msg"))
    return res.json().get("data", {})


def get_good_detail(headers, pid):
    """查询商品列表信息"""
    res = requests.post("https://ypt.bjyipai.cn/api/bid/goodDetail", data={'id': pid}, headers=headers)
    if res.json().get("code") != 1:
        print(res.json().get("msg"))
    return res.json().get("data", {})


def prepare_goods_id(headers, cid, goods_id, more_than=2500):
    """准备商品ID"""
    goods_id = goods_id and str(goods_id).split(",") or []
    prepare_goods_id = []
    if goods_id:
        print("优先购买商品信息如下：")
        for id in goods_id:
            good = get_good_detail(headers, int(id))
            prepare_goods_id.append((good.get("pid"), float(good.get("price")), good.get("title")))
            print("%s，价格：%s，pid：%s" % (good.get("title"), good.get("price"), good.get("pid")))
    pages = get_goods_list(headers, cid, page=1).get("pages")  # 获取商品总页数
    print("商品总页数：%s" % str(pages))
    goods_list = []
    for i in range(1, pages):
        i_list = get_goods_list(headers, cid, pages-i+1)
        for good in i_list.get("list"):
            if float(good.get("price")) >= more_than:
                goods_list.append((good.get("pid"), float(good.get("price")), good.get("title")))
    # 按价格倒序排列
    goods_list.sort(key=lambda x: x[1])
    print("匹配到的商品总数：%s" % str(len(prepare_goods_id + goods_list)))
    return prepare_goods_id + goods_list


def submit_order(headers, pid):
    """立即购买"""
    try:
        res_json = requests.post("https://ypt.bjyipai.cn/api/bid/submitorder", data={'pid': pid},
                                 headers=headers).json()
        if res_json.get("code") == 2001 or '此商品已被抢走' in res_json.get("msg") or '未开始' in res_json.get("msg"):
            return res_json.get("msg", False)
        else:
            print(res_json.get("msg"))
            return True
    except:
        return False


def auto_take(headers, goods_list, need_num):
    """自动抢单"""
    total_price = 0
    success_num = 0
    failure_num = 0
    for g in goods_list:
        # 数量够了，就退出
        if need_num <= 0:
            break
        # 如果抢到，need_num就减去1
        result = submit_order(headers, g[0])
        if result is True:
            total_price += g[1]
            print("%s购买成功，价格%s" % (g[2], g[1]))
            need_num -= 1
            success_num += 1
            # 完成一单暂停三秒
            sleep(3)
        else:
            if '未开始' in result:
                return result
            else:
                failure_num += 1
    print("本次活动总计抢到%s件商品，花费：%s，抢购失败次数：%s" % (str(success_num), str(total_price), str(failure_num)))


def get_order_sell(headers, phone, cid):
    """获得用户待售商品列表"""
    # 拼接请求头
    res_json = requests.post("https://ypt.bjyipai.cn/api/bid/myorderSell", data={'page': 1, 'pageSize': 10, 'type': 2},
                             headers=headers).json()
    result = []
    sell_list = res_json.get("data", {}).get("list", [])
    for i in sell_list:
        if i.get("cid") == cid:
            result.append((i.get("pro_title"), i.get("price"), i.get("pid")))
    if result:
        result.sort(key=lambda x: x[2])
        result.sort(key=lambda x: x[1], reverse=True)
        print("用户%s在场馆%s的待卖商品列表如下：" % (phone, cid))
        for i in result:
            print("%s，价格：%s，pid：%s" % i)
        return ",".join([str(x[2]) for x in result])
    else:
        print("该用户无待售商品！")
        return ""


def get_args():
    """处理请求参数"""
    parser = argparse.ArgumentParser()
    parser.usage = "ypt定时抢购脚本"
    parser.epilog = """
python3 ypt.py -seller_phone= -seller_password= -buyer_phone= -buyer_password -c_time=19:30 -start_time=19:27 -need_num=
    """
    parser.add_argument('-seller_phone', type=str, dest='phone')
    parser.add_argument('-seller_password', type=str, dest='password')
    parser.add_argument('-buyer_phone', type=str, dest='phone')
    parser.add_argument('-buyer_password', type=str, dest='password')
    parser.add_argument('-c_time', type=str, dest='c_time', help='匹配几点的场次，12:30 或者 19:30', default='19:30')
    parser.add_argument('-start_time', type=str, dest='start_time', help='开抢时间', default='19:27')
    parser.add_argument('-need_num', type=int, dest='need_num', help='需要数量', default=2)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_args()



    if args.get_sells is True:
        ###################### 查询用户待卖商品列表 ###################
        # args.phone = ''  # 电话
        # args.password = ''  # 密码
        # args.c_time = '19:30'  # 匹配几点的场次，12:30 或者 19:30
        ###########################################################
        # 登陆
        data = login(args.phone, args.password)
        # 拼接请求头
        headers = {'userid': str(data.get("user_id")), 'token': data.get("token")}
        # 获得场次ID
        cid = get_cid(headers, args.c_time)
        # 获得待售商品
        sells = get_order_sell(headers, args.phone, cid)
        if sells:
            print('"' + sells + '"')
    else:
        ###################### 调试参数 #############################
        # args.phone = ''  # 电话
        # args.password = ''  # 密码
        # args.c_time = '19:30'  # 匹配几点的场次，12:30 或者 19:30
        # args.start_time = '19:27'  # 开抢时间
        # args.need_num = 4  # 要抢多少个
        # args.goods_id = "19437,19070,19933,19822"  # 指定要购买的商品ID
        ###########################################################
        # 登陆
        data = login(args.phone, args.password)
        # 拼接请求头
        headers = {'userid': str(data.get("user_id")), 'token': data.get("token")}
        # 获得场次ID
        cid = get_cid(headers, args.c_time)
        # 提前进入场馆，准备数据
        goods_list = prepare_goods_id(headers, cid, args.goods_id, more_than=2500)
        # 设置结束时间
        start_hour, start_minute = [int(x) for x in args.start_time.split(":")]
        start_time = datetime.now().replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
        end_time = datetime.now().replace(hour=start_hour, minute=start_minute + 10, second=0, microsecond=0)
        print("数据已经准备就绪，等待开抢...")
        # 定时自动抢need_num个good
        has_print = False
        while True:
            if datetime.now() > end_time:
                print("这个点儿【%s】已经没货了，停止抢购！" % datetime.now().replace(microsecond=0))
                break
            elif datetime.now() > start_time:
                if has_print is False:
                    print("【%s】现在开始抢购！" % datetime.now().replace(microsecond=0))
                    has_print = True
                result = auto_take(headers, goods_list, args.need_num)
                if result is not None and '未开始' in result:
                    print(result)
                    continue
                else:
                    break
            else:
                sleep(0.01)
