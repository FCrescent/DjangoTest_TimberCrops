from django.db import models

# Create your models here.

class GameMode(models.Model):
    # DIFFICULTY_CHOICES = (
    #     ('easy', 'Easy'),
    #     ('normal', 'Normal'),
    #     ('hard', 'Hard'),
    #     ('custom', 'Custom'),
    # )

    # name = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    name = models.CharField(max_length=100, unique=True)
    food_consumption_percentage = models.PositiveIntegerField()
    food_consumption_daily_unit = models.DecimalField(max_digits=5, decimal_places=2)
    locked = models.BooleanField(default=False)  

    def __str__(self):
        return self.name
