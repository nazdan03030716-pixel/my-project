from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('publications/', views.post_list, name='post_list'),
    path('publications/<int:pk>/', views.post_detail, name='post_detail'),
    path('publications/add/', views.post_create, name='post_create'),
    path('publications/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='myapp:home'), name='logout'),
]