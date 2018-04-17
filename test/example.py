import sys
sys.path.append("..")
from Filehandler import corpusreader
from Model import model
from trainer import trainer

md=model.model()
md.buildemodel("D:\simplespider/train",300)
tr=trainer.trainer(md,0.025)
md=tr.train()
md.save("D:/MYPJ/model.model")
md1=model.model()
md1.read("D:/MYPJ/model.model")
md1.predict("D:\simplespider/test")
