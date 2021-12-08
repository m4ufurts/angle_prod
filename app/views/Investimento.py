from django.shortcuts import redirect, render
from django.views import generic
from app.models import Investimento

def index(request):
    context =  { 
        'info' : Investimento.objects.filter(usuario=request.user), 
        "display_list":Investimento.display_list,
        'create' : 'investimento_create',
        'update' : 'investimento_update',
        'delete' : 'investimento_delete',
        'tela' : 'Investimento'
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Investimento
    fields = ['descricao', 'custo']
    template_name = "save.html"
    success_url = "/investimento"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Investimento
    fields = ['descricao', 'custo']
    template_name = "save.html"
    success_url = "/investimento"

def delete(request, delete_id):
    Investimento.objects.get(id=delete_id).delete()
    return redirect('/investimento')



