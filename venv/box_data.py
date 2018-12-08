# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import urllib2
import json
import pygal



# 打开网页，获取源码
def open_page(url):
    try:
        netword = urllib2.urlopen(url)
    except urllib2.HTTPError as hp:
        print(hp)
    else:
        # 采用BeautifulSoup来解析，且指定解析器
        html = bs(netword, 'lxml')
        return html


# 获取网页数据
def get_page(url):
    # 电影名称，上映天数，电影总票房，票房占比，排片场次，排片占比，场均人次，上座率
    movieName, releaseInfo, sumBoxInfo, boxInfo, boxRate, showInfo, showRate, avgShowView, avgSeatView = [], [], [], [], [], [], [], [], []
    html = open_page(url)
    print(html)
    p = html.find('p')
    text = p.get_text()
    # 将数据转换为python能够处理的格式
    jsonObj = json.loads(text)
    # 获取字典里面特定的键对应的键值
    data = jsonObj.get('data')
    # 想要的数据就在字典的键"list"对应的值
    lists = data.get('list')
    for list in lists:
        # 获取字典里面特定的键对应的键值,并存储到列表中去
        movieName.append(list.get('movieName'))
        releaseInfo.append(list.get('releaseInfo'))
        sumBoxInfo.append(list.get('sumBoxInfo'))
        boxInfo.append(list.get('boxInfo'))
        boxRate.append(list.get('boxRate'))
        showInfo.append(list.get('showInfo'))
        showRate.append(list.get('showRate'))
        avgShowView.append(list.get('avgShowView'))
        avgSeatView.append(list.get('avgSeatView'))
    return movieName, releaseInfo, sumBoxInfo, boxInfo, boxRate, showInfo, showRate, avgShowView, avgSeatView


url = 'https://box.maoyan.com/promovie/api/box/second.json'
movieName, releaseInfo, sumBoxInfos, boxInfos, boxRate, showInfo, showRate, avgShowView, avgSeatView = get_page(url)