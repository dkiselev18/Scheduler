from django.db import models
from django.utils.timezone import now
import uuid


class SchedulerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(verbose_name="Время создание записи", default=now, editable=False)
    updated = models.DateTimeField(verbose_name="Время последего изменения записи", default=created)

    class Meta:
        abstract = True


class MilitaryUnit(SchedulerModel):
    name = models.CharField(max_length=200, verbose_name="Воинская часть")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Воинская часть"
        verbose_name_plural = "1. Воинская часть"


class ResponsiblePerson(SchedulerModel):
    name = models.CharField(max_length=200, verbose_name="Наименование должности ответственного лица")
    short_name = models.CharField(max_length=200, verbose_name="Краткое наименование должности ответственного лица")

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Ответственные исполнители"
        verbose_name_plural = "2. Ответственные исполнители"


class EventDef(SchedulerModel):
    """
    This model represents all event types.
    """
    name = models.CharField(max_length=300, verbose_name="Название мероприятия")


class TimeSlot(SchedulerModel):
    """
    This model represents time slots for events (Event model).
    """
    start_date = models.DateField(verbose_name="Дата начала мероприятия")
    end_date = models.DateField(verbose_name="Дата окончания мероприятия")
    start_time = models.TimeField(null=True, blank=True, verbose_name="Время окончания мероприятия")
    end_time = models.TimeField(null=True, blank=True, verbose_name="Время окончания мероприятия")


class Event(SchedulerModel):
    militaryUnit = models.ForeignKey(MilitaryUnit, verbose_name="Подразделение", on_delete=models.CASCADE)
    eventDef = models.ForeignKey(EventDef, verbose_name="Название мероприятия", on_delete=models.CASCADE)
    responsiblePersons = models.ForeignKey(ResponsiblePerson, verbose_name="Ответственный", on_delete=models.CASCADE,
                                           null=True, blank=True)
    timeSlot = models.ForeignKey(TimeSlot, unique=True, verbose_name="Время проведения мероприятия")
    template_event = fk

    class Meta:
        verbose_name = "Основные мероприятия"
        verbose_name_plural = "3. Основные мероприятия"

class EventPattern():

