from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.

TAKNIE = ((False, 'Nie'),
             (True, 'Tak')
            )
SLUZ = (('none', 'none'),
        ('sticky', 'sticky'),
        ('transparent', 'transparent'),
        ('opaque', 'opaque'),
            )

class FertileMucus(models.Model):
    description = models.CharField(max_length=50, verbose_name='śluz płodny', blank=True, null=True)
    def __str__(self):
        return self.description

class NotFertileMucus(models.Model):
    description = models.CharField(max_length=50, verbose_name='śluz płodny', blank=True, null=True)
    def __str__(self):
        return self.description





class Measurement(models.Model):
    datetime.datetime.now(tz=timezone.utc)
    temperature = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='temperatura ciała')
    period_day = models.IntegerField(verbose_name="Dzień cyklu", null=True)
    stressed = models.BooleanField(choices=TAKNIE, default="Nie", verbose_name='Stres?')
    sick = models.BooleanField(choices=TAKNIE, default="Nie", verbose_name='Choroba?')
    out_of_time = models.BooleanField(choices=TAKNIE, default="Nie", verbose_name='pomiar poza planowaną godziną?')

    date = models.DateTimeField(auto_now_add=True, verbose_name='data i czas pomiaru')
    remarks = models.CharField(max_length=500, verbose_name='uwagi', blank=True)
    user = models.ForeignKey(User, on_delete=models.SET('deleted user'), verbose_name='podpis')
    fertile_mucus = models.ManyToManyField(FertileMucus, blank=True)
    not_fertile_mucus = models.ManyToManyField(NotFertileMucus, blank=True)

    #fertile_mucus = models.SelectMultipleField(max_length=120, choices=SLUZ, verbose_name='śluz', blank=True)



    #def __str__(self):
    #    return self.id