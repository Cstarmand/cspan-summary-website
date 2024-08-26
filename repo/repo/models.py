from django.db import models

class Temp(models.Model):
    date= models.CharField(max_length=1000)
    summary= models.CharField(max_length=1000000000000000000000000000000)
    def __str__(self):
        return self.date + ': ' + self.summary