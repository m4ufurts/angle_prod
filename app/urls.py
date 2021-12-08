from app.views import Dashboard
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required 
from django.contrib.admin.views.decorators import staff_member_required

from .views import Material, Produto, Quebra, Registro, Login
from .views import Energia, Investimento, Operador, Processo, QuebraProcesso
from .views import Dashboard, Calibracao, Categoria, Fornecedor

urlpatterns = [
    #Registro
    path('', login_required(Registro.index), name="ip_index"), 
    path('create', Registro.create.as_view(), name="ip_create"), 
    path('update/<int:pk>', Registro.update.as_view(), name="ip_update"),
    path('delete/<int:delete_id>', Registro.delete, name="ip_delete"), 

    #Material
    path('rawmaterial/', staff_member_required(Material.index) , name="rm_index"), 
    path('rawmaterial/create', Material.create.as_view(), name="rm_create"), 
    path('rawmaterial/update/<int:pk>', Material.update.as_view(), name="rm_update"),
    path('rawmaterial/delete/<int:delete_id>', Material.delete, name="rm_delete"), 

    #Breakpoint
    path('breakdown/', staff_member_required(Quebra.index), name="bd_index"), 
    path('breakdown/create', Quebra.create.as_view(), name="bd_create"), 
    path('breakdown/update/<int:pk>', Quebra.update.as_view(), name="bd_update"),
    path('breakdown/delete/<int:delete_id>', Quebra.delete, name="bd_delete"), 
    
    #Production Type
    path('productiontype/', staff_member_required(Produto.index), name="pt_index"), 
    path('productiontype/create', Produto.create.as_view(), name="pt_create"), 
    path('productiontype/update/<int:pk>', Produto.update.as_view(), name="pt_update"),
    path('productiontype/delete/<int:delete_id>', Produto.delete, name="pt_delete"), 

    #Energia
    path('energia/', staff_member_required(Energia.index), name="energia_index"), 
    path('energia/create', Energia.create.as_view(), name="energia_create"), 
    path('energia/update/<int:pk>', Energia.update.as_view(), name="energia_update"),
    path('energia/delete/<int:delete_id>', Energia.delete, name="energia_delete"), 

    #Investimento
    path('investimento/', staff_member_required(Investimento.index), name="investimento_index"), 
    path('investimento/create', Investimento.create.as_view(), name="investimento_create"), 
    path('investimento/update/<int:pk>', Investimento.update.as_view(), name="investimento_update"),
    path('investimento/delete/<int:delete_id>', Investimento.delete, name="investimento_delete"), 

    #Operador
    path('operador/', staff_member_required(Operador.index), name="operador_index"), 
    path('operador/create', Operador.create.as_view(), name="operador_create"), 
    path('operador/update/<int:pk>', Operador.update.as_view(), name="operador_update"),
    path('operador/delete/<int:delete_id>', Operador.delete, name="operador_delete"), 

    #Processo
    path('processo/', staff_member_required(Processo.index), name="processo_index"), 
    path('processo/create', Processo.create.as_view(), name="processo_create"), 
    path('processo/update/<int:pk>', Processo.update.as_view(), name="processo_update"),
    path('processo/delete/<int:delete_id>', Processo.delete, name="processo_delete"), 

    #Quebra Processo
    path('quebra_processo/', staff_member_required(QuebraProcesso.index), name="quebra_processo_index"), 
    path('quebra_processo/create', QuebraProcesso.create.as_view(), name="quebra_processo_create"), 
    path('quebra_processo/update/<int:pk>', QuebraProcesso.update.as_view(), name="quebra_processo_update"),
    path('quebra_processo/delete/<int:delete_id>', QuebraProcesso.delete, name="quebra_processo_delete"), 

    #Calibracao
    path('calibracao/', login_required(Calibracao.index), name="calibracao_index"), 
    path('calibracao/create', Calibracao.create.as_view(), name="calibracao_create"), 
    path('calibracao/update/<int:pk>', Calibracao.update.as_view(), name="calibracao_update"),
    path('calibracao/delete/<int:delete_id>', Calibracao.delete, name="calibracao_delete"), 

    #Categoria
    path('categoria/', staff_member_required(Categoria.index), name="categoria_index"), 
    path('categoria/create', Categoria.create.as_view(), name="categoria_create"), 
    path('categoria/update/<int:pk>', Categoria.update.as_view(), name="categoria_update"),
    path('categoria/delete/<int:delete_id>', Categoria.delete, name="categoria_delete"), 

    #Fornecedor
    path('fornecedor/', staff_member_required(Fornecedor.index), name="fornecedor_index"), 
    path('fornecedor/create', Fornecedor.create.as_view(), name="fornecedor_create"), 
    path('fornecedor/update/<int:pk>', Fornecedor.update.as_view(), name="fornecedor_update"),
    path('fornecedor/delete/<int:delete_id>', Fornecedor.delete, name="fornecedor_delete"), 

    #Login
    path('login', Login.login, name="login"), 
    path('logout', Login.logout, name="logout"), 

    #Dashboard
    path('dashboard',login_required(Dashboard.index), name="dashboard_index"), 
    path('dashboard/calibracao', login_required(Calibracao.listagem)), 
    path('dashboard/calibracao/<int:pk>', login_required(Calibracao.salvar)), 
    path('dashboard/registro', login_required(Registro.listagem)),
    path('dashboard/registro_resumo', login_required(Registro.resumo)), 
]