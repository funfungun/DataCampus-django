from django.urls import path
from . import views

urlpatterns = [
    path('one/', views.one),
    path('one/two/', views.two),
    path('one/two/three/', views.three),
    path('', views.index),
]