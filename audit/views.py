from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Howdy volks")

def shmeng(request):
    return HttpResponse("Shcmeng und Drek isten der liebeslungenlied volks")


