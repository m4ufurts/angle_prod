from django.shortcuts import redirect, render
from django.views import generic
from app.models import Processo

def index(request):
    context =  { 
        'info' : Processo.objects.filter(usuario=request.user), 
        "display_list":Processo.display_list,
        'create' : 'processo_create',
        'update' : 'processo_update',
        'delete' : 'processo_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Processo
    fields = [
        'codigo',
        'descricao',
        'operador',
        'qnt_operadores', 
        'energia', 
        'consumo_energia', 
        'investimento'
    ]
    template_name = "save.html"
    success_url = "/processo"

    def form_valid(self, form):
        i = form.instance
        i.usuario = self.request.user
        i.mao_obra =  i.qnt_operadores * i.operador.custo
        i.depreciacao =  i.investimento.custo
        i.custo_energia =  i.consumo_energia * i.energia.custo 

        return super().form_valid(form)

class update(generic.UpdateView):
    model = Processo
    fields = [
        'codigo',
        'descricao',
        'operador',
        'qnt_operadores', 
        'mao_obra', 
        'energia', 
        'consumo_energia', 
        'investimento', 
        'depreciacao', 
    ]
    template_name = "save.html"
    success_url = "/processo"

def delete(request, delete_id):
    Processo.objects.get(id=delete_id).delete()
    return redirect('/processo')



