# Warning that the Django tutorial says that
# shortcuts couple the model to the view
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404

from .models import Submittal, Item


# Create your views here.


def index(request):
    # Do it the long way first
    # template = loader.get_template()
    # context = {'list_name': 'Submittals',
    #            'submittals': Submittal.objects.all(), }
    # return HttpResponse(template.render(context, request))
    context = {'list_name': 'Items', 'items': Item.objects.all(), }
    return render(request, 'audit/items.html', context)


def contributor(request, c_id: int):
    return HttpResponse(f"Looking up contributor {c_id}")


def submittal(request, submittal_id: int):
    """
    Redirect to safe or cute method
    :param request:
    :param submittal_id:
    :return:
    """
    return submittal_cute(request, submittal_id)


def submittal_cute(request: HttpRequest, submittal_id: int) -> HttpResponse:
    """
    Use shortcut, which couples view and model more than we'd like
    :param request:
    :param submittal_id:
    :return:
    """
    a_submittal = get_object_or_404(Submittal, pk=submittal_id)
    return render(request, 'audit/submittal.html', {'submittal': a_submittal})


def submittal_safe(request, submittal_id: int) -> HttpResponse:
    try:
        a_submittal = Submittal.objects.get(pk=submittal_id)
    except Submittal.DoesNotExist:
        raise Http404(f"Submittal with id {submittal_id} does not exist")
    return render(request, 'audit/submittal.html', {'submittal': a_submittal})


def item(request: HttpRequest, item_id: int) -> HttpResponse:
    """
    handle a request for a single item detail
    :param request:
    :param item_id:
    :return:
    """
    an_item = get_object_or_404(Item, pk=item_id)

    return render(request, 'audit/item.html', {'item': an_item})
