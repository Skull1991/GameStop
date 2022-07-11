from django.urls import path,include
from app import views

urlpatterns = [
    path("",views.home),
    path("about",views.about),
    path("contact",views.contact),
    path("playstation",views.playstation),
    path("xbox",views.xbox),
    path("nintendo",views.nintendo),
    path("login",views.login),
    path("cart",views.cart),
    path("profile/<int:id>",views.profile),
    path("eupdate/<int:id>",views.eupdate),
    path("eprofile/<int:id>",views.eprofile),
    path("eprofile",views.eprofile)
  
]