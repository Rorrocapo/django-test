from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name= 'apiOverview'),
    path('list-client/', views.showClients, name= 'list-client'),
    path('list-users/', views.showUsers, name= 'list-users'),
    path('create-client/', views.createClient, name='create-client'),
    path('create-user/', views.createUser, name= 'create-user'),
]