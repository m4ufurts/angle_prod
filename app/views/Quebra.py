from django.shortcuts import redirect, render
from django.views import generic
from app.models import Quebra

def index(request):
    context =  { 
        'info' : Quebra.objects.filter(usuario=request.user), 
        "display_list":Quebra.display_list,
        'create' : 'bd_create',
        'update' : 'bd_update',
        'delete' : 'bd_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Quebra
    fields = ['produto','material','porcentagem']
    template_name = "save.html"
    success_url = "/breakdown"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Quebra
    fields = ['produto','material','porcentagem']
    template_name = "save.html"
    success_url = "/breakdown"

def delete(request, delete_id):
    Quebra.objects.get(id=delete_id).delete()
    return redirect('/breakdown')



