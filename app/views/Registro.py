from typing import Dict
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import generic
from app.models import Processo, Produto, Registro, Quebra, Material,QuebraProc, Calibracao
from django.db.models.signals import pre_save, post_save

def index(request):
    context =  { 
        'info' : Registro.objects.filter(usuario=request.user), 
        "display_list":Registro.display_list,
        'create' : 'ip_create',
        'update' : 'ip_update',
        'delete' : 'ip_delete',
        'tela' : 'Registro'
    }

    return render(request, 'list.html', context)
    
class create(generic.CreateView):
    model = Registro
    fields =  [
        'produto',
        'codigo',
        'descricao',
        'categoria',
        'fornecedor',
        'largura',
        'comprimento',
        'altura',
        'peso',
        #'preco_pago',
        'volume_por_ano',
    ]

    template_name = "save.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Registro
    fields =  [
        'produto',
        'codigo',
        'descricao',
        'categoria',
        'fornecedor',
        'largura',
        'comprimento',
        'altura',
        'peso',
        'preco_pago',
        'volume_por_ano',
    ]
    template_name = "save.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        return super().form_valid(form)

def delete(request, delete_id):
    Registro.objects.get(id=delete_id).delete()
    return redirect('/')

def listagem(request):
    registros = Registro.objects.filter(usuario=request.user).values('descricao', 'ganho_anual', 'angle_anual', 'custo_esperado', 'categoria__nome', 'fornecedor__nome')
    return JsonResponse( list(registros), safe=False )

def resumo(request):
    registros = Registro.objects.filter(usuario=request.user).values('ganho_anual', 'angle_anual')

    resposta = dict()
    resposta["ganho_anual"] = 0
    resposta["angle_anual"] = 0

    for r in registros:
        ganho_anual = r.get('ganho_anual')
        angle_anual = r.get('angle_anual')

        resposta["ganho_anual"] += float(ganho_anual)
        resposta["angle_anual"] += float(angle_anual)

    return JsonResponse( resposta, safe=False )

def calcular(sender, instance, **kwargs) :
    produto = instance.produto
    quebras =  Quebra.objects.filter(produto=produto.id)
    calibracao =  Calibracao.objects.get(produto=produto.id)

    print('calibracao', calibracao)

    #distâncias em milimetros
    largura =  instance.largura
    comprimento =  instance.comprimento
    altura =  instance.altura
    
    #dimensão em metros
    dimensao = largura * comprimento * altura / 1000 * (1 + produto.perda) * produto.offset

    print('volume', dimensao)
    
    #custo associado a matéria-prima
    custo = 0
    peso = 0

    for quebra in quebras:
        material = Material.objects.get(id = quebra.material.id)
        peso_material = dimensao *  material.densidade * quebra.porcentagem 
        
        print('peso_material', peso_material)
        
        peso += peso_material
        custo += (1 + calibracao.materia_prima) * peso_material * material.custo_kg / 1000

    print('peso', peso)
    print('custo', custo)

    quebras_proc =  QuebraProc.objects.filter(produto=produto.id)
    pcs = 0
    mao_obra = 0
    custo_energia = 0
    depreciacao = 0

    for quebra_proc in quebras_proc:
        processo = Processo.objects.get(id = quebra_proc.processo.id)
        pcs_proc = (1 + calibracao.produtividade) * produto.ref_kg * 1000 / peso * produto.OEE #* quebra_proc.alocacao_percentual
        
        print('pcs_proc', pcs_proc)

        pcs += pcs_proc
        mao_obra += (1 + calibracao.processo) * processo.mao_obra / pcs_proc 
        custo_energia += (1 + calibracao.processo) * processo.custo_energia / pcs_proc 
        depreciacao += (1 + calibracao.processo) * processo.depreciacao / pcs_proc 
        
        
    # +1 para quando não houver quebra_proc ??!?
    diff = len(quebras) - len(quebras_proc)
    media = (pcs + diff) / len(quebras)

    custo_proc = mao_obra + custo_energia + depreciacao

    print('custo_proc', custo_proc)

    custo_total = custo + custo_proc

    print('custo_total', custo_total)

    print('produto.markup', produto.markup)
    print('calibracao.markup', calibracao.markup)
    
    markup = custo_total / (1 - produto.markup - calibracao.markup ) - custo_total

    print('markup', markup)
    should_cost = custo_total + markup

    print('should_cost', should_cost)

    angle_anual = should_cost * instance.volume_por_ano

    #custo calculado e should_cost são a mesma coisa?!??
    instance.custo_calc = custo
    instance.preco_pago = custo
    instance.pcs = media
    instance.mao_obra = mao_obra
    instance.custo_proc = custo_proc
    instance.energia = custo_energia
    instance.depreciacao = depreciacao
    instance.custo_esperado = should_cost
    instance.angle_anual = angle_anual
    instance.ganho_anual = angle_anual

#calcula as informações derivadas
pre_save.connect(calcular, sender=Registro)

def atualizar(sender, instance, created, **kwargs):
    if not created:
        registros = []
        if sender == Produto:
            registros = Registro.objects.filter(produto=instance)

        for obj in registros:
            obj.save()

#atualiza o 'Registro' baseado em todos as suas ForeignKey (relevantes)
post_save.connect(atualizar, sender=Produto)
#post_save.connect(atualizar, sender=Processo)
#post_save.connect(atualizar, sender=QuebraProc)