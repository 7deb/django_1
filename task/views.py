from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

tasks = []
def index(request):
    return render(request,"task/index.html",{
        "tasks":tasks
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("task:index"))
        else:
            form = NewTaskForm()

    return render(request,"task/add.html",{
        "tasks":tasks
    })
