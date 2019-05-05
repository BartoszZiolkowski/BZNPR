"""BZNPR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from NPRlog.views import HomeView, Login, Logout, AddUser, ChangeUserDataView, AddMeasurement, AllMeasurementsView, \
    EditMeasurementView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home_view'),
    url(r'^login', Login.as_view(), name='login-form'),
    url(r'^logout', Logout.as_view(), name='logout'),
    url(r'^add_user', AddUser.as_view(), name='add-user'),
    path('edit_user/<user_id>', ChangeUserDataView.as_view(), name='edit-user'),
    path('add_measurement', AddMeasurement.as_view(), name='add-measurement'),
    path('all_measurements_list', AllMeasurementsView.as_view(), name='all-measurements'),
    path('edit_measurement/<id>', EditMeasurementView.as_view(), name='edit-measurement'),
]
