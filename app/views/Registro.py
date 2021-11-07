from django.shortcuts import redirect, render
from django.views import generic
from app.models import Processo, Produto, Registro, Quebra, Material,QuebraProc, Calibracao

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
    produto = form.instance.produto
    quebras =  Quebra.objects.filter(produto=produto.id)
    calibracao =  Calibracao.objects.get(produto=produto.id)

    print('calibracao', calibracao)

    #distâncias em milimetros
    largura =  form.instance.largura
    comprimento =  form.instance.comprimento
    altura =  form.instance.altura
    
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

def delete(request, delete_id):
    Registro.objects.get(id=delete_id).delete()
    return redirect('/')



