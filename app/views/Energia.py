from django.shortcuts import redirect, render
from django.views import generic
from app.models import Energia

def index(request):
    context =  { 
        'info' : Energia.objects.filter(usuario=request.user), 
        "display_list":Energia.display_list,
        'create' : 'energia_create',
        'update' : 'energia_update',
        'delete' : 'energia_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Energia
    fields = ['descricao', 'custo']
    template_name = "save.html"
    success_url = "/energia"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Energia
    fields = ['descricao', 'custo',]
    template_name = "save.html"
    success_url = "/energia"

def delete(request, delete_id):
    Energia.objects.get(id=delete_id).delete()
    return redirect('/energia')



