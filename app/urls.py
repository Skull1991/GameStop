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
    path("details/<int:id>",views.details),
    path("profile/<int:id>",views.profile),
    path("eupdate/<int:id>",views.eupdate),
    path("eprofile/<int:id>",views.eprofile),
    path("eprofile",views.eprofile),
    path("adminlogin",views.adminlogin),
  
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

]