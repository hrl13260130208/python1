#!/usr/bin/env python
# coding=utf-8
from urllib import request
import re
import requests
import json
import os
import sys
from bs4 import BeautifulSoup

def get_html(url):
    data = requests.get( url )
    data.encoding = 'utf-8'
    data = data.text
    return data

def get_url_argv(html):
    soup = BeautifulSoup(html, "html.parser")
    for ul_tag in soup.find_all("ul", class_="nav-second-level"):
        for a_tag in ul_tag.find_all("a", class_="zc"):
            codes = a_tag["codes"]
            name = a_tag.get_text()
            list.append([codes, name])

def get_detail_url(html):
    soup = BeautifulSoup(html, "html.parser")
    for table in soup.find_all("table"):
        for a_tag in table.find_all("a"):
            detail_url.append("http://cz.fjzfcg.gov.cn"+a_tag["href"])



def get_next_page(html):
    soup = BeautifulSoup(html, "html.parser")
    for div_tag in soup.find_all("div",class_="pageGroup"):
        num=-1
        for active_tag in div_tag.find_all("button",class_="active"):
            num=active_tag.get_text()
        for next in div_tag.find_all("button"):
            print("next:"+next.get_text())
            if "下一页" == next.get_text().strip():
                print(num)
                return num
        return

url="http://cz.fjzfcg.gov.cn/3500/openbidlist/f9ebc6637c3641ee9017db2a94bfe5f0/"

list=[]
urls=[]
detail_url=[]
html=get_html(url)
print("++++++++++++++++++++")
get_url_argv(html)
print(list)


#获取各个地区对应的URLs
for argv in list:
    new_url=url+"?zone_code="+argv[0]+"&zone_name="+argv[1]
    urls.append(new_url)

first_level_url_html=get_html(urls[0])
print(first_level_url_html)
get_detail_url(first_level_url_html)
print(get_next_page(first_level_url_html))











