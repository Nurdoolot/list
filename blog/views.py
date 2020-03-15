from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    lists = List.objects.all()
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'lists': lists, 'form': form}
    return render(request, 'lists/list.html', context)

@login_required(login_url='login')
def update(request, pk):
    list = List.objects.get(id=pk)
    form = ListForm(instance=list)
    if request.method == 'POST':
        form = ListForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'lists/update_list.html', context)

@login_required(login_url='login')
def delete(request, pk):
    item = List.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'lists/delete.html', context)