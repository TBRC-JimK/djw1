from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Howdy volks")

def work(request, work_id: int):
    return HttpResponse(f"looking at  work {work_id}")

def contributor(request,c_id: int):
    return HttpResponse(f"Looking up contributor {c_id}")

def submittal(request, submittal_id: int):
    return HttpResponse("Looking for sumbittal id %d" % submittal_id)

