from django.db import models

# Create your models here.

class GameMode(models.Model):
    name = models.CharField(max_length=100, unique=True)
    food_consumption_percentage = models.PositiveIntegerField()
    food_consumption_daily_unit = models.DecimalField(max_digits=5, decimal_places=2)
    locked = models.BooleanField(default=False)  

    def __str__(self):
        return self.name

class NeedCat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Need(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(NeedCat, on_delete=models.PROTECT, related_name='needs')

    def __str__(self):
        return self.name
    
class ResourceCat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Resource(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ResourceCat, on_delete=models.PROTECT, related_name='resources')

    def __str__(self):
        return self.name
    
class NatStructCat(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class NatStruct(models.Model):
    name = models.CharField(max_length=100)
    days_to_grow = models.PositiveIntegerField()
    days_between_harvest = models.PositiveIntegerField()
    resource_cut_yield = models.PositiveIntegerField()
    resource_harvest_yield = models.PositiveIntegerField()
    category = models.ForeignKey(NatStructCat, on_delete=models.PROTECT, related_name='nat_structs')
    resource_cut = models.ForeignKey(Resource, on_delete=models.PROTECT, related_name='cut_nat_structs')
    resource_harvest = models.ForeignKey(Resource, on_delete=models.PROTECT, related_name='harvest_nat_structs')

    def __str__(self):
        return self.name
    
