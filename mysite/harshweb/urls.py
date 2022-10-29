from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name= "index"),
    path('school/',views.school,name= "school"),
    path('college/',views.college,name= "college"),
    path('ug/',views.ug,name= "ug"),
    path('pg/',views.pg,name= "pg")
]