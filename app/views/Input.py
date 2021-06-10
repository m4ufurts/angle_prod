from django.shortcuts import redirect, render
from django.views import generic
from app.models import Input, Breakdown, RawMaterial

def index(request):
    context =  { 
        'info' : Input.objects.all(), 
        "display_list":Input.display_list,
        'create' : 'ip_create',
        'update' : 'ip_update',
        'delete' : 'ip_delete',
    }

    return render(request, 'list.html', context)

def calc(form) :
    width =  form.instance.width
    length =  form.instance.length
    height =  form.instance.height
    
    dimension = width * length * height

    productiontype = form.instance.productiontype

    sum = 0

    breakdowns =  Breakdown.objects.filter(productionType=productiontype.id)
    print (breakdowns)
    for breakdown in breakdowns:
        rawMaterial = RawMaterial.objects.get(id = breakdown.rawMaterial.id)
        sum += dimension *  breakdown.percent * rawMaterial.density * rawMaterial.brl_kg

    return sum
    
class create(generic.CreateView):
    model = Input
    fields = ['productiontype', 'length', 'width', 'height']
    template_name = "save.html"
    success_url = "/"

    def form_valid(self, form):
        sum = calc(form)

        form.instance.calc_price = sum
        form.instance.price = sum

        return super().form_valid(form)

class update(generic.UpdateView):
    model = Input
    fields = ['productiontype', 'length', 'width', 'height', 'price']
    template_name = "save.html"
    success_url = "/"

    #def form_valid(self, form):
    #    form.instance.brl_kg = 2 * form.instance.density
    #    return super().form_valid(form)

def delete(request, delete_id):
    Input.objects.get(id=delete_id).delete()
    return redirect('/')



