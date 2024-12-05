from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('craete', views.student_form, name='create'),
    path('detail/<int:pk>', views.student_detil, name='detail'),
    path('delete/<int:pk>', views.student_delete, name='delete')
]