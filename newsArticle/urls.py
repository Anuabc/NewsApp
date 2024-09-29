from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("news/<path:link>/", view=views.article, name='article'),
    path("meaning/", view=views.meaning, name='meaning')
]