from Filehandler import corpusreader
from Model import model
import os
import shutil
filelist=[]
namelist=[]
for root, dirs, files in os.walk("D:/迅雷下载/网易新闻语料dataset_602151/corpus_6_4000"):
    for name in files:
        namelist.append(name)
        filelist.append(root + "/" + name)


for i in range(len(filelist)):
    if i%100==0:
        shutil.copyfile(filelist[i], "E:/text8/test/"+namelist[i])
    elif i % 10 == 0:
        shutil.copyfile(filelist[i], "E:/text8/neteasy/"+namelist[i])