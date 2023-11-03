from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.accounts, name='list'),
    path('create/', views.create, name='create_account'),
    path('delete/<int:user_id>/', views.delete, name='delete_account'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    ]
