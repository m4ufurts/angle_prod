from .BaseModel import BaseModel, models


class Material( BaseModel ):
    # cadastro do usuario, não obrigatorio, mas para facil ratreamento
    codigo = models.CharField(max_length=255) 
    
    # descricao do material cadastrado
    descricao = models.CharField(max_length=255) 

    # [kg/m3]: densidade do material cadastrado, para Peso_Calc
    densidade = models.FloatField()

    # preco do material cadastrado
    custo_kg = models.FloatField()  

    display_list = ['codigo', 'descricao', 'densidade', 'custo_kg', 'data_registro', 'data_edicao']
    
    def __str__(self):
        return self.descricao