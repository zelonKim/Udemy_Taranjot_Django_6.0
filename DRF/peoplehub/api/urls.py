from django.urls import path
from .import views

urlpatterns = [
    # path('multipleobj/', views.multipleobj),
    # path('singleobj/<int:id>/', views.singleobj),
    
    # path('multipleobj/', views.MultipleObjAPIView.as_view()),
    # path('singleobj/<int:id>/', views.SingleObjAPIViw.as_view()),
    
    # path('multipleobj/', views.MultipleObjGenericAPIView.as_view()),
    # path('singleobj/<int:pk>/', views.SingleObjGenericAPIView.as_view()),
    
    path('multipleobj/', views.MultipleObjConcreteAPIView.as_view()),
    path('singleobj/<int:pk>/', views.SingleObjConcreteAPIView.as_view()),
]