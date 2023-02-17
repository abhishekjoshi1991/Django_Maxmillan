from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:mon>', views.month_by_number),
    path('<str:mon>', views.month, name='monthly-challenge'),
]