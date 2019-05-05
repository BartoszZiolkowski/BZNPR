# Generated by Django 2.2 on 2019-04-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NPRlog', '0004_auto_20190423_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='fertile_mucus',
        ),
        migrations.AddField(
            model_name='measurement',
            name='fertile_mucus',
            field=models.ManyToManyField(null=True, to='NPRlog.FertileMucus'),
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='not_fertile_mucus',
        ),
        migrations.AddField(
            model_name='measurement',
            name='not_fertile_mucus',
            field=models.ManyToManyField(null=True, to='NPRlog.NotFertileMucus'),
        ),
    ]