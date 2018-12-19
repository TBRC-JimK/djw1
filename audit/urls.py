from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="indexYY"),
    # localhost:8000/audit/gartweezix
    path('gartweezix',views.shmeng,name="rootnTootn")
]