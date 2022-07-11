from django.urls import path
from xbox import views

urlpatterns = [
    path("",views.home),
    path("xdetails/<int:id>",views.xdetails),

    
]