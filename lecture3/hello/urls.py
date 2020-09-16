from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("nithya",views.nithya, name="nithya"),
    path("<str:name>",views.greet, name="greet"),
]