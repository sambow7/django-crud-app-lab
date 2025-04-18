from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()
    date_planted = models.DateField()
    image_url = models.URLField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class CareLog(models.Model):
    date = models.DateField()
    notes = models.TextField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - {self.plant.name}"