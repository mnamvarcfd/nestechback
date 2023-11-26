from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('get_team_members/', views.get_team_members, name='get_team_members'),
    path('get_team_members/<str:pk>/', views.get_team_member, name='get_team_member'),
    path('get_services/', views.get_services, name='get_services'),
]
