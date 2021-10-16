from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')



def CalcDriver(request):
    val1=float(request.GET.get('num1',0))
    val2=float(request.GET.get('num2',0))
    sumstat=request.GET.get('sum')
    substat = request.GET.get('sub')
    mulstat = request.GET.get('mul')
    divstat = request.GET.get('div')
    modstat = request.GET.get('mod')
    result=0.0

    if sumstat=="on":
        result=val1+val2
    elif substat=="on":
        result=val1-val2
    elif mulstat=="on":
        result=val1*val2
    elif divstat=="on":
        result=val1/val2
    elif modstat=="on":
        result=val1%val2
    param = {'res':result}
    return render(request,'Analyze.html',param)