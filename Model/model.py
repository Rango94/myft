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

    def buildemodel(self,path,size):
        self.SIZE=size
        for root, dirs, files in os.walk(path):
            na = 0
            for name in files:
                if name.split("_")[0] not in self.category_name:
                    self.category_name[name.split("_")[0]]=na
                    na+=1
                tmp_ca=[]
                for k in range(len(self.category_name)):
                    if k==self.category_name[name.split("_")[0]]:
                        tmp_ca.append(1)
                    else:
                        tmp_ca.append(0)
                self.category.append(tmp_ca)
                self.filelist.append(root+"/"+name)
        print("种类："+str(len(self.category_name)))
        self.genareteoutputlayer()
        for i in range(len(self.filelist)):
            if i%100==0:
                print(i)
            self.readcorpus()



    def readcorpus(self):
        dic_subtmp={}
        f=open(self.filelist[self.idx],"r",encoding="utf-8")
        line=f.readline()
        Line=""
        while(line!=""):
            Line+=self.cn(line.replace(",",""))
            line=f.readline()
        for i in jieba.cut(Line, cut_all=False):
            if i not in self.dic_tmp:
                self.dic_tmp.append(i)
                self.genarete(i)
            if i not in dic_subtmp.keys():
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
            vec=np.zeros(self.SIZE)
            vecs.append(vec)
        self.outputlayer=np.array(vecs)



    def save(self,path):
        fo=open(path,"w",encoding="utf-8")
        fo.write("this is a fasttext model created by WNZ"+"\n")
        idx=0
        for i in self.category_name.keys():
            fo.write("$cate"+"#"+str(self.category_name[i])+"#"+i+"#")
            for j in self.outputlayer[self.category_name[i]]:
                fo.write(str(j)+"\t")
            fo.write("\n")

        for i in self.dic.keys():
            fo.write(i+":")
            for j in self.dic[i]:
                fo.write(str(j)+"\t")
            fo.write("\n")
        fo.close()

    def read(self,path):
        fo=open(path,encoding="utf-8")
        line=fo.readline()
        if line.replace("\n","")!="this is a fasttext model created by WNZ":
            print("not a model")
            return 0
        outputlayer = []
        seq=[]
        name=[]
        line = fo.readline()
        while(line!="" and line!="\n"):
            if line.startswith("$"):
                tmpvec=[]
                seq.append(int(line.split("#")[1]))
                name.append(line.split("#")[2])
                print(line.split("#")[3].replace("\n","").split("\t"))
                for i in line.split("#")[3].replace("\n","").split("\t"):
                    if i!="":
                        tmpvec.append(float(i))
                outputlayer.append(tmpvec)
            else:
                tmpvec=[]
                # print(line.split(":")[1].replace("\n",""))
                for i in line.split(":")[1].replace("\n","").split("\t"):
                    if i!="":
                        tmpvec.append(float(i))
                self.dic[line.split(":")[0]]=np.array(tmpvec)
            line = fo.readline()
        self.outputlayer = np.zeros((len(outputlayer), len(outputlayer[0])))
        idx=0
        for i in seq:
            self.category_name[name[idx]]=i
            self.outputlayer[i]=np.array(outputlayer[idx])
            idx+=1


    def predict(self,path):
        self.filelist=[]
        self.category=[]
        consu={}
        right=0
        leng=len(self.category_name)
        for root, dirs, files in os.walk(path):
            for name in files:
                tmp_ca = []
                for k in range(leng):
                    if k == self.category_name[name.split("_")[0]]:
                        tmp_ca.append(1)
                    else:
                        tmp_ca.append(0)
                self.category.append(tmp_ca)
                self.filelist.append(root+"/"+name)
        num=0
        print("预测种类："+str(len(self.category_name)))
        for i in range(len(self.filelist)):
            f = open(self.filelist[i], "r", encoding="utf-8")
            line = f.readline()
            Line = ""
            while (line != ""):
                Line += self.cn(line)
                line = f.readline()
            feature_tmp = 0
            total = 0
            for term in jieba.cut(Line, cut_all=False):
                total += 1
                try:
                    feature_tmp += self.dic[term]
                except:
                    continue
            feature=feature_tmp/total
            out=[]
            for ca_tmp in range(len(self.category_name)):
                out.append(np.dot(feature,self.outputlayer[ca_tmp]))
            if self.category[i].index(max(self.category[i])) not in consu.keys():
                consu[self.category[i].index(max(self.category[i]))]={}
                for qq in range(len(self.category_name)):
                    consu[self.category[i].index(max(self.category[i]))][qq]=0
                if out.index(max(out)) not in consu[self.category[i].index(max(self.category[i]))]:
                    consu[self.category[i].index(max(self.category[i]))][out.index(max(out))]=1
                else:
                    consu[self.category[i].index(max(self.category[i]))][out.index(max(out))] += 1
            else:
                if out.index(max(out)) not in consu[self.category[i].index(max(self.category[i]))]:
                    consu[self.category[i].index(max(self.category[i]))][out.index(max(out))]=1
                else:
                    consu[self.category[i].index(max(self.category[i]))][out.index(max(out))] += 1
            if out.index(max(out))==self.category[i].index(max(self.category[i])):
                right+=1
            else:
                num+=1
                print(out)
                print(self.category[i])
                print("-----------------------")
        print(num)
        print(right)
        trr=""
        for i in self.category_name:
            trr+=i+"\t"
        print(trr)
        consu=draw(consu)
        print(consu)
        for i in consu:
            srr=""
            for j in i:
                srr+=str(j)+"\t"
            print(srr)
        print(right/len(self.filelist))


def draw(consu):
    print(consu)
    out=np.zeros((28,28))
    for i in consu.keys():
        tmp=[]
        total=0
        for j in consu[i]:
            tmp.append(consu[i][j])
        # for j in consu[i]:
        #     tmp.append(consu[i][j]/total)
        out[i]=np.array(tmp)
    return out






# md=model("F:/test",100)
# md=model("F:/test",100)




