from django.urls import path
from playstation import views

urlpatterns = [
    path("",views.home),
    path("pdetails/<int:id>",views.pdetails)
    
]