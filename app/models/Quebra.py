from .BaseModel import BaseModel, models
from .Material import Material
from .Produto import Produto


class Quebra( BaseModel):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    porcentagem = models.FloatField()

    display_list = ['produto','material','porcentagem', 'data_registro', 'data_edicao']