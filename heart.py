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
        if len(value)>0:
            if value=="exit":
                print("欢迎下次使用")
                break
            if value[0]=="+":
                if value=="+yisi":
                    withYisi(words,words_cp)
                else :
                    first(value[1],words,words_cp)
def withYisi(words,words_cp):
    value=""
    while(1):
        if words_cp==[]:
            print("\n你已完成一次复习\n")
            words_cp = list(words)
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
with open("p1.json","r",encoding="utf8")as fp:
    words=json.load(fp)
    words_cp = list(words)
    while(1):
        if words_cp==[]:
            print("\n你已完成一次复习\n")
            words_cp = list(words)
        word=random.sample(words_cp,1)
        word=str(word[0])
        words_cp.remove(word)
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