# Generated by Django 2.1.1 on 2018-11-01 23:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='temperature ciała')),
                ('stressed', models.BooleanField(choices=[(False, 'Nie'), (True, 'Tak')], default='Nie', verbose_name='Stres?')),
                ('sick', models.BooleanField(choices=[(False, 'Nie'), (True, 'Tak')], default='Nie', verbose_name='Choroba?')),
                ('out_of_time', models.BooleanField(choices=[(False, 'Nie'), (True, 'Tak')], default='Nie', verbose_name='pomiar poza planowaną godziną?')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='data i czas pomiaru')),
                ('remarks', models.CharField(blank=True, max_length=500, verbose_name='uwagi')),
                ('user', models.ForeignKey(on_delete=models.SET('deleted user'), to=settings.AUTH_USER_MODEL, verbose_name='podpis')),
            ],
        ),
    ]
