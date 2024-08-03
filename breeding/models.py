from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    
    
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name
