import os
class model():
    
    def __init__(self,path,size):
        for root, dirs, files in os.walk(path):
            for name in files:
                print(root+"/"+name)

md=model("F:/w2vcorpus/neteasydataset_602151/corpus_6_4000",100)


