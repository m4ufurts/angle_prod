from .BaseModel import BaseModel, models
from .RawMaterial import RawMaterial
from .ProductionType import ProductionType


class Breakdown( BaseModel):
    rawMaterial = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    productionType = models.ForeignKey(ProductionType, on_delete=models.CASCADE)
    percent = models.FloatField()

    display_list = ['productionType','rawMaterial','percent']