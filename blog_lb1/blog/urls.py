from django.urls import path

from . import views

urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.home, name='home'),
    path('user/exit', views.exit, name='usr-exit'),
    path('user/login', views.login_usr, name='usr-login'),
] 