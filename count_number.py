# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 13:50:55 2019

@author: user
"""

import urllib
from bs4 import BeautifulSoup

html = urllib.request.urlopen("https://zh.wikipedia.org/zh-tw/ISO_3166-1").read()
soup = BeautifulSoup(html, 'html.parser')

#利用 class 從該 HTML 裡取得特定表格
table = soup.find('table', {'class': 'wikitable sortable'})

#產生欄位名稱
columns = [th.text.replace('\n', '') for th in table.find('tr').find_all('th')]
columns
['英文短名稱', '二位代碼', '三位代碼', '數字代碼', 'ISO 3166-2', '中文名稱', '獨立主權']

#patent_inventor = soup.find("dd", { "itemprop" : "inventor" }).text #發明者
#產生每個國家的對應資料
trs = table.find_all('tr')[1:5] #從table裡找到tr
rows = list()
for tr in trs:
    #從tr裡找到td
    rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])

print(rows)
