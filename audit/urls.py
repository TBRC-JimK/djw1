from django.urls import path

from . import views

urlpatterns = [
    # ex: /audit/
    path('', views.index, name = "indexYY"),
    # /audit/3
    path('submittal/<int:submittal_id>', views.submittal, name = "Submittal"),
    # ex: /audit/work/5
    path('work/<int:work_id>', views.work, name = "work"),
    # ex: '/audit/contrib/3
    path('contrib/<int:c_id>', views.contributor, name = "Contributor")
]
