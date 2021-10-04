from django.shortcuts import redirect, render
from django.views import generic
from app.models import Processo, Produto, Registro, Quebra, Material,QuebraProc

def index(request):
    context =  { 
        'info' : Registro.objects.filter(usuario=request.user), 
        "display_list":Registro.display_list,
        'create' : 'ip_create',
        'update' : 'ip_update',
        'delete' : 'ip_delete',
    }

    return render(request, 'list.html', context)

def calc(form) :
    #distâncias em milimetros
    largura =  form.instance.largura / 1000
    comprimento =  form.instance.comprimento / 1000
    altura =  form.instance.altura / 1000
    
    #dimensão em metros
    dimensao = largura * comprimento * altura

    produto = form.instance.produto
    quebras =  Quebra.objects.filter(produto=produto.id)

    #custo associado a matéria-prima
    custo = 0
    peso = 0

    for quebra in quebras:
        material = Material.objects.get(id = quebra.material.id)
        peso_material = dimensao * (1 + produto.perda) * produto.offset *  material.densidade * quebra.porcentagem 
        peso += peso_material
        custo += peso_material * material.custo_kg

    quebras_proc =  QuebraProc.objects.filter(produto=produto.id)
    pcs = 0
    mao_obra = 0
    custo_energia = 0
    depreciacao = 0

    for quebra_proc in quebras_proc:
        processo = Processo.objects.get(id = quebra_proc.processo.id)
        pcs_proc = produto.ref_kg / peso * produto.OEE * quebra_proc.alocacao_percentual
        pcs += pcs_proc
        mao_obra += processo.mao_obra / pcs_proc 
        custo_energia += processo.custo_energia / pcs_proc 
        depreciacao += processo.depreciacao / pcs_proc 
        
        
    # +1 para quando não houver quebra_proc ??!?
    diff = len(quebras) - len(quebras_proc)
    media = (pcs + diff) / len(quebras)

    custo_proc = mao_obra + custo_energia + depreciacao
    
    #pegar dinamicamente
    markup = 0.12

    # sem parentese ???
    should_cost = ( custo + custo_proc ) / 1 - markup

    angle_anual = should_cost * form.instance.volume_por_ano

    return {
        'custo': custo, 
        'pcs': media, 
        'mao_obra': mao_obra, 
        'custo_energia': custo_energia, 
        'depreciacao': depreciacao,
        'custo_proc' : custo_proc,
        'should_cost' : should_cost,
        'angle_anual': angle_anual
    }
    
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
        #'preco_pago',
        'volume_por_ano',
    ]

    template_name = "save.html"
    success_url = "/"

    def form_valid(self, form):
        r = calc(form)
        print(r)

        i = form.instance 

        #custo calculado e should_cost são a mesma coisa?!??
        i.custo_calc = r["custo"]
        i.preco_pago = r["custo"]
        i.pcs = r["pcs"]
        i.mao_obra = r["mao_obra"]
        i.custo_proc = r["custo_proc"]
        i.energia = r["custo_energia"]
        i.depreciacao = r["depreciacao"]
        i.custo_esperado = r["should_cost"]
        i.angle_anual = r["angle_anual"]
        i.ganho_anual = r["angle_anual"]

        i.usuario = self.request.user

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
        'preco_pago',
        'volume_por_ano',
    ]
    template_name = "save.html"
    success_url = "/"

def delete(request, delete_id):
    Registro.objects.get(id=delete_id).delete()
    return redirect('/')



