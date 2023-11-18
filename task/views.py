from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

tasks = []


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")


def index(request):
    return render(request, "task/index.html", {"tasks": tasks})


def add(request):
    print(tasks)
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task6 = form.cleaned_data["task"]
            tasks.append(task6)
            return render(request, "task/index.html", {"tasks": tasks})
        else:
            form = NewTaskForm()
            return render(request, "task/add.html", {"form": form})     

    return render(request, "task/add.html", {"form": NewTaskForm()})
