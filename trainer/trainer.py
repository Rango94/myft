import math
import numpy as np
import random
from Filehandler import corpusreader

class trainer():
    caSIZE=0
    cr=0
    filenum=0
    md=0
    Step=0
    step=0

    def __init__(self,md,step):
        self.md=md
        self.caSIZE=len(md.category_name)
        self.cr=corpusreader.corpusreader(md)
        self.filenum=len(md.filelist)
        self.Step=step
        self.step=step

    def train(self):
        maxloop=50000
        for i in range(maxloop):
            self.step=self.Step*(1-i/maxloop)
            print(self.step)
            self.trainfile()
        return self.md

    def trainfile(self):
        out=[]
        idx=random.randint(0,self.filenum-1)
        feature=self.cr.readafile(idx)
        try:
            if feature==0:
                print("***************")
                return 0
        except:
            for i in range(self.caSIZE):
                out.append(np.dot(feature,self.md.outputlayer[i]))
            output = self.softmax(out)
            ca=self.md.category[idx].index(max(self.md.category[idx]))

            if(ca==output.index(max(output))):
                print("分类正确")
            else:
                print("分类错误")
            e=0
            for i in range(self.caSIZE):
                if i==ca:
                    e=e-self.step*(output[i]-1)*self.md.outputlayer[i]
                    self.md.outputlayer[i]=self.md.outputlayer[i]-self.step*(output[i]-1)*feature
                else:
                    e = e - self.step * output[i] * self.md.outputlayer[i]
                    self.md.outputlayer[i] = self.md.outputlayer[i] - self.step * output[i] * feature
            for i in self.md.dic_list[idx].keys():
                self.md.dic[i]=self.md.dic[i]+e


    def softmax(self,vec):
        total=0;
        out=[]
        for i in vec:
            total+=math.pow(math.e,i)
        for i in vec:
            out.append(math.pow(math.e,i)/total)
        return out