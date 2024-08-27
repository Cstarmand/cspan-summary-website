from django.db import models

class CSPANdata(models.Model):
    date=models.CharField(max_length=10000)
    summary=models.CharField(max_length=10000000000000000000000000)
    def __str__(self):
        return self.date + ": " + self.summary