from django.urls import path
from . import views

urlpatterns = [
    path('<int:mon>', views.month_by_number),
    path('<str:mon>', views.month),
]