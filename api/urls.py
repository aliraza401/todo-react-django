from django.urls import path
from .import views

app_name = 'api'

urlpatterns = [
    path('info/', views.ApiInfo, name= 'info' ),
    path('list/', views.TaskList, name='list'),
    path('detail/<str:id>/', views.TaskDetail, name='detail'),
    path('create/', views.TaskCreate, name='create'),
    path('update/<str:id>', views.TaskUpdate, name='update'),
    path('delete/<str:id>', views.TaskDelete, name='delete'),

    
]