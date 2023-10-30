from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
