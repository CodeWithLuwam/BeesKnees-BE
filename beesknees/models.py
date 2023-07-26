from django.db import models

class DExercise_board(models.Model):
    name = models.CharField(max_length=200)
    description=models.CharField(max_length=500)

    def _str_(self):
        return self.name + '' + self.description
    