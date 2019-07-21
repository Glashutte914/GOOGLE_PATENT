#encoding=utf-8
'''
Created on 2018-2-6

'''
import opencc
import jieba

# 字典
jieba.load_userdict("user_dict.txt") 
rt = open(r"r_jieba.txt", "r").read()
wt =  open(r"w_jieba1.txt", "w")
# 这里的_word_ngrams方法其实就是sklearn中CountVectorizer函数中用于N-Gram的方法，位置在D:\Python27\Lib\site-packages\sklearn\feature_extraction\text.py
def _word_ngrams(tokens, stop_words=None,ngram_range=(1,1)):
        """Turn tokens into a sequence of n-grams after stop words filtering"""
        # handle stop words
        if stop_words is not None:
            tokens = [w for w in tokens if w not in stop_words]

        # handle token n-grams
        min_n, max_n = ngram_range
        if max_n != 1:
            original_tokens = tokens
            tokens = []
            n_original_tokens = len(original_tokens)
            for n in range(min_n,
                            min(max_n + 1, n_original_tokens + 1)):
                for i in range(n_original_tokens - n + 1):
                    tokens.append(" ".join(original_tokens[i: i + n]))

        return tokens

text = "我去云南旅游，不仅去了玉龙雪山，丽江古城还去，很喜欢丽江古城"
# 簡轉繁
cc = opencc.OpenCC('s2t') 
cut = jieba.cut(rt, cut_all=True)
listcut = list(cut)
n_gramWords = _word_ngrams(tokens = listcut,ngram_range=(1,2))
# print (n_gramWords)
for n_gramWord in n_gramWords:
    print (cc.convert(n_gramWord))
    
    text = "圓滾滾的牙牙癢癢的人幹"
# 簡轉繁
"""words = jieba.cut(text, cut_all=False)
print ("Output 精確模式 Full Mode：")
for word in words:
    print (word)
    wt.write(word)
    wt.write("\n")"""