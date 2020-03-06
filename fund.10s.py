#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
持有/关注的基金的涨跌情况，及预计亏损/盈利
"""
import datetime
import time
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


def valid_period():
    if datetime.date.today().weekday() > 4:
        sys.exit()
    now = datetime.datetime.now()
    if not (9 < now.hour < 15 or (now.hour == 9 and now.minute >= 30)):
        sys.exit()


def updateFunds(funds):
    cookies.update({'Eastmoney_Fund': '_'.join(funds.keys())})
    r = requests.get(
        "https://api.fund.eastmoney.com/Favor/Get",
        headers=headers,
        cookies=cookies
    )
    if r.status_code != 200:
        print('error | color=red')
        sys.exit()
    # ["Data"]["KFS"]*["FCODE"] 基金代码
    # ["Data"]["KFS"]*["gszzl"] 基金估算涨幅
    # ["Data"]["KFS"]*["SHORTNAME"] 基金名
    # ["Data"]["KFS"]*["RZDF"] 基金日增长率
    d = r.json()["Data"]["KFS"]
    for i in d:
        funds[i["FCODE"]].update({"status": i["gszzl"]})


def colorNum(num):
    color = "red" if float(num) > 0 else "green"
    return '{:.2f} | color={}'.format(float(num), color)


def printFundsStatus(funds):
    allIncome = 0
    for k, v in funds.items():
        income = v['money'] * float(v['status']) / 100
        v.update({'income': income})
        allIncome += income
    print(f'income:{colorNum(allIncome)}')
    print('---')
    for k, v in funds.items():
        print(f'{v["name"]}:{round(v["income"], 2)}  {colorNum(v["status"])}')
    print('基金详情 | href=http://data.eastmoney.com/hsgt/index.html')
    print("刷新... | refresh=true")


if __name__ == '__main__':
    valid_period()
    funds = {
        '008087': {'name': '华夏 5g', 'money': 5400, 'status': 0, 'income': 0},
        '519005': {'name': '海富通 ', 'money': 2000, 'status': 0, 'income': 0},
        '110022': {'name': '易方达消费 ', 'money': 4000, 'status': 0, 'income': 0},
        '003834': {'name': '华夏能源', 'money': 5000, 'status': 0, 'income': 0},
        '040046': {'name': '华安纳斯达克', 'money': 2000, 'status': 0, 'income': 0},
        '519674': {'name': '银河创新', 'money': 100, 'status': 0, 'income': 0},
        '005911': {'name': '广发双擎', 'money': 100, 'status': 0, 'income': 0},
        '320007': {'name': '诺安成长', 'money': 100, 'status': 0, 'income': 0},
        '161725': {'name': '招商白酒', 'money': 100, 'status': 0, 'income': 0},
    }
    updateFunds(funds)
    printFundsStatus(funds)