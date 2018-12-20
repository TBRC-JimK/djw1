from django.shortcuts import render
from django.http import HttpResponse


from .models import Submittal

# Create your views here.


def index(request):
    # Do it the long way first
    # template = loader.get_template()
    # context = {'list_name': 'Submittals',
    #            'submittals': Submittal.objects.all(), }
    # return HttpResponse(template.render(context, request))
    context = {'list_name': 'Submittals',
                'submittals': Submittal.objects.all(), }
    return render(request, 'audit/submittals.html', context)

def work(request, work_id: int):
    return HttpResponse(f"looking at  work {work_id}")

def contributor(request,c_id: int):
    return HttpResponse(f"Looking up contributor {c_id}")

def submittal(request, submittal_id: int):
    return HttpResponse("Looking for sumbittal id %d" % submittal_id)

