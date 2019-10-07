#URLconf - uplyft
from django.urls import path

from . import views

app_name = 'uplyft'
urlpatterns = [
    # ex: /uplyft/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /uplyft/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /uplyft/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /uplyft/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /uplyft/register
    path('register/', views.register, name='register'),
]