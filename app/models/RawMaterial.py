from .BaseModel import BaseModel, models


class RawMaterial( BaseModel ):
    name = models.CharField(max_length=255) 
    density = models.FloatField()
    brl_kg = models.FloatField()  

    display_list = ['name', 'density', 'brl_kg']
    
    def __str__(self):
        return self.name