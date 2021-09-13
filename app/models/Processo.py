from .Operador import Operador
from .Energia import Energia
from .Investimento import Investimento
from .BaseModel import BaseModel, models

# Cadastro dos tipos de processo 
# e premissas para calculo de custo de MO (Mao-de-Obra), ENER (Energia), DEPR (Depreciação).
class Processo( BaseModel):
    # código rastreável por procesoo
    codigo = models.CharField(max_length=255)

    # decrição do processo 
    descricao = models.CharField(max_length=255)

    # tipo de operador
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)

    # quantidade de operadores necessários para o processo
    qnt_operadores = models.FloatField()
   
    #calculo de custo por hora de todos os operadores diretos e indiretos
    mao_obra = models.FloatField()
    
    # tipo de energia utilizada no processo
    energia = models.ForeignKey(Energia, on_delete=models.CASCADE)

    # consumo/gasto de energia por hora
    consumo_energia = models.FloatField()

    # valor gasto com energia, baseado no valor da energia e o consumo por hora
    custo_energia = models.FloatField()

    # tipo de invesitmento relacionado ao processo
    investimento = models.ForeignKey(Investimento, on_delete=models.CASCADE)
    
    #cálculo de custo por hora de depreciação
    depreciacao = models.FloatField()
    
    display_list =[
        'id',
        'codigo',
        'descricao',
        'operador',
        'qnt_operadores', 
        'mao_obra', 
        'energia', 
        'consumo_energia', 
        'custo_energia',
        'investimento', 
        'depreciacao', 

        #'data_registro', 
        #'data_edicao'
    ]

    def __str__(self):
        return self.descricao