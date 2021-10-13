from django.urls import path
from . import views


urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    #code below is parth of dynamic path/link/url
    path("", views.index, name="index"), # this is for /challenge/ path
    path("<int:month>", views.monthly_challange_by_number),
    path("<str:month>", views.monthly_challange, name="month-challenge")
]
