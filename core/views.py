import re
from turtle import title
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

@login_required
def tasks_list(request):
    tasks = Task.objects.filter(user_id=request.user).order_by('-done_on','-created_on')
    return render(request, 'core/tasks-list.html', {"tasks":tasks})

@login_required
def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'core/task.html', {'task':task})

@login_required
def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'ongoing'
            task.user_id = request.user
            task.save()
            return redirect('user-tasks')
    else:
        form =TaskForm()
        return render(request, 'core/new-task.html', {'form':form})

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method=='POST'):
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('user-tasks')
        else:
            return render(request, 'core/edit-task.html',{'form':form, 'task':task})
    else:
        return render(request, 'core/edit-task.html', {'form':form, 'task':task})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso')
    return redirect('user-tasks')

@login_required
def change_status(request, id):
    task = get_object_or_404(Task, pk=id)
    if task.done == 'ongoing':
        task.done = 'done'
    else:
        task.done = 'ongoing'
    task.save()
    return redirect('user-tasks')

