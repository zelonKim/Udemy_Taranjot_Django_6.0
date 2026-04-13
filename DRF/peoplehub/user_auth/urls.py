from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('login/', views.LoginAPIView.as_view())
    path('login/', obtain_auth_token),
    path('register/', views.UserRegistration.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
]