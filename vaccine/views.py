from django.shortcuts import render
from django.http import HttpResponse
from .forms import vaccineForm
from .models import Hospital
# Create your views here.

def index(request):
    params={
        'goto':'next',
    }
    return render(request, 'vaccine/index.html',params)

def next(request):
    huken=str(request.GET.get('huken'))
    sityou=str(request.GET.get('sityou'))
    year=str(request.GET.get('year'))
    month=str(request.GET.get('month'))
    day=str(request.GET.get('day'))
    sei=str(request.GET.get('sei'))
    mei=str(request.GET.get('na'))
    time=str(request.GET.get('time'))
    mail=str(request.GET.get('mail'))
    si_tmp=sityou.split('市')
    si=si_tmp[0]
    data=Hospital.objects.filter(city__contains=si)
    params={
        'sei' : sei,
        'mei' : mei,
        'time' : time,
        'huken': huken,
        'si' : si,
        'data' : data,
        'year' : year,
        'month' : month,
        'day' : day,
        'mail' : mail,
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

def decide(request):
    all=str(request.GET.get('all'))
    tmp=all.split(',')
    hospital_name=tmp[0]
    myouji=tmp[8]
    namae=tmp[9]
    year=tmp[4]
    month=tmp[5]
    day=tmp[6]
    time=tmp[7]
    params={
        'hospital' : hospital_name,
        'myouji' : myouji,
        'namae' : namae,
        'year' : year,
        'month' : month,
        'day' : day,
        'all' : all,
        'time' : time,
    }
    return render(request, 'vaccine/decide.html',params)
    