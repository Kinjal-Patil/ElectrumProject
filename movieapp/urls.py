from django.contrib import admin
from django.urls import path, include

from movieapp import views
from movieapp.views import *

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('movie-list/', MovieList.as_view(), name='movie-list'),
    path('movie-create/', views.movie_create, name='movie-create'),
    path('movie-edit/<pk>/', views.movie_edit, name='movie-edit'),

    path('genre-list/', GenreList.as_view(), name='genre-list'),
    path('genre-edit/<pk>/', views.genre_edit, name='genre-edit'),
]
