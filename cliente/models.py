from django.db import models

# Create your models here.

class Cliente (models.Model):
    name=models.CharField(max_length=50)

    def __str__ (self):
        return '{}'.format(self.name)
