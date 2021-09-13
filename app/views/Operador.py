from django.shortcuts import redirect, render
from django.views import generic
from app.models import Operador

def index(request):
    context =  { 
        'info' : Operador.objects.filter(usuario=request.user), 
        "display_list":Operador.display_list,
        'create' : 'operador_create',
        'update' : 'operador_update',
        'delete' : 'operador_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Operador
    fields = ['descricao', 'custo']
    template_name = "save.html"
    success_url = "/operador"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Operador
    fields = ['descricao', 'custo']
    template_name = "save.html"
    success_url = "/operador"

def delete(request, delete_id):
    Operador.objects.get(id=delete_id).delete()
    return redirect('/operador')



