from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()), 
    path('register/', views.RegisterView.as_view()),
    path('refresh/token', views.RefreshView.as_view()), 
    path('update/', views.DetailUpdateView.as_view(), name='update'),
    path('confirm/<int:user_id>/', views.ConfirmationView.as_view(), name='confirm_registration'),
]
