from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index,name="index"),
    path('challenge/',views.challenge,name="challenge"),
    path('help/',views.home,name="help"),
]