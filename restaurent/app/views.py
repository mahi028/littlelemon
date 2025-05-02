from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Menu, Table
from .forms import BookTableForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu})

def menu_item(request, pk):
    item = Menu.objects.get(pk=pk)
    return render(request, 'menu_item.html', {'item': item})

def book(request):
    avaliable_tables = Table.objects.filter(isAvailable = True)
    form = BookTableForm()

    if request.method == 'POST':
        form = BookTableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Table has been booked!')
            return redirect('index')
        messages.warning(request, 'Invalid Input!')
    return render(request, 'book.html', {'form': form, 'tables': avaliable_tables})
