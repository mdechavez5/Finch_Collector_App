from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dancers/', views.DancerList.as_view(), name="dancer_list"),
    path('dancers/new/', views.DancerCreate.as_view(), name="dancer_create"),
    path('dancers/<int:pk>/', views.DancerDetail.as_view(), name="dancer_detail"),
] 