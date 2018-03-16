import os
import jieba
import random
import numpy as np

class model():
    # 输出层参数
    outputlayer = 0
    filelist=[]
    idx=0
    dic_tmp=[]
    dic={}
    dic_list=[]
    SIZE=0
    category_name={}
    # 类别向量
    category=[]
    def __init__(self,path,size):
        self.SIZE=size
        for root, dirs, files in os.walk(path):
            na = 0
            for name in files:
                if name.split("_")[0] not in self.category_name:
                    self.category_name[name.split("_")[0]]=na
                    na+=1
                tmp_ca=[]
                for k in range(6):
                    if k==self.category_name[name.split("_")[0]]:
                        tmp_ca.append(1)
                    else:
                        tmp_ca.append(0)
                self.category.append(tmp_ca)
                self.filelist.append(root+"/"+name)
        self.genareteoutputlayer()
        for i in range(len(self.filelist)):
            self.readcorpus()

    def readcorpus(self):
        dic_subtmp={}
        f=open(self.filelist[self.idx],"r",encoding="utf-8")
        line=f.readline()
        Line=""
        while(line!=""):
            Line+=self.cn(line)
            line=f.readline()
        for i in jieba.cut(Line, cut_all=False):
            if i not in self.dic_tmp:
                self.dic_tmp.append(i)
                self.genarete(i)
            if i not in dic_subtmp:
                dic_subtmp[i]=1
            else:
                dic_subtmp[i]=dic_subtmp[i]+1
        self.dic_list.append(dic_subtmp)
        self.idx+=1

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


    def genareteoutputlayer(self):
        vecs=[]
        for k in range(len(self.category_name)):
            vec = []
            for i in range(self.SIZE):
                vec.append((0.5 - random.random()) / self.SIZE)
            vecs.append(vec)
        self.outputlayer=np.array(vecs)

# md=model("F:/test",100)
# md=model("F:/test",100)




