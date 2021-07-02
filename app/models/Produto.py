from .BaseModel import BaseModel, models

class Produto( BaseModel):
    # descrição da tecnologia ou tipo de produto
    tipo = models.CharField(max_length=255)

    #Organização do tipo do mercados/industria
    categoria_produto = models.CharField(max_length=255)

    #atribuição de percentual de ajuste
    offset = models.FloatField()

    # atribuição de percentual de perda/scrap
    perda = models.FloatField()
    
    display_list =['id','tipo', 'categoria_produto', 'offset', 'perda', 'data_registro', 'data_edicao']

    def __str__(self):
        return self.tipo