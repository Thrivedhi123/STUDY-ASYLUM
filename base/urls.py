from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginpage,name="login_page"),
    path('logout/',views.logoutuser,name="logoutuser"),
    path('register/',views.registerpage,name="register"),
    path('profile/<str:pk>/',views.profilepage,name='profilepage'),
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room',views.create_room,name="create-room"),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-room/<str:pk>/', views.delete_room, name='delete-room'),
    path('delete-message/<str:pk>/', views.deletemessage, name='delete-message'),
    path('update-user/', views.updateuser, name='update-user'),
    path('topics/', views.topicspage, name='topics'),
    path('activity/', views.activitypage, name='activity'),


]