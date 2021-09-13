from app.models import Processo
from .BaseModel import BaseModel, models
from .Produto import Produto

# Construção e alocação de tipo processo (semelhante ou feito para Material). 
# Nesta etapa construi-se todos a sequência de todos os processos relacionado a aquele tipo de produto.
class QuebraProc( BaseModel):
    #busca de tipo_produto cadastrado
    produto= models.ForeignKey(Produto, on_delete=models.CASCADE)

    # busca de tipo_material cadastrado
    processo = models.ForeignKey(Processo, on_delete=models.CASCADE)

    #alocacao percentual
    alocacao_percentual = models.FloatField()

    display_list = ['produto','processo','alocacao_percentual', 'data_registro', 'data_edicao']