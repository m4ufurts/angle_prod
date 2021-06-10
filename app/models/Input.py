from .BaseModel import BaseModel, models
from . import ProductionType

class Input( BaseModel ):
    productiontype = models.ForeignKey(ProductionType, on_delete=models.CASCADE)
    length  = models.FloatField() 
    width  = models.FloatField()
    height  = models.FloatField()
    price = models.FloatField()
    calc_price = models.FloatField()

    display_list =['productiontype', 'length', 'width', 'height', 'price']