from django.shortcuts import redirect, render
from django.views import generic
from app.models import Operador, Processo, Energia, Investimento
from django.db.models.signals import pre_save, post_save

from app.models.Produto import Produto

def index(request):
    context =  { 
        'info' : Processo.objects.filter(usuario=request.user), 
        "display_list":Processo.display_list,
        'create' : 'processo_create',
        'update' : 'processo_update',
        'delete' : 'processo_delete',
        'tela' : 'Processo'
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
        form.instance.usuario = self.request.user
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

def calcular(sender, instance, **kwargs):
    i = instance
    i.mao_obra = i.qnt_operadores * i.operador.custo
    i.depreciacao =  i.investimento.custo
    i.custo_energia =  i.consumo_energia * i.energia.custo

#calcula as informações derivadas
pre_save.connect(calcular, sender=Processo)

def atualizar(sender, instance, created, **kwargs):
    if not created:
        processos = []
        if sender == Operador:
            processos = Processo.objects.filter(operador=instance)
        elif sender == Energia:
            processos = Processo.objects.filter(energia=instance)
        elif sender == Investimento:
            processos = Processo.objects.filter(investimento=instance)
        else:
            processos = Processo.objects.all()

        for obj in processos:
            obj.save()

#atualiza o 'Processo' baseado em todos as suas ForeignKey
post_save.connect(atualizar, sender=Operador)
post_save.connect(atualizar, sender=Energia)
post_save.connect(atualizar, sender=Investimento)