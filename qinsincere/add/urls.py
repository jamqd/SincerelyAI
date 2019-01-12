from django.urls import path
from . import views

<<<<<<< HEAD
<<<<<<< HEAD
urlpatterns = [
    path('', views.index, name='index'),
=======
=======
>>>>>>> 751c87058daf389b97484113501dbb29629abc22
app_name = 'add'
urlpatterns = [
    # ex: /add/
    #path('', views.IndexView.as_view(), name='sentence'),
    path('', views.index, name='sentence'),
    # ex: /add/ml/
    path('ml/', views.get_name, name='ml'),
    # ex: /add/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /add/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /add/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
<<<<<<< HEAD
>>>>>>> 751c87058daf389b97484113501dbb29629abc22
=======
>>>>>>> 751c87058daf389b97484113501dbb29629abc22
]

