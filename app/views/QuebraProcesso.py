from django.shortcuts import redirect, render
from django.views import generic
from app.models import QuebraProc

def index(request):
    context =  { 
        'info' : QuebraProc.objects.filter(usuario=request.user), 
        "display_list":QuebraProc.display_list,
        'create' : 'quebra_processo_create',
        'update' : 'quebra_processo_update',
        'delete' : 'quebra_processo_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = QuebraProc
    fields = ['produto','processo','alocacao_percentual',]
    template_name = "save.html"
    success_url = "/quebra_processo"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class update(generic.UpdateView):
    model = QuebraProc
    fields = ['produto','processo','alocacao_percentual',]
    template_name = "save.html"
    success_url = "/quebra_processo"

def delete(request, delete_id):
    QuebraProc.objects.get(id=delete_id).delete()
    return redirect('/quebra_processo')



