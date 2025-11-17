from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.team, name='team'),
    path('member/<str:member_id>/', views.member, name='member'),
    path('system/', views.system, name='system'),
    path('process/', views.process, name='process'),
    path('video/', views.video, name='video'),
]
