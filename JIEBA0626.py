#encoding=utf-8
"""
Created on Wed Jun 26 15:47:38 2019

@author: user
"""

import jieba
rt = open(r"r_jieba.txt", "r").read()
wt =  open(r"w_jieba1.txt", "w")
#sentence = "獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
#print ("Input：", sentence)
#1. 精確模式 ：將句子最精確地切開，叫適合文本分析。
#寫法:words = jieba.cut(content, cut_all=False)
#2.全模式：把句子中所有的可以成詞的詞語都掃描出來, 速度快。
#寫法:words = jieba.cut(content, cut_all=True)
#3.搜索引勤模式：在精確模式的基礎上對長詞再次切分，提高召回率，
#適合用於搜尋引擎分詞。          
words = jieba.cut(rt, cut_all=False)
print ("Output 精確模式 Full Mode：")
for word in words:
    print (word)
    wt.write(word)
    wt.write("\n")
    


