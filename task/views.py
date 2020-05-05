from django.shortcuts import render
from .forms import TaskForm
from .models import Task
# Create your views here.


def task_list(request):
    tasks = Task.objects.all()
    context = {
        'form': TaskForm,
        'tasks': tasks
    }
    return render(request, 'task/task_list.html', context)
