# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Todolist, Category
import datetime


# Create your views here.

def index(request):# the index view
    todos = Todolist.objects.all()  # quering all todos with the object manager
    categories = Category.objects.all()  # getting all categories with object manager

    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            date = str(request.POST["date"])  # date
            category = request.POST["category_select"]  # category
            content = title + " -- " + date + " " + category  # content
            Todo = Todolist(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()  # saving the todo
              # reloading the page

        # Added two methods for sorting
        if "taskSortDsc" in request.POST: 
            # Returns descending order of model objects
            todos = Todolist.objects.all().order_by("due_date")

        if "taskSortAsc" in request.POST:  
            # Returns ascending order of model objects
            todos = Todolist.objects.all().order_by("-due_date")
           
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            checkedlist = request.POST.getlist('checkedbox')
            for todo_id in checkedlist:
                todo = Todolist.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo

    return render(request, "index.html", {"todos": todos,"categories": categories})
