from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()), 
    path('register/', views.RegisterView.as_view()),
    path('refresh/token', views.RefreshView.as_view()) 
]
