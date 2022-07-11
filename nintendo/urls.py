from django.urls import path
from nintendo import views

urlpatterns = [
    path("",views.home),
    path("ndetails/<int:id>",views.ndetails)

]