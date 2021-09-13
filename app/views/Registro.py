from django.shortcuts import redirect, render
from django.views import generic
from app.models import Produto, Registro, Quebra, Material

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
    largura =  form.instance.largura
    comprimento =  form.instance.comprimento
    altura =  form.instance.altura
    
    dimensao = largura * comprimento * altura / 1000000

    produto = form.instance.produto
    quebras =  Quebra.objects.filter(produto=produto.id)

    sum = 0
    pcs = 0
    
    for quebra in quebras:
        material = Material.objects.get(id = quebra.material.id)
        peso = dimensao * (1 + produto.perda) * produto.offset *  material.densidade * quebra.porcentagem
        sum += peso * material.custo_kg
        pcs += produto.ref_kg / peso * produto.OEE

    return {'sum': sum, 'pcs': pcs}
    
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

        form.instance.custo_calc = r["sum"]
        form.instance.preco_pago = r["sum"]
        form.instance.pcs = r["pcs"]
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
        'preco_pago',
        'volume_por_ano',
    ]
    template_name = "save.html"
    success_url = "/"

def delete(request, delete_id):
    Registro.objects.get(id=delete_id).delete()
    return redirect('/')



