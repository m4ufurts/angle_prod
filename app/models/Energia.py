from .BaseModel import BaseModel, models

# Cadastro de dados referente às possibilidades de Tipo_Energia
class Energia( BaseModel):
    descricao = models.CharField(max_length=255)
    
    #valor de custo por hora
    custo = models.FloatField()

    display_list =['id','descricao', 'custo', 'data_registro', 'data_edicao']

    def __str__(self):
        return self.descricao