from django.urls import path
from django import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]

