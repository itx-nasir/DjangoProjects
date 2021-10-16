# I have created this file- Nasir
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def Analyze(request):
    inptext= request.GET.get('text', 'default')
    RemovePuncStatus=request.GET.get('removepunc', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    Analyzed=""
    if RemovePuncStatus=='on':
        for ch in (inptext):
            if ch not in punctuations:
                Analyzed=Analyzed+ch
    else:
        Analyzed='Check is off'

    params={'purpose':'Removed Punctuations','Analyzed_text':Analyzed}
    return render(request,'Analyze.html',params)
