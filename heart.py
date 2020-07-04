import json
import random
print("四六级词汇复习\n")
count=0
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
        if value=="exit":
            print("欢迎下次使用")
            break