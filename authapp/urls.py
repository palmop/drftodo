from authapp import views
from django.urls import path

urlpatterns = [
    path('register', views.RegisterUserApp.as_view(), name='register'),
    path('login', views.LoginUserApp.as_view(), name='login'),
    path('userinfo', views.UserInfo.as_view(), name='userinfo'),
]