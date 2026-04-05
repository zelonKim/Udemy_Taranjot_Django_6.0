from django.urls import path
from . import views


urlpatterns = [
     path('home/', views.home, name='basic'),
     # path('home/<str:city>/', views.home, name='basic'),
     path('<int:id>/', views.post, name='find'),   
]




