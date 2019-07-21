# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:15:20 2019

@author: user
"""
from requests_html import HTML
import requests

def fetch(url):
    response = requests.get(url)
    response = requests.get(url, cookies={'over18': '1'})  # 一直向 server 回答滿 18 歲了 !
    return response

'print(resp.text) # result of setp-1'


def parse_article_entries(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.r-ent') #每一列的所有元素儲存點
    return post_entries

url = 'https://www.ptt.cc/bbs/movie/index.html'
resp = fetch(url)  # step-1
post_entries = parse_article_entries(resp.text)  # step-2

print(post_entries)  # result of setp-2


def parse_article_meta(entry):
    '''
    每筆資料都存在 dict() 類型中：key-value paird data
    '''
    return {
        'title': entry.find('div.title', first=True).text, #標題
        'push': entry.find('div.nrec', first=True).text, #推文
        'date': entry.find('div.date', first=True).text, #日期
        'author': entry.find('div.author', first=True).text, # 作者
    }
num = 8126
url = 'https://www.ptt.cc/bbs/movie/index' + str(num) + '.html'
resp = fetch(url)  # step-1
post_entries = parse_article_entries(resp.text)  # step-2

for entry in post_entries:
    meta = parse_article_meta(entry)
    print(meta)  # result of setp-3