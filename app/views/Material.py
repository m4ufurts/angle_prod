from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic.edit import CreateView
from app.models import Material
from django.contrib import auth

def index(request):
    context =  { 
        'info' : Material.objects.filter(usuario=request.user), 
        "display_list":Material.display_list,
        'create' : 'rm_create',
        'update' : 'rm_update',
        'delete' : 'rm_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Material
    fields=['codigo', 'descricao', 'densidade', 'custo_kg']
    template_name = "save.html"
    success_url = "/rawmaterial"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Material
    fields=['codigo', 'descricao', 'densidade', 'custo_kg']
    template_name = "save.html"
    success_url = "/rawmaterial"

def delete(request, delete_id):
    Material.objects.get(id=delete_id).delete()
    return redirect('/rawmaterial')



