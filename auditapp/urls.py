from django.urls import path

from . import views

# Magic name - See auditapp templates
app_name = 'auditapp'
urlpatterns = [  # ex: /auditapp/
    path('', views.index, name="indexYY"),  # /auditapp/3
    path('submittal/<int:submittal_id>', views.submittal, name="submittal"),  # ex: /auditapp/work/5
    path('item/<int:item_id>', views.item, name="item"),  # ex: '/auditapp/contrib/3
    path('contrib/<int:c_id>', views.contributor, name="contributor")]
