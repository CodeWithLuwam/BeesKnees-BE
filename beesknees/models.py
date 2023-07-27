from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='files/muscleimage', default='image of muscle')
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + self.description
    