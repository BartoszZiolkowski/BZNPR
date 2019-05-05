from django import forms
from django.contrib.auth.models import User
from .models import TAKNIE, SLUZ
from .models import Measurement
from datetime import datetime

#from .validators import validate_name, validate_surname, validate_email_domain

from .models import FertileMucus, NotFertileMucus

class UserForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=128)
    last_name = forms.CharField(label='Nazwisko', max_length=128)
    email = forms.EmailField(label='Email')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class AddUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=128, widget=forms.PasswordInput)



class ChangeUserDataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=128, widget=forms.PasswordInput)



class AddMeasurementForm(forms.Form):
    temperature = forms.DecimalField(decimal_places=2, max_digits=4, initial=36.60, widget=forms.NumberInput(attrs={'step': 0.05}))
    period_day = forms.IntegerField(widget=forms.NumberInput)
    stressed = forms.BooleanField(required=False, help_text='Stres?')
    sick = forms.BooleanField(required=False, help_text='Choroba?')
    out_of_time = forms.BooleanField(required=False, help_text='pomiar poza planowaną godziną?')
    #date = forms.DateTimeField(widget=forms.DateInput)
    remarks = forms.CharField(max_length=500, required=False)
    #user = forms.ForeignKey(User, on_delete=models.SET('deleted user'), verbose_name='podpis')
    fertile_mucus = forms.ModelMultipleChoiceField(queryset=FertileMucus.objects.all(), widget=forms.SelectMultiple)
    not_fertile_mucus = forms.ModelMultipleChoiceField(queryset=NotFertileMucus.objects.all(), widget=forms.SelectMultiple)

    # fertile_mucus = forms.SelectMultipleField(max_length=120, choices=SLUZ, verbose_name='śluz', blank=True)










"""
class AddMeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = '__all__'
        exclude = ['user', 'date']


class AddMeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = '__all__'

        exclude = ['user', 'date']
        widgets = {
            'temperature': forms.NumberInput(attrs={'step': 0.05}),
            #'fertile_mucus': forms.ModelChoiceField(queryset=None, to_field_name='name')
        }

"""

"""
    widgets = {
            'temperature': forms.NumberInput(attrs={'step': 0.01}),
        }
    
    
    
    temperature = forms.DecimalField(decimal_places=2, max_digits=4, label='temperatura ciała')
    stressed = forms.ChoiceField(choices=TAKNIE, initial=0, label='Stres?')
    sick = forms.ChoiceField(choices=TAKNIE, initial=TAKNIE[0], label='Choroba?')
    out_of_time = forms.ChoiceField(choices=TAKNIE, initial=TAKNIE[False], label='pomiar poza planowaną godziną?')

    remarks = forms.CharField(max_length=500, required=False, label='uwagi')
    sluz = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False, choices=SLUZ, label='śluz')
"""