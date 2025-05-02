from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    ingredients = models.CharField()
    price = models.IntegerField()
    time_taken = models.IntegerField()

    def __str__(self):
        return self.name
    
class Table(models.Model):
    num = models.IntegerField()
    capacity = models.IntegerField()
    position = models.CharField()
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return f"Table Num: {self.num}. CAPACITY: {self.capacity}"

class Booking(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    table_for = models.IntegerField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.table.isAvailable = False
        self.table.save()