from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView
from app.models import Calibracao
from django.contrib import auth
from django.core import serializers

def index(request):
    context =  { 
        'info' : Calibracao.objects.filter(usuario=request.user), 
        "display_list":Calibracao.display_list,
        'create' : 'calibracao_create',
        'update' : 'calibracao_update',
        'delete' : 'calibracao_delete',
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


def get(request):
    id = request.GET.get('pk')
    obj = Calibracao.objects.filter(id=id).values('id', 'processo', 'produtividade', 'markup', 'materia_prima' )
    return JsonResponse( list(obj), safe=False )

def listagem(request):
    calibracoes = Calibracao.objects.filter(usuario=request.user).values('id','produto__tipo')
    return JsonResponse( list(calibracoes), safe=False )
