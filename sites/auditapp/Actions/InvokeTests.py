"""
View to invoke a test
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest


from auditapp.models import  Item, Contributor

def invoke_test(request: HttpRequest ) -> HttpResponse:
    """
    A form to select a work item and invoke the test for it
    :param request:
    :param work_id:
    :return:
    """
    item = get_object_or_404(Item, pk=request.POST['work_id'])
    # Todo. Run a test
    # Left off here:
    return render(request, )
