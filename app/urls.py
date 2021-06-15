from django.contrib import admin
from django.urls import path, include

from .views import RawMaterial, ProductionType, Breakdown, Input, Login

urlpatterns = [
    #Raw Material
    path('rawmaterial/', RawMaterial.index, name="rm_index"), 
    path('rawmaterial/create', RawMaterial.create.as_view(), name="rm_create"), 
    path('rawmaterial/update/<int:pk>', RawMaterial.update.as_view(), name="rm_update"),
    path('rawmaterial/delete/<int:delete_id>', RawMaterial.delete, name="rm_delete"), 

    #Production Type
    path('productiontype/', ProductionType.index, name="pt_index"), 
    path('productiontype/create', ProductionType.create.as_view(), name="pt_create"), 
    path('productiontype/update/<int:pk>', ProductionType.update.as_view(), name="pt_update"),
    path('productiontype/delete/<int:delete_id>', ProductionType.delete, name="pt_delete"), 

    #Breakpoint
    path('breakdown/', Breakdown.index, name="bd_index"), 
    path('breakdown/create', Breakdown.create.as_view(), name="bd_create"), 
    path('breakdown/update/<int:pk>', Breakdown.update.as_view(), name="bd_update"),
    path('breakdown/delete/<int:delete_id>', Breakdown.delete, name="bd_delete"), 

    #Input
    path('', Input.index, name="ip_index"), 
    path('create', Input.create.as_view(), name="ip_create"), 
    path('update/<int:pk>', Input.update.as_view(), name="ip_update"),
    path('delete/<int:delete_id>', Input.delete, name="ip_delete"), 

    #Login
    path('login', Login.login, name="login"), 
    path('logout', Login.logout, name="logout"), 
]