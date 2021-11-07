from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView
from app.models import Fornecedor
from django.contrib import auth

def index(request):
    context =  { 
        'info' : Fornecedor.objects.filter(usuario=request.user), 
        "display_list":Fornecedor.display_list,
        'create' : 'fornecedor_create',
        'update' : 'fornecedor_update',
        'delete' : 'fornecedor_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Fornecedor
    fields=['nome']
    template_name = "save.html"
    success_url = "/fornecedor"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Fornecedor
    fields=['nome']
    template_name = "save.html"
    success_url = "/fornecedor"

def delete(request, delete_id):
    Fornecedor.objects.get(id=delete_id).delete()
    return redirect('/fornecedor')



