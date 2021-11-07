from .BaseModel import BaseModel, models
from .Material import Material
from .Produto import Produto

class Calibracao( BaseModel):
    #busca de tipo_produto cadastrado   
    produto= models.ForeignKey(Produto, on_delete=models.CASCADE)

    #perceuntual +/- que influecia output de SHOULD COST

    materia_prima = models.FloatField()  
    processo = models.FloatField()  
    produtividade = models.FloatField()  
    markup = models.FloatField()  

    display_list = ['produto','materia_prima','processo','produtividade','markup', 'data_registro', 'data_edicao']