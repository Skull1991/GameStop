from django.contrib import admin
from django.urls import path,include
from adminpg import views

urlpatterns = [
    path('',views.adminlogin),
    path('home',views.adminhome, name="home"),
    path('order',views.order, name="order"),
 
    path('logout',views.logoutadmin),
    path('addproducts',views.addproducts),
    path('add',views.add),
    path('delete/<int:id>',views.delete),
    
    path('edit/<int:id>/', views.edit ,name="edit"),
    path('updatepage/<int:id>', views.updatepage)

    
    # path('',views.login_signup),
    
]