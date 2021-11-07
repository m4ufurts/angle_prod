from .BaseModel import BaseModel, models

class Fornecedor( BaseModel):
    nome = models.CharField(max_length=255)

    display_list = ['id', 'nome', 'data_registro', 'data_edicao']

    def __str__(self):
        return self.nome