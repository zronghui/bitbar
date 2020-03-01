#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import re

import chardet
import pretty_errors
import requests
import gzip

# from icecream import ic
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "http://tianqi.2345.com/indexs.htm",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}
r = requests.get("http://tianqi.2345.com/luan/58311.htm", headers=headers)

# ic(r.headers, chardet.detect(r.content), r.apparent_encoding, r.encoding)
r.encoding = 'gbk'
text = r.text
results = re.findall(r'今日天气：(.*)；明日天气：(.*) 点击查看', text)[0]

# 这接口不准
# # where to get the token -> https://aqicn.org/api/
# AQI_TOKEN = "993bbeae0ace031d098a8f02a873abff8e2efd43"
# AQI_CITY = "luan"
# AQI_URL = f"http://api.waqi.info/feed/{AQI_CITY}/?token={AQI_TOKEN}"
# # print(AQI_URL)
# aqi = requests.get(AQI_URL).json()['data']['aqi']

r = requests.get("http://tianqi.2345.com/air-58311.htm", headers=headers)
r.encoding = 'gbk'
text = r.text
results2 = re.findall(r'</span><i>(.*?)</i>.*?<div class="td td3 tc"><span>(.*?)</span>', text)
# print(results2)
# [('良', '61'), ('优', '44'), ...
print(f'🌡️{results[0].split("，")[0]}{results[0].split("，")[1].strip("气温")}😷{results2[0][0]}{results2[0][1]}')
print("---")
print(f'今天：{results[0]} {results2[0][0]}{results2[0][1]}')
print(f'明天：{results[1]} {results2[1][0]}{results2[1][1]}')
print("六安天气详情... | href=http://tianqi.2345.com/today-58311.htm")
print("六安空气质量详情... | href=http://tianqi.2345.com/air-58311.htm")
print("刷新... | refresh=true")
