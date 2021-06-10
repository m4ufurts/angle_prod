from .BaseModel import BaseModel, models

class ProductionType( BaseModel):
    name = models.CharField(max_length=255) 
    offset = models.FloatField()
    scrap = models.FloatField()
    display_list =['name', 'offset', 'scrap']

    def __str__(self):
        return self.name