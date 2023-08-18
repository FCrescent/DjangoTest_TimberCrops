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
    category = models.ForeignKey(NeedCat, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class ResourceCat(models.Model):
    name = models.CharField(max_length=255)  # Adjust the max_length as needed

    def __str__(self):
        return self.name