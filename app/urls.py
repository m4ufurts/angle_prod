from django.contrib import admin
from django.urls import path, include

from .views import Material, Produto, Quebra, Registro, Login

urlpatterns = [
    #Raw Material
    path('rawmaterial/', Material.index, name="rm_index"), 
    path('rawmaterial/create', Material.create.as_view(), name="rm_create"), 
    path('rawmaterial/update/<int:pk>', Material.update.as_view(), name="rm_update"),
    path('rawmaterial/delete/<int:delete_id>', Material.delete, name="rm_delete"), 

    #Production Type
    path('productiontype/', Produto.index, name="pt_index"), 
    path('productiontype/create', Produto.create.as_view(), name="pt_create"), 
    path('productiontype/update/<int:pk>', Produto.update.as_view(), name="pt_update"),
    path('productiontype/delete/<int:delete_id>', Produto.delete, name="pt_delete"), 

    #Breakpoint
    path('breakdown/', Quebra.index, name="bd_index"), 
    path('breakdown/create', Quebra.create.as_view(), name="bd_create"), 
    path('breakdown/update/<int:pk>', Quebra.update.as_view(), name="bd_update"),
    path('breakdown/delete/<int:delete_id>', Quebra.delete, name="bd_delete"), 

    #Registro
    path('', Registro.index, name="ip_index"), 
    path('create', Registro.create.as_view(), name="ip_create"), 
    path('update/<int:pk>', Registro.update.as_view(), name="ip_update"),
    path('delete/<int:delete_id>', Registro.delete, name="ip_delete"), 

    #Login
    path('login', Login.login, name="login"), 
    path('logout', Login.logout, name="logout"), 
]