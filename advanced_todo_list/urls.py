from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    
    # Действия с задачами
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    
    # Действия с подзадачами
    path('subtask/toggle/<int:subtask_id>/', views.toggle_subtask, name='toggle_subtask'),
    path('subtask/delete/<int:subtask_id>/', views.delete_subtask, name='delete_subtask'),
]
