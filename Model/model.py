import os
class model():

    def __init__(self,path,size):
        for root, dirs, files in os.walk(path):
            print(root)
            print(dirs)
            print(files)
md=model("F:\w2vcorpus",100)


