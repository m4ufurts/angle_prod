from django.shortcuts import redirect, render
from django.views import generic
from app.models import Produto

def index(request):
    context =  { 
        'info' : Produto.objects.filter(usuario=request.user), 
        "display_list":Produto.display_list,
        'create' : 'pt_create',
        'update' : 'pt_update',
        'delete' : 'pt_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Produto
    fields=['tipo', 'categoria_produto', 'offset', 'perda']
    template_name = "save.html"
    success_url = "/productiontype"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = Produto
    fields=['tipo', 'categoria_produto', 'offset', 'perda']
    template_name = "save.html"
    success_url = "/productiontype"

def delete(request, delete_id):
    Produto.objects.get(id=delete_id).delete()
    return redirect('/productiontype')



