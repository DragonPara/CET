import json
import random
def first(firstWord,words,words_cp):
    value=""
    while(1):
        if words_cp==[]:
            print("\n你已完成一次复习\n")
            words_cp = list(words)
        words_cp=list(words_cp)
        word=random.sample(words_cp,1)
        word=str(word[0])
        words_cp.remove(word)
        if(word[0]==firstWord):
            print("单词：",word)
            print("翻译：",words[word],"\n")
            value=input("")
        if len(value)>0:# 若不加此判断，当word[0]!=first时，下方value[0]会越界
            if value=="exit":# 退出
                print("欢迎下次使用")
                break
            if value[0]=="+":# 判断是否采用控制
                if value=="+yisi":
                    withYisi(words,words_cp)
                else :
                    first(value[1],words,words_cp)
def withYisi(words,words_cp):
    value=""
    while(1):
        if words_cp==[]:
            print("\n你已完成一次复习\n")
            words_cp = list(words)#重新初始化
        word=random.sample(words_cp,1)
        word=str(word[0])
        words_cp.remove(word)
        print("单词：",word)
        print("翻译：",words[word],"\n")
        value=input("")
        if len(value)>0:
            if value=="exit":
                print("欢迎下次使用")
                break
            if value[0]=="+":
                if value=="+yisi":
                    withYisi(words,words_cp)
                else :
                    first(value[1],words,words_cp)
print("四六级词汇复习\n")
count=0
with open("p1.json","r",encoding="utf8")as fp:
    count+=1
    if count%100==0:
        print("本次已复习",count,"个单词")
        for i in range(5):
            print("*"*i)
    words=json.load(fp)
    words_cp = list(words)
    while(1):
        if words_cp==[]:
            print("\n你已完成一次复习\n")
            words_cp = list(words)
        word=random.sample(words_cp,1)# 随机选一个单词
        word=str(word[0])
        words_cp.remove(word)# 防止同一个单词被多次选中
        print("单词：",word)
        value=input("")
        print("翻译：",words[word],"\n")
        if len(value)>0:
            if value=="exit":
                print("欢迎下次使用")
                break
            if value[0]=="+":
                if value=="+yisi":
                    withYisi(words,words_cp)
                else :
                    first(value[1],words,words_cp)