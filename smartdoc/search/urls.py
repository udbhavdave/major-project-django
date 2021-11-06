from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('upload/', views.upload, name='upload'),
    path('search-image/', views.search_image, name='search-image'),
    path('search-audio/', views.search_audio, name='search-audio'),
]
