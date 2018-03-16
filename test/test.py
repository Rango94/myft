from Filehandler import corpusreader
from Model import model

md=model.model("F:/test",100)
cr=corpusreader.corpusreader(md)
print(md.getVector("毕加索"))
print(cr.readafile(2)[0])
print(cr.readafile(2)[1])