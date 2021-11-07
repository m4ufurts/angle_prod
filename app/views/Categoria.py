from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib import auth
from app.models import Categoria

def index(request):
    context =  { 
        'info' : Categoria.objects.filter(usuario=request.user), 
        "display_list":Categoria.display_list,
        'create' : 'categoria_create',
        'update' : 'categoria_update',
        'delete' : 'categoria_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Categoria
    fields=['nome']
    template_name = "save.html"
    success_url = "/categoria"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Categoria
    fields=['nome']
    template_name = "save.html"
    success_url = "/categoria"

def delete(request, delete_id):
    Categoria.objects.get(id=delete_id).delete()
    return redirect('/categoria')



