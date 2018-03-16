from Filehandler import corpusreader
from Model import model
from trainer import trainer

md=model.model("F:/test",100)
tr=trainer.trainer(md,0.001)
tr.train()

