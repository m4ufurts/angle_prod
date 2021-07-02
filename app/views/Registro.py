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

    sum = 0

    quebras =  Quebra.objects.filter(produto=produto.id)
    
    for quebra in quebras:
        material = Material.objects.get(id = quebra.material.id)
        sum += dimensao * (1 + produto.perda) * produto.offset *  material.densidade * quebra.porcentagem * material.custo_kg

    return sum
    
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
        'preco_pago',
    ]

    template_name = "save.html"
    success_url = "/"

    def form_valid(self, form):
        sum = calc(form)

        form.instance.custo_calc = sum
        form.instance.preco_pago = sum
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
    ]
    template_name = "save.html"
    success_url = "/"

    #def form_valid(self, form):
    #    form.instance.brl_kg = 2 * form.instance.density
    #    return super().form_valid(form)

def delete(request, delete_id):
    Registro.objects.get(id=delete_id).delete()
    return redirect('/')



