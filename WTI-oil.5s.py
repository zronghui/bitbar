#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
[【WTI原油期货】今日WTI原油期货实时行情,最新价格,走势分析_英为财情](https://cn.investing.com/commodities/crude-oil)
[美元人民币_外汇行情_网易财经](http://quotes.money.163.com/forex/hq/USDCNY.html)
"""
import pretty_errors
import requests
from lxml import etree

pretty_errors.activate()

# 美元人民币
USDCNY = 7.0621

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/59.0.3071.104 Safari/537.36',
}


def main():
    r = requests.get('https://cn.investing.com/commodities/crude-oil', headers=headers)
    xml = etree.HTML(r.text)
    currentPrice = float(xml.xpath("//span[@id='last_last']/text()")[0])
    priceSpan = xml.xpath("//div[@class='first inlineblock'][3]/span[@class='float_lang_base_2 bold']/text()")
    minPrice, maxPrice = list(map(lambda i: float(i.strip()), priceSpan[0].split('-')))
    currentPrice, minPrice, maxPrice = round(currentPrice * USDCNY, 2), \
                                       round(minPrice * USDCNY, 2), \
                                       round(maxPrice * USDCNY, 2)

    print(currentPrice)
    print('---')
    print('min:', minPrice, 'max:', maxPrice)
    upPrice = round(maxPrice - currentPrice, 2)
    upPercent = round(upPrice / (maxPrice - minPrice) * 100, 2)
    print('上涨空间：{} 上涨比例：{}'.format(upPrice, upPercent))
    print('---')
    print('详情 | href=https://cn.investing.com/commodities/crude-oil')
    print("刷新... | refresh=true")


if __name__ == '__main__':
    main()
