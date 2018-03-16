import os
import jieba
import random
import numpy as np

class model():
    filelist=[]
    idx=0
    dic_tmp=[]
    dic={}
    SIZE=0
    def __init__(self,path,size):
        self.SIZE=size
        for root, dirs, files in os.walk(path):
            for name in files:
                self.filelist.append(root+"/"+name)
        for i in range(len(self.filelist)):
            self.readcorpus()
        for i in self.dic_tmp:
            self.genarete(i)

    def readcorpus(self):
        print(self.filelist[self.idx])
        f=open(self.filelist[self.idx],"r",encoding="utf-8")
        line=f.readline()
        Line=""
        while(line!=""):
            Line+=self.cn(line)
            line=f.readline()
        for i in jieba.cut(Line, cut_all=False):
            if i not in self.dic_tmp:
                self.dic_tmp.append(i)
        self.idx+=1
        # print(len(self.dic_tmp))

    def cn(self,str):
        out=""
        for e in str:
            if e >= u'\u4e00' and e<=u'\u9fa5':
                out+=e
        return out

    def genarete(self,term):
        vec=[]
        for i in range(self.SIZE):
            vec.append((0.5-random.random())/self.SIZE)
        self.dic[term]=np.array(vec)

    def getVector(self,term):
        # print(self.dic[term])
        return self.dic[term]

md=model("F:/test",100)
print(md.getVector("毕加索"))
# md=model("F:/w2vcorpus/neteasydataset_602151/corpus_6_4000",100)



