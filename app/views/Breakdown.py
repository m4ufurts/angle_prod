from django.shortcuts import redirect, render
from django.views import generic
from app.models import Breakdown

def index(request):
    context =  { 
        'info' : Breakdown.objects.all(), 
        "display_list":Breakdown.display_list,
        'create' : 'bd_create',
        'update' : 'bd_update',
        'delete' : 'bd_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = Breakdown
    fields = ['productionType','rawMaterial','percent']
    template_name = "save.html"
    success_url = "/breakdown"

    #def form_valid(self, form):
    #    form.instance.brl_kg = 2 * form.instance.density
    #    return super().form_valid(form)

class update(generic.UpdateView):
    model = Breakdown
    fields = ['productionType','rawMaterial','percent']
    template_name = "save.html"
    success_url = "/breakdown"

    #def form_valid(self, form):
    #    form.instance.brl_kg = 2 * form.instance.density
    #    return super().form_valid(form)

def delete(request, delete_id):
    Breakdown.objects.get(id=delete_id).delete()
    return redirect('/breakdown')



