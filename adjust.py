import json
with open("大学英语四六级词汇完整打印版.txt","r",encoding="utf8")as fp:
    word=""# 暂时存储区
    sign=0 # 中文标记
    insert={}
    while(1):
        a=fp.read(1)
        if a=="":
            break
        if a!=" ":
            if ord(a)>122:# <=122的是. \n 字母
                sign=1
            if a!="\n":
                word+=a
            if a=="\n":
                a=" "
        if a==" ":
            if sign==0:# 如果不包含汉字
                key=word #重置key
                value=""#只有当key被重置，value才会初始化
            if sign==1:# 如果包含汉字
                sign=0
                if key in insert.keys():#如果当前单词已经存在于字典中，加个空格
                    value+=" "
                value+=word
                insert[key]=value
            word=""
for i in insert.keys():
    print(i,":",insert[i])
insertFile=open("p1.json","w")
json.dump(insert,insertFile)# 输出到json文件
insertFile.close()