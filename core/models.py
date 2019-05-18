from django.db import models


class MilitaryUnit(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Название воинской части")
    Number = models.IntegerField(verbose_name="Номер воинской части", null=True, blank=True)

    def __str__(self):
        return self.Name


class