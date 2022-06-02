from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('dancers/', views.DancerList.as_view(), name="dancer_list"),
    path('dancers/new/', views.DancerCreate.as_view(), name="dancer_create"),
    path('dancers/<int:pk>/', views.DancerDetail.as_view(), name="dancer_detail"),
    path('dancers/<int:pk>/update',views.DancerUpdate.as_view(), name="dancer_update"),
    path('dancers/<int:pk>/delete',views.DancerDelete.as_view(), name="dancer_delete"),
    path('dancers/<int:pk>/choreos/new/', views.ChoreoCreate.as_view(), name="choreo_create"),
    path('playlists/<int:pk>/choreos/<int:choreo_pk>/', views.PlaylistChoreoAssoc.as_view(), name="playlist_choreo_assoc"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('teams/', views.TeamsList.as_view(), name="teams_list"),
] 