from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('<int:id>/', views.shortcut),
]
