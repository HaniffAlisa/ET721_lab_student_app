from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST

def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_todo = Task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data.get('description', ''),
                category=form.cleaned_data.get('category', ''),
                due_date=form.cleaned_data.get('due_date', None),
                completed=form.cleaned_data.get('completed', False)
            )
            new_todo.save()
            return redirect('index')
    else:
        form = TaskForm()
    
    todo_tasks = Task.objects.order_by('id')
    context = {'todo_tasks': todo_tasks, 'form': form}
    return render(request, 'to_do_list/task_list.html', context)

@require_POST
def addTodoItem(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_todo = Task(
            title=form.cleaned_data['title'],
            description=form.cleaned_data.get('description', ''),
            category=form.cleaned_data.get('category', ''),
            due_date=form.cleaned_data.get('due_date', None),
            completed=form.cleaned_data.get('completed', False)
        )
        new_todo.save()
    return redirect('index')

def completedTodo(request, todo_id):
    todo = Task.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def deletecompleted(request):
    Task.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Task.objects.all().delete()
    return redirect('index')