from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index,name="index"),
    path('challenge/',views.challenge,name="challenge"),
    path('home/',views.home,name="home"),
    path('help/',views.help,name="help"),
]