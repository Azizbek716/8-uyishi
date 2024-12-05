from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.group_name, name='group_list'),
    path('create/', views.group_type, name='create'),
    path('detail/<int:pk>/', views.group_detail, name='detail'),
    path('delete/<int:pk>/', views.group_delete, name='delete'),
]