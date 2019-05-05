from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


from .forms import LoginForm, AddUserForm, ChangeUserDataForm, AddMeasurementForm
from django.views.generic import DeleteView, CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from .models import Measurement
import re
import os
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import make_aware

import pytz


# Create your views here.


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return HttpResponse('post request')


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            userAuth = authenticate(**form.cleaned_data)

            if userAuth:
                login(request, userAuth)
                logged_in = request.user.is_authenticated

                return redirect('/')
                # render(request, 'home.html', {'data':userAuth})
            else:
                return render(request, 'login.html', {'form': form,
                                                      'message': 'wrong data'})


class Logout(View):

    def get(self, request):
        logout(request)
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        logout(request)
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


class AddUser(View):

    def get(self, request):

        form = AddUserForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):

        form = AddUserForm(request.POST)
        if form.is_valid():

            try:
                User.objects.get(username=form.cleaned_data['username'])

                return render(request, 'add_user.html', {'form': form,
                                                         'message': 'user already exists'})

            except Exception as e:
                if form.cleaned_data['password'] == form.cleaned_data['repeat_password']:

                    User.objects.create_user(username=form.cleaned_data['username'],
                                             password=form.cleaned_data['password'],
                                             first_name=form.cleaned_data['first_name'],
                                             last_name=form.cleaned_data['last_name'],
                                             email=form.cleaned_data['email'])

                    return redirect('/')

                else:
                    return render(request, 'add_user.html', {'form': form,
                                                             'message': 'passowords are not the same'})
        return render(request, 'add_user.html', {'form': form,
                                                 'message': 'coś nie tak w formularzu'})


class ChangeUserDataView(View):

    def get(self, request, user_id):

        try:
            user = User.objects.get(pk=user_id)
        except:
            return HttpResponse('there is no user with id {}'.format(user_id))

        form = ChangeUserDataForm(initial=model_to_dict(user))
        print(request.user.username)

        return render(request, 'change_user_data.html', {'form': form,
                                                         'user_id': user_id})

    def post(self, request, user_id):
        form = ChangeUserDataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = User.objects.get(pk=user_id)
            if data['password'] == data['repeat_password']:
                user.set_password(data['password'])
                user.username = (data['username'])
                user.save()

                return redirect('/')
            else:
                return render(request, 'change_user_data.html', {'form': form,
                                                                 'error': 'password not the same',
                                                                 'user_id': user_id
                                                                 })
        return render(request, 'change_user_data.html', {'form': form,
                                                         'error': 'form not valid',
                                                         'user_id': user_id
                                                         })


"""
class AddMeasurement(CreateView):
    model = Measurement
    fields = ['temperature', 'stressed', 'sick', 'out_of_time', 'remarks']

    success_url = '/'
"""

class AddMeasurement(View):
    def get(self, request):

        user = User.objects.get(pk=request.user.id)

        data_raw = Measurement.objects.filter(date__lte=datetime.now(), user=user).order_by('-date')[0]

        data_date = data_raw.date

        date_now = datetime.now()
        date_now = make_aware(date_now, timezone.get_current_timezone())
        measurement_now_difference = date_now - data_date

        data = model_to_dict(data_raw)

        data['period_day'] += measurement_now_difference.days

        form = AddMeasurementForm(initial=data)

        return render(request, 'add_measurement_form.html', {'form': form})

    def post(self, request):

        form = AddMeasurementForm(request.POST)
        if form.is_valid():






            data = form.cleaned_data

            data['user_id'] = request.user.pk

            data_stripped = data
            fertile_mucus = data_stripped.pop('fertile_mucus')
            not_fertile_mucus = data_stripped.pop('not_fertile_mucus')



            try:
                new_measurement = Measurement.objects.create(**data)
                new_measurement.fertile_mucus.set(fertile_mucus)
                new_measurement.not_fertile_mucus.set(not_fertile_mucus)



                return redirect('/')
            except Exception as e:

                return render(request, 'add_measurement_form.html', {'form': form,
                                                           'message': e})

        return render(request, 'add_measurement_form.html', {'form': form,
                                                   'message': 'coś nie tak w formularzu'})



class AllMeasurementsView(View):

    def get(self, request):

        measurements = Measurement.objects.filter(user_id=request.user.pk).order_by('-date')

        print(measurements)

        return render(request, 'measurements_list.html', {'samples': measurements})



class EditMeasurementView(UpdateView):
    model = Measurement
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/all_measurements_list'