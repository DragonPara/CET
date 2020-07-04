import json
insert={}
with open("大学英语四六级词汇完整打印版.txt","r",encoding="utf8")as fp:
    word=""
    count=0
    sign=0
    key=""
    value=""
    while(1):
        count+=1
        a=fp.read(1)
        if a=="":
            break
        if a!=" ":
            if ord(a)>122:
                sign=1
            if a!="\n":
                word+=a
            if a=="\n":
                a=" "
        if a==" ":
            if sign==0:
                key=word
            if sign==1:
                # print("意思")
                sign=0
                value=word
                if key!="":
                    insert[key]=value
                key=""
                value=""
            # print(word)
            word=""
count=0
for i in insert.keys():
    count+=1
    print(i,"  :  ",insert[i])
insertFile=open("p1.json","w")
json.dump(insert,insertFile)
insertFile.close()
# print(insert)