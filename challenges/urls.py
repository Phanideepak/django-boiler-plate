from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month>', views.index_monthly_challenge_by_number),
    path('<str:month>', views.index_monthly_challenge, name='monthly-challenge'),
]