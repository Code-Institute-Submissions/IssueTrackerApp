"""Reset password URLs"""
from django.contrib.auth import views
from django.urls import path

urlpatterns = [
    path('', views.PasswordResetView.as_view(), name='password_reset'),
    path('done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
