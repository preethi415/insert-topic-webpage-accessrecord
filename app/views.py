from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.


def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=="POST":
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            t=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=t)[0]
            TO.save()
            return HttpResponse('data valid')
        else:
            return HttpResponse('data')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            t=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=t)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
            WO.save()
            return HttpResponse('data inserted')
        else:
            return HttpResponse('data invalid')
    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=="POST":
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(pk=n)
            d=AFDO.cleaned_data['date']
            a=AFDO.cleaned_data['author']
            AO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
            AO.save()
            return HttpResponse('data valid')
        else:
            return HttpResponse('data invalid')

    return render(request,'insert_accessrecord.html',d)
