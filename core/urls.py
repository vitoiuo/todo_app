from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my-tasks/', views.tasks_list, name='user-tasks'),
    path('task/<int:id>/', views.task_view, name='task-view'),
    path('new-task/', views.new_task, name='new-task'),
    path('edit-task/<int:id>', views.edit_task, name='edit-task'),
    path('delete-task/<int:id>', views.delete_task, name='delete-task'),
    path('change-status/<int:id>', views.change_status, name='change-status'),
]