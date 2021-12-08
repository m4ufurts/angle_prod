from django.db.models.fields import DateTimeField

from .BaseModel import BaseModel, models
from . import Produto, Categoria, Fornecedor

class Registro( BaseModel ):
    # codigo sequencial, gerado a cada cadastro (KEY_CODE)
    id = models.BigAutoField(primary_key=True) #id_godroid

    # é a tecnologia de produção para determinado produto
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    # é o codigo do cliente para rastreamento do produto
    codigo = models.CharField(max_length=255)

    # é a descrição do produto, conhecido pelo cliente
    descricao = models.CharField(max_length=255)

    # como o cliente classifica cada produto internamente (organização)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    # é de quem o cliente compra o produto
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    largura  = models.FloatField() 
    comprimento  = models.FloatField()
    altura  = models.FloatField()

    #peso real objeto
    peso = models.FloatField(default=0)

    # é o preço pago pelo cliente
    preco_pago = models.FloatField()

    # é o custo de material calculado a partir do peso bruto
    custo_calc = models.FloatField()

    # v2
    volume_por_ano = models.FloatField(default=10000)

    pcs = models.FloatField()
    mao_obra = models.FloatField()
    energia = models.FloatField()
    depreciacao = models.FloatField()

    custo_proc = models.FloatField()
    custo_esperado = models.FloatField() #should_cost

    ganho_anual = models.FloatField()
    angle_anual = models.FloatField()

    display_list = [
        'id',
        'produto',
        'codigo',
        'descricao',
        #'categoria',
        #'fornecedor',
        #'largura',
        #'comprimento',
        #'altura',
        'preco_pago',
        'volume_por_ano',
         'pcs',
        'mao_obra',
        'energia',
        'depreciacao',
        'custo_proc',
        'custo_esperado', #should_cost
        'ganho_anual',
        'angle_anual',
        'data_registro',
        'data_edicao'
    ]