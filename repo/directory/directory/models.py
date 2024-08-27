from django.db import models

class CSPANdata(models.Model):
    name=models.CharField(max_length=10000)
    description=models.CharField(max_length=10000000000000000000000000)
    def __str__(self):
        return self.name + ": " + self.description