from django.shortcuts import render, redirect

from .models import *


def index_view(request):
    context = {
        'tasks': Todo.objects.all()
    }
    return render(request, 'index.html', context)


def create_task_view(request):
    if request.method == "POST":
        task = request.POST['task']
        Todo.objects.create(
            task=task
        )
    return redirect('index_url')


def swap_status_deleted(request, id):
    todo = Todo.objects.get(id=id)
    todo.status = "DELETED"
    todo.save()
    return redirect('index_url')


def swap_status_finished(request, id):
    todo = Todo.objects.get(id=id)
    todo.status = "FINISHED"
    todo.save()
    return redirect('index_url')


def inprogress_view(request):
    context = {
    'tasks' : Todo.objects.filter(status = "In Progress")
    }
    return render(request, 'inprogress.html', context)


def deleted_task_view(request , pk):
    task = Todo.objects.get(pk=pk)
    task.delete()