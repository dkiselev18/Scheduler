# Generated by Django 2.2.1 on 2019-05-19 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MilitaryUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Название воинской части')),
                ('Number', models.IntegerField(blank=True, null=True, verbose_name='Номер воинской части')),
            ],
            options={
                'verbose_name': 'Воинские части',
                'verbose_name_plural': '1. Воинские части',
            },
        ),
        migrations.CreateModel(
            name='ResponsiblePerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Наименование должности ответственного лица')),
                ('ShortName', models.CharField(max_length=200, verbose_name='Краткое наименование должности ответственного лица')),
                ('MilitaryUnitsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.MilitaryUnit', verbose_name='Название воинской части')),
            ],
            options={
                'verbose_name': 'Ответственные исполнители',
                'verbose_name_plural': '2. Ответственные исполнители',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300, verbose_name='Название мероприятия')),
                ('StartDate', models.DateField(verbose_name='Дата начала мероприятия')),
                ('EndDate', models.DateField(verbose_name='Дата окончания мероприятия')),
                ('StartTime', models.TimeField(blank=True, null=True, verbose_name='Время начала мероприятия')),
                ('EndTime', models.TimeField(blank=True, null=True, verbose_name='Время окончания мероприятия')),
                ('ResponsiblePersonsID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ResponsiblePerson', verbose_name='Ответственный')),
            ],
            options={
                'verbose_name': 'Основные мероприятия',
                'verbose_name_plural': '3. Основные мероприятия',
            },
        ),
    ]
