from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('get_team_members/', views.get_team_members, name='get_team_members'),
    path('get_team_member_imag/', views.get_team_member_imag, name='get_team_member_imag'),
    # path('get_team_members/<str:pk>/', views.get_team_member, name='get_team_members'),
    path('get_services/', views.get_services, name='get_services'),
    path('get_service_imag/', views.get_service_imag, name='get_service_imag'),
    path('get_video/', views.get_video, name='get_video'),
    path('get_all_video/', views.get_all_video, name='get_all_video'),
]
