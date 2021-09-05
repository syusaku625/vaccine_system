from django.shortcuts import render
from django.http import HttpResponse
from .forms import vaccineForm
# Create your views here.

def index(request):
    params={
        'goto':'next',
    }
    return render(request, 'vaccine/index.html',params)

def next(request):
    params={
        'lastname': request.GET.get('sei'),
        'firstname': request.GET.get('na'),
        'huken': request.GET.get('huken'),
        'sityou': request.GET.get('sityou'),
    }
    return render(request, 'vaccine/test.html',params)

def form(request):
    params={
        'message' : 'your data',
        'form': vaccineForm()
    }
    if(request.method=='POST'):
        params['message']=request.POST['lastname']+request.POST['firstname']+request.POST['mail']+request.POST['age']+request.POST['radio']
        params['form']=vaccineForm(request.POST)

    return render(request, 'vaccine/next.html',params)
    