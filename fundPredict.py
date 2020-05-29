#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import sys

import requests

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7",
    "Connection": "keep-alive",
    "Referer": "http://favor.fund.eastmoney.com/",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}

cookies = {
    "Eastmoney_Fund": "007539_100038_005911_001549_001210_001595",
    "Eastmoney_Fund_Transform": "true",
    "qgqp_b_id": "d7bfa1516dc659e82434019f88644ca9",
    "st_asi": "delete",
    "st_inirUrl": "http%3A%2F%2Ffund.eastmoney.com%2Ffavor.html",
    "st_psi": "20191231100957577-119146300572-9396846884",
    "st_pvi": "85952350175164",
    "st_si": "31647646072534",
    "st_sn": "4",
    "st_sp": "2019-12-31%2010%3A04%3A09"
}


def getWeekday(s):
    # return 0, 1, …, 6
    # Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
    return int(datetime.datetime.strptime(s, '%Y-%m-%d').strftime('%w'))


if __name__ == '__main__':
    r = requests.get(url="http://api.fund.eastmoney.com/f10/lsjz?"
    # "callback=jQuery18306412047658073068_1590647234411&"
                         "fundCode=161725&"
                         # "fundCode=320007&"
                         "pageIndex=1&"
                         "pageSize=60&"
                         "startDate=&endDate=&_=1590647257810", headers=headers, cookies=cookies)
    # print(r.status_code)
    # print(len(r.text), r.text[:200])
    j = r.json()
    _sum = len(j["Data"]["LSJZList"])
    zhangNums = [0] * 7
    dieNums = [0] * 7
    for i in j["Data"]["LSJZList"]:
        index = getWeekday(i["FSRQ"]) - 1
        if not i["JZZZL"].startswith('-'):
            zhangNums[index] += 1
        else:
            dieNums[index] += 1
    print('涨', list(round(zhangNums[i] / (zhangNums[i] + dieNums[i]), 2) for i in range(5)))
    # print('跌', list(round(i / _sum, 2) for i in dieNums[:5]))
    # print('test')
