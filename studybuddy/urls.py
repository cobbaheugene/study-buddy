from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('room/<str:pk>/', views.rooms, name='rooms'),
    path("createroom/", views.CreateRoom, name="create-room"),
]
