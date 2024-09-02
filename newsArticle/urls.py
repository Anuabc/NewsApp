from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("<news>/", view=views.article, name='article'),
]