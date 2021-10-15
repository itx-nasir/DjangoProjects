# I have created this file- Nasir
from django.http import HttpResponse


def index(request):
    file=open("Links.txt")
    line=file.read()
    file.close()
    return HttpResponse("<h1>"+line+"</h1>")
