from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView
from app.models import Calibracao, Produto
from django.contrib import auth
from django.core import serializers
from django.db.models.signals import post_save
from django.views.decorators.csrf import csrf_exempt

def index(request):
    context =  { 
        'info' : Calibracao.objects.filter(usuario=request.user), 
        "display_list":Calibracao.display_list,
        'create' : 'calibracao_create',
        'update' : 'calibracao_update',
        'delete' : 'calibracao_delete',
        'tela' : 'Calibração'
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Calibracao
    fields=['produto','materia_prima','processo','produtividade','markup']
    template_name = "save.html"
    success_url = "/calibracao"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Calibracao
    fields=['produto','materia_prima','processo','produtividade','markup']
    template_name = "save.html"
    success_url = "/calibracao"

def delete(request, delete_id):
    Calibracao.objects.get(id=delete_id).delete()
    return redirect('/calibracao')

@csrf_exempt
def salvar(request, pk):
    id = request.POST.get('id')

    obj = Calibracao.objects.filter(id=id)[0]

    obj.materia_prima = request.POST.get('materia_prima')
    obj.processo = request.POST.get('processo')
    obj.produtividade = request.POST.get('produtividade')
    obj.markup = request.POST.get('markup')

    obj.save()

    return JsonResponse( 'ok', safe=False )

def listagem(request):
    calibracoes = Calibracao.objects.filter(usuario=request.user).values('id', 'processo', 'produtividade', 'markup', 'materia_prima', 'produto__tipo')
    return JsonResponse( list(calibracoes), safe=False )

 #cria uma calibração padrão, associada ao produto criado.
def atualizar(sender, instance, created, **kwargs):
    if created:
        calibracao = Calibracao.objects.create(
            materia_prima = 0,
            processo = 0,
            produtividade = 0,
            markup = 0,

            produto = instance,
            usuario = instance.usuario
        )

        calibracao.save()

post_save.connect(atualizar, sender=Produto)