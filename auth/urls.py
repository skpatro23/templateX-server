from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
    path('me/', views.Me.as_view(), name='me')
]
