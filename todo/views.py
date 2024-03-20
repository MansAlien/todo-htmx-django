from django.views.generic import ListView
from django.shortcuts import render
from todo.models import Task
from django.http import HttpResponse

class TodoListView(ListView):
    model = Task
    template_name = "home.html"

def createview(request):
    task_name = request.POST.get("task")
    task = Task.objects.create(title=task_name)
    task_list = Task.objects.all()
    context = {"task_list":task_list}
    return render(request, "home.html", context)

def cancelview(request):
    task_list = Task.objects.all()
    context = {"task_list":task_list}
    return render(request, "home.html", context)

def renameview(request, pk):
    task = Task.objects.get(id=pk)
    context = {"task":task}
    return render(request, "edit.html", context)



def applyview(request, pk):
    task = Task.objects.get(id=pk)
    task.title = request.POST.get("update") 
    task.save()
    task_list = Task.objects.all()
    context = {"task_list":task_list}
    return render(request, "home.html", context) 

def deleteview(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    task_list = Task.objects.all()
    context = {"task_list":task_list}
    return render(request, "home.html", context)

