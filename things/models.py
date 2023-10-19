from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length = 30, unique = True, blank = False)
    description = models.TextField(max_length = 120, blank = True)
    quantity = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(100)])