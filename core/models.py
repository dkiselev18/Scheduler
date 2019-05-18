from django.db import models


class MilitaryUnits(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Название воинской части")
    Number = models.IntegerField(verbose_name="Номер воинской части", null=True, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Воинские части"
        verbose_name_plural = "1. Воинские части"


class ResponsiblePersons(models.Model):
    MilitaryUnitsID = models.ForeignKey(MilitaryUnits, verbose_name="Название воинской части", on_delete=models.CASCADE)
    Name = models.CharField(max_length=200, verbose_name="Наименование должности ответственного лица")
    ShortName = models.CharField(max_length=200, verbose_name="Краткое наименование должности ответственного лица")

    def __str__(self):
        return self.ShortName

    class Meta:
        verbose_name = "Ответственные исполнители"
        verbose_name_plural = "2. Ответственные исполнители"


class Events(models.Model):
    ResponsiblePersonsID = models.ForeignKey(ResponsiblePersons, verbose_name="Ответственный", on_delete=models.CASCADE)
    Name = models.CharField(max_length=300, verbose_name="Название мероприятия")
    StartDate = models.DateField(verbose_name="Дата начала мероприятия")
    EndDate = models.DateField(verbose_name="Дата окончания мероприятия")
    StartTime = models.TimeField(verbose_name="Время начала мероприятия", null=True, blank=True)
    EndTime = models.TimeField(verbose_name="Время окончания мероприятия", null=True, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Основные мероприятия"
        verbose_name_plural = "3. Основные мероприятия"
