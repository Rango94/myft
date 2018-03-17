
class corpusreader():
    dic_list=[]
    dic={}
    category=[]
    def __init__(self,md):
        self.dic_list=md.dic_list
        self.dic=md.dic
        self.category=md.category

    def readafile(self,idx):
        feature=0
        total=0
        for i in self.dic_list[idx].keys():
            total+=self.dic_list[idx][i]
            feature+=self.dic[i]*self.dic_list[idx][i]
        if total==0:
            return 0
        return feature/total







