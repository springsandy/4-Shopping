from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('login/', auth_views.views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logput/', auth_views.views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]