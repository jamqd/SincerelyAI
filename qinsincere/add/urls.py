from django.urls import path
from . import views

<<<<<<< HEAD
urlpatterns = [
    path('', views.index, name='index'),
=======
app_name = 'add'
urlpatterns = [
    # ex: /add/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /add/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /add/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
>>>>>>> 751c87058daf389b97484113501dbb29629abc22
]

