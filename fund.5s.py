#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
北向资金动态
"""
import datetime
import time
import sys

if datetime.date.today().weekday() > 4:
    sys.exit()
now = datetime.datetime.now()
if not (9 < now.hour < 15 or (now.hour == 9 and now.minute >= 30)):
    sys.exit()
from requests_html import HTMLSession

# https://cncert.github.io/requests-html-doc-cn
headers = {
    'authority': 'xclient.info',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'sec-fetch-site': 'same-origin',
    'referer': 'https://xclient.info/s/doo.html',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7',
    'cookie': '_ga=GA1.2.1129443542.1571488491; _gid=GA1.2.812175064.1571724208; popcashpu=1; PHPSESSID=7ht75uvpk4vbpj8rsiqtkofilg; Hm_lvt_befb95b3cbb10a937d15e5181625c9f2=1571488491,1571724207,1571746643; Hm_lpvt_befb95b3cbb10a937d15e5181625c9f2=1571750275',
}
session = HTMLSession()
r = session.get("http://push2.eastmoney.com/api/qt/kamt/get?fields1=f1,f2,f3,f4&fields2=f51,f52,f53,f54")

# 沪股通
hk2sh = r.json()['data']['hk2sh']['dayNetAmtIn'] / 10000
# 深股通
hk2sz = r.json()['data']['hk2sz']['dayNetAmtIn'] / 10000
color = "red" if float(hk2sh + hk2sz) > 0 else "green"
print('北{:.2f} | color={}'.format(hk2sh + hk2sz, color))
print('---')
print('沪深港通资金流向详情 | href=http://data.eastmoney.com/hsgt/index.html')
color = "red" if float(hk2sh) > 0 else "green"
print('沪股通: {:.2f} | color={}'.format(hk2sh, color))
color = "red" if float(hk2sz) > 0 else "green"
print('深股通: {:.2f} | color={}'.format(hk2sz, color))
