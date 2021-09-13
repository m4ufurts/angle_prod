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
    
    # valor referência de produção por tipo_produto
    ref_kg = models.FloatField()

    # valor percentual de ineficiência por tipo_produto
    OEE = models.FloatField()

    # valor percentual para tipo_produto
    markup = models.FloatField()

    display_list =['id','tipo', 'categoria_produto', 'offset', 'perda', 'ref_kg', 'OEE', 'markup', 'data_registro', 'data_edicao']

    def __str__(self):
        return self.tipo