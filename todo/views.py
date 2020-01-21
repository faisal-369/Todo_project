from django.shortcuts import render, redirect
from . models import Todo
from . forms import TodoForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)

        if form.is_valid():
            form.save()
            todos = Todo.objects.all
            return render(request, 'todo/index.html', {'todos': todos})

    else:
        todos = Todo.objects.all
        return render(request, 'todo/index.html', {'todos': todos})


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('/')


def todo_pending(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = False
    todo.save()
    return redirect('/')


def todo_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('/')


def edit(request, todo_id):
    if request.method == 'POST':
        todos = Todo.objects.get(id=todo_id)
        form = TodoForm(request.POST or None, instance=todos)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        todos = Todo.objects.get(id=todo_id)
        return render(request, 'todo/update.html', {'todos': todos})
