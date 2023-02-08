from django.urls import path
from . import views

urlpatterns = [
    path('<month>', views.index), # if str:month not given then it treats as str only
    # if str is specified then it check whether converted to string
    # if int is specified then it check whether converted to integer

    # order below is important, it first check month can be converted to integer if yes runs first route
    # if not then runs second route
    path('new/<int:mon>', views.month_by_number),
    path('new/<str:mon>', views.month),

]