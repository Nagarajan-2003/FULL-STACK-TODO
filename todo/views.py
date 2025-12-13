from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse
# Create your views here.
def create(request):
    if request.method=="POST":
        form =TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("read")
        return redirect("create")
    else:
        form=TodoForm()
    context={
         'form':form
    }
    return render(request,"create.html",context)
def read(request):
    todo=TodoModel.objects.all()
    form=TodoForm()
    context={
        'todo':todo 
    }
    return render(request,"read.html",context)
def update(request,id):
    obj=TodoModel.objects.get(id=id)
    if request.method=="POST":
        form=TodoForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("read")
        return redirect("update")
    else:
        form=TodoForm(instance=obj)
    context={
        'form':form
    }
    return render(request,"update.html",context)
def delete(request,id):
    obj=TodoModel.objects.get(id=id)
    obj.delete()
    return redirect("read")
    