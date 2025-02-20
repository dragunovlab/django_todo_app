from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, SubTask
from .forms import TaskForm, SubTaskForm

def todo_list(request):
    """
    Отображает список всех задач.
    При POST-запросе создаётся новая задача.
    """
    tasks = Task.objects.all().order_by('-created_at')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'advanced_todo_list/todo_list.html', {'tasks': tasks, 'form': form})

def task_detail(request, task_id):
    """
    Детальная страница задачи: отображает подзадачи, форму для их создания
    и прогресс-бар выполнения.
    """
    task = get_object_or_404(Task, id=task_id)
    subtasks = task.subtask_set.all().order_by('-created_at')
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            subtask = form.save(commit=False)
            subtask.task = task
            subtask.save()
            return redirect('task_detail', task_id=task_id)
    else:
        form = SubTaskForm()
    return render(request, 'advanced_todo_list/task_detail.html', {
        'task': task,
        'subtasks': subtasks,
        'form': form
    })

def toggle_task(request, task_id):
    """
    Переключает статус выполнения задачи.
    """
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('todo_list')

def delete_task(request, task_id):
    """
    Удаляет задачу.
    """
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('todo_list')

def toggle_subtask(request, subtask_id):
    """
    Переключает статус выполнения подзадачи.
    """
    subtask = get_object_or_404(SubTask, id=subtask_id)
    subtask.completed = not subtask.completed
    subtask.save()
    return redirect('task_detail', task_id=subtask.task.id)

def delete_subtask(request, subtask_id):
    """
    Удаляет подзадачу.
    """
    subtask = get_object_or_404(SubTask, id=subtask_id)
    task_id = subtask.task.id
    subtask.delete()
    return redirect('task_detail', task_id=task_id)
