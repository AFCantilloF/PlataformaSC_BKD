from django.urls import path,re_path
from . import views 

urlpatterns = [
    path('', views.apiOverview),
    path('base/', views.base),
    path('userlist/', views.userlist, name="UserList"),
    path('userdetail/<str:pk>/', views.userdetail, name="UserDatail"),
    path('createuser/', views.createuser, name="createuser"),
    path('updateuser/<str:pk>/', views.updateuser, name="updateuser"),
    path('deleteuser/<str:pk>/', views.deleteuser, name="deleteuser"),
    ]