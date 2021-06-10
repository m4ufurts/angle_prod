from django.shortcuts import redirect, render
from django.views import generic
from app.models import ProductionType

def index(request):
    context =  { 
        'info' : ProductionType.objects.all(), 
        "display_list":ProductionType.display_list,
        'create' : 'pt_create',
        'update' : 'pt_update',
        'delete' : 'pt_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = ProductionType
    fields=['name', 'offset', 'scrap']
    template_name = "save.html"
    success_url = "/productiontype"

    #def form_valid(self, form):
    #    form.instance.brl_kg = 2 * form.instance.density
    #    return super().form_valid(form)

class update(generic.UpdateView):
    model = ProductionType
    fields=['name', 'offset', 'scrap']
    template_name = "save.html"
    success_url = "/productiontype"

    #def form_valid(self, form):
    #    form.instance.brl_kg = 2 * form.instance.density
    #    return super().form_valid(form)

def delete(request, delete_id):
    ProductionType.objects.get(id=delete_id).delete()
    return redirect('/productiontype')



