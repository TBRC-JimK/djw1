from django.urls import path

from . import views

# Magic name - See auditapp templates
app_name = 'auditapp'
urlpatterns = [  # ex: /auditapp/

    # indexYY the 'name' value as called by the {% url %} template tag
    path('', views.index, name="indexYY"),  # /auditapp/3
    path('submittal/<int:submittal_id>', views.submittal, name="submittal"),  # ex: /auditapp/work/5
    path('item/<int:item_id>', views.item, name="item"),  # ex: '/auditapp/item/3
    path('<int:item_id>/get_tests/', views.select_tests_for_item, name="select_tests"),  # ex: '/auditapp/item/3
    path('<int:item_id>/run_tests/', views.run_tests_for_item, name="run_tests_for_item_name"),  # ex: '/auditapp/item/3

    path('contrib/<int:c_id>', views.contributor, name="contributor")]
