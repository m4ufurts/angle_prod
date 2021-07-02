from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    display_list = []

    #registro automatico ao registrar um item
    data_registro = models.DateTimeField(auto_now_add=True)

    #registro automatico ao editar um item
    data_edicao = models.DateTimeField(auto_now=True)

    #registro automatico do usuario responsavel pelo id_godroid
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True