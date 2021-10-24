
from django.shortcuts import render
from . models import Person


def homeView(request):
    return render(request, 'base.html')


def about(request):
   
    return render(request, 'about.html')


def contract(request):
     if request.method=='POST':
        Name=request.POST.get('name')
        dataset=Person(Name=Name)
        dataset.save()
     return render(request, 'contract.html')


def Login(request):
    return render(request, 'login.html')


def Ragistarion(request):
    return render(request, 'ragistration.html')


def Sview(request):
    return render(request, 'serias.html')
