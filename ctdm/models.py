from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()


class NewData(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    class Meta:
        verbose_name = 'New Data'
        verbose_name_plural = 'New Data'
