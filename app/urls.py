from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

from .views import Material, Produto, Quebra, Registro, Login
from .views import Energia, Investimento, Operador, Processo, QuebraProcesso

urlpatterns = [
    #Registro
    path('', login_required(Registro.index), name="ip_index"), 
    path('create', Registro.create.as_view(), name="ip_create"), 
    path('update/<int:pk>', Registro.update.as_view(), name="ip_update"),
    path('delete/<int:delete_id>', Registro.delete, name="ip_delete"), 

    #Material
    path('rawmaterial/', login_required(Material.index) , name="rm_index"), 
    path('rawmaterial/create', Material.create.as_view(), name="rm_create"), 
    path('rawmaterial/update/<int:pk>', Material.update.as_view(), name="rm_update"),
    path('rawmaterial/delete/<int:delete_id>', Material.delete, name="rm_delete"), 

    #Breakpoint
    path('breakdown/', login_required(Quebra.index), name="bd_index"), 
    path('breakdown/create', Quebra.create.as_view(), name="bd_create"), 
    path('breakdown/update/<int:pk>', Quebra.update.as_view(), name="bd_update"),
    path('breakdown/delete/<int:delete_id>', Quebra.delete, name="bd_delete"), 
    
    #Production Type
    path('productiontype/', login_required(Produto.index), name="pt_index"), 
    path('productiontype/create', Produto.create.as_view(), name="pt_create"), 
    path('productiontype/update/<int:pk>', Produto.update.as_view(), name="pt_update"),
    path('productiontype/delete/<int:delete_id>', Produto.delete, name="pt_delete"), 

    #v2
    #Energia
    path('energia/', login_required(Energia.index), name="energia_index"), 
    path('energia/create', Energia.create.as_view(), name="energia_create"), 
    path('energia/update/<int:pk>', Energia.update.as_view(), name="energia_update"),
    path('energia/delete/<int:delete_id>', Energia.delete, name="energia_delete"), 

    #Investimento
    path('investimento/', login_required(Investimento.index), name="investimento_index"), 
    path('investimento/create', Investimento.create.as_view(), name="investimento_create"), 
    path('investimento/update/<int:pk>', Investimento.update.as_view(), name="investimento_update"),
    path('investimento/delete/<int:delete_id>', Investimento.delete, name="investimento_delete"), 

    #Operador
    path('operador/', login_required(Operador.index), name="operador_index"), 
    path('operador/create', Operador.create.as_view(), name="operador_create"), 
    path('operador/update/<int:pk>', Operador.update.as_view(), name="operador_update"),
    path('operador/delete/<int:delete_id>', Operador.delete, name="operador_delete"), 

    #Processo
    path('processo/', login_required(Processo.index), name="processo_index"), 
    path('processo/create', Processo.create.as_view(), name="processo_create"), 
    path('processo/update/<int:pk>', Processo.update.as_view(), name="processo_update"),
    path('processo/delete/<int:delete_id>', Processo.delete, name="processo_delete"), 

    #Quebra Processo
    path('quebra_processo/', login_required(QuebraProcesso.index), name="quebra_processo_index"), 
    path('quebra_processo/create', QuebraProcesso.create.as_view(), name="quebra_processo_create"), 
    path('quebra_processo/update/<int:pk>', QuebraProcesso.update.as_view(), name="quebra_processo_update"),
    path('quebra_processo/delete/<int:delete_id>', QuebraProcesso.delete, name="quebra_processo_delete"), 

    #Login
    path('login', Login.login, name="login"), 
    path('logout', Login.logout, name="logout"), 
]