from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo = TodoItem.objects.all()
    return render(request, 'index.html', {
        'all_items': all_todo 
    })

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    delete_item = TodoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect('/todo/')