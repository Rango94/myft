from Filehandler import corpusreader
from Model import model
from trainer import trainer

# md=model.model()
# md.buildemodel("E:/text8/neteasy",100)
# tr=trainer.trainer(md,0.025)
# md=tr.train()
# md.save("E:/text8/model.model")
md1=model.model()
md1.read("E:/text8/model.model")
md1.predict("E:/text8/test")

