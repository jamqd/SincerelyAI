from django.urls import path

from . import views


urlpatterns = [
    path('', views.sms_response, name='sms')
]
