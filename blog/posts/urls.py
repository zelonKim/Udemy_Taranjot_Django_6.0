from django.urls import path
from . import views


urlpatterns = [
     path('', views.home, name='basic'),
     path('<int:id>/', views.post, name='post'),   
     path('tags/<int:id>/', views.tags, name='tag'),
     path('search/', views.search, name='search')
]




