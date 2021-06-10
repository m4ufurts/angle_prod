from django.db import models

class BaseModel(models.Model):
    display_list = []

    class Meta:
        abstract = True