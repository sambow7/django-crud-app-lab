from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()
    date_planted = models.DateField()

class CareLog(models.Model):
    date = models.DateField()
    notes = models.TextField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.plant.name}"