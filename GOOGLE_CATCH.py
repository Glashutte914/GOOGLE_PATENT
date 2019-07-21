# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:32:31 2019

@author: user

碰到反爬蟲
1 設header 模擬真人訪問
2 每次存取要有一定的間隔時間
3 用多個proxy輪流存取

中國專利模式
專利號碼
發明家
申請日期
Pulication日期
准予日期
分類
抽象abstract
說明Description
索賠Claims 
專利引用
引用:

"""
from lxml.html.clean import Cleaner
import json
import urllib.request
from bs4 import BeautifulSoup
import re
cleaner = Cleaner(style = True,scripts=True,comments=True,javascript=True,page_structure=False,safe_attrs_only=False)

req = urllib.request.Request('https://patents.google.com/patent/CN102486572A/zh')#網址
req.add_header('User-agent', 'Mozilla/5.0') #設header 模擬真人訪問
patent_html = urllib.request.urlopen(req)
soup = BeautifulSoup(patent_html, 'html.parser')


patent_description = soup.find("div", { "class" : "description" }).text #說明
patent_claims = soup.find("div", { "class" : "claims" }).text #索賠
patent_abstract = soup.find("div", { "class" : "abstract" }).text #索賠
patent_number = soup.find("span", { "itemprop" : "publicationNumber" }).text #專利號碼
#patent_inventor = soup.find("dd", { "itemprop" : "inventor" }).text #發明者
#assigneeMetaTag = soup.find("meta", { "scheme" : "assignee"})
#patentAssignee = assigneeMetaTag.attrs["content"]

patent_inventor = soup.find_all(itemprop=re.compile('inventor'))
for inventor in soup.find_all(itemprop=re.compile('inventor')):
   print (inventor.text, end=',')


