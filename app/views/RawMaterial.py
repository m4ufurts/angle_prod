from django.shortcuts import redirect, render
from django.views import generic
from app.models import RawMaterial

def index(request):
    context =  { 
        'info' : RawMaterial.objects.all(), 
        "display_list":RawMaterial.display_list,
        'create' : 'rm_create',
        'update' : 'rm_update',
        'delete' : 'rm_delete',
    }

    return render(request, 'list.html', context)

class create(generic.CreateView):
    model = RawMaterial
    fields=['name', 'density', 'brl_kg']
    template_name = "save.html"
    success_url = "/rawmaterial"

class update(generic.UpdateView):
    model = RawMaterial
    fields=['name', 'density', 'brl_kg']
    template_name = "save.html"
    success_url = "/rawmaterial"

def delete(request, delete_id):
    RawMaterial.objects.get(id=delete_id).delete()
    return redirect('/rawmaterial')



