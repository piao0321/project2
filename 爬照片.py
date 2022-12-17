# -*- coding: utf-8 -*-
"""
@Time :2022/12/3 15:41
@Author :Lai Xiangyuan
@Email :2936885192@qq.com
@File :爬照片.py
@ID :12003990122
"""

import time
from urllib import request
import aiohttp
import asyncio
import requests
from lxml import etree
import urllib.request
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from urllib.request import Request, urlopen

import urllib.error

start = 10517

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
year = 2022
page = 1

# for i in range(1, 2):
#     url = "http://dilidili12.com/acg/0/0/all/" + str(i) + ".html"
#     driver = webdriver.Edge()
#     driver.get(url)
#     time.sleep(2)
#     # print(url)
#     # url = 'http://1.14.157.239:7022/getsortdata_all_z.php?action=acg&page=400&year=0&area=all&class=0&dect=&id='
#     # url2 = "http://121.4.190.96:9991/getsortdata_all_z.php?action=acg&page=1&year=0&area=all&class=0&dect=&id="
#     # req = urllib.request.Request(url, headers=header)
#     # html_str = request.urlopen(req)
#     # date = html_str.read().decode()
#     # print(date)
#     # html = etree.HTML(date)
#     htmp_q = driver.page_source
#     html = etree.HTML(htmp_q)
#     driver.close()
#     ret1 = html.xpath('/html/body/div[2]/div[3]/ul/li/a/div[2]/p/text()')
#     htmt_list = html.xpath('/html/body/div[2]/div[3]/ul/li/a/@href')
#     # print(ret1)
#     # print(htmt_list)
#
#     # zip同时循环两个列表
#     for m, n in zip(htmt_list, ret1):
#         name = r"./download/" + str(start) + ".txt"
#         start += 1
#         f = open(name, 'w', encoding="utf-8")
#         f.write("http://dilidili12.com" + m + "\n\n")
#         f.write(n + "\n\n\n")
#         try:
#             temp_html = "http://dilidili12.com" + m
#             request = Request(temp_html, headers=header)
#             response = urlopen(request, timeout=2)
#             date = response.read().decode()
#             html = etree.HTML(date)
#             info = html.xpath('/html/body/div[2]/div[2]/div[2]/dl/dd[2]/text()')
#             presentation = html.xpath('/html/body/div[2]/div[2]/div[2]/dl/dt[2]/div/div[2]/text()')
#             f.write("".join(info) + "\n\n")
#             f.write("".join(presentation) + "\n\n")
#
#         except urllib.error.URLError as error:
#             print(error)
#             f.write("暂无\r\n")

# 添加千与千寻
# url = "http://dilidili12.com/mov/15641/"
# name = r"./download/" + str(start) + ".txt"
# f = open(name, 'w', encoding='utf-8')
# f.write(url + "\n\n")
# request = Request(url, headers=header)
# response = urlopen(request, timeout=2)
# date = response.read().decode()
# html = etree.HTML(date)
# n = html.xpath("/html/body/div[2]/div[2]/div[2]/dl/dt[1]/text()")
# info = html.xpath("/html/body/div[2]/div[2]/div[2]/dl/dd[2]/text()")
# presentation = html.xpath("/html/body/div[2]/div[2]/div[2]/dl/dt[2]/div/div[3]/text()")
# f.write(n[0] + "\n\n\n")
# f.write("".join(info) + "\n\n")
# f.write("".join(presentation) + "\n\n")


url = "https://cn.bing.com/images/search?q=%E6%98%8E%E6%98%9F%E8%AF%81%E4%BB%B6%E7%85%A7&form=IRFLTR&first=1&tsc=ImageHoverTitle&cw=1177&ch=737"
driver = webdriver.Edge()
driver.get(url)
time.sleep(10)
htmp_q = driver.page_source
html = etree.HTML(htmp_q)
driver.close()
img = html.xpath('//*[@id="emb3A6203B"]/attribute::src')

print(img)
"""
https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E8%89%BA%E4%BA%BA&rsv_spt=1&rsv_iqid=0xe6b3a1910010de29&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=15&rsv_sug1=21&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=%25E4%25B8%25AD%25E5%259B%25BDyi%2526%252339%253Bren&rsp=5&inputT=8343&rsv_sug4=8954
https://www.baidu.com/s?wd=%E4%B8%AD%E5%9B%BD%E8%89%BA%E4%BA%BA&rsv_spt=1&rsv_iqid=0xe6b3a1910010de29&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=15&rsv_sug1=21&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=%25E4%25B8%25AD%25E5%259B%25BDyi%2526%252339%253Bren&rsp=5&inputT=8343&rsv_sug4=8954

"""

