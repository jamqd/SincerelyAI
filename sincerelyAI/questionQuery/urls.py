from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search_question'),
    path('result/', views.result, name='result'),
]

