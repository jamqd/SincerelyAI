from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search_question'),
    path('thanks/', views.answer, name='answer')
]
