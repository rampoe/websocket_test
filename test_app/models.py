from django.db import models

class Test(models.Model):
    message = models.TextField()
    number = models.IntegerField()
