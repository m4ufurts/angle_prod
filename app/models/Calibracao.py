from .BaseModel import BaseModel, models
from .Material import Material
from .Produto import Produto

class Calibracao( BaseModel):
    #busca de tipo_produto cadastrado   
    produto= models.ForeignKey(Produto, on_delete=models.CASCADE)

    #perceuntual +/- que influecia output de SHOULD COST
    mp = models.FloatField()  
    mao_obra = models.FloatField()  
    energia = models.FloatField()  
    depreciacao = models.FloatField()  
    markup = models.FloatField()  

    display_list = ['produto','mp','mao_obra','energia','depreciacao','markup', 'data_registro', 'data_edicao']