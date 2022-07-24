import imp
from unicodedata import category
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from product.models import Product
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
# Create your views here.

def adminlogin(request):
    return render(request,"adminlogin.html")

def home(request):
    console=Product.objects.filter(category='console')[0:3]
    xbox=Product.objects.filter(accessories='xbox')
    playstation=Product.objects.filter(accessories='playstation')
    nintendo=Product.objects.filter(accessories='nintendo')
    return render(request, 'home.html', {'console': console,'xbox':xbox,'playstation':playstation,'nintendo':nintendo,'nbar': 'home'})

def details(request,id):
    data=Product.objects.get(id=id)
    print(id)
    return render(request,"details.html",{'data':data})

def xbox(request):
    xbox=Product.objects.filter(games='xbox')
    return render(request,'xbox.html',{'xbox':xbox})

def playstation(request):
    playstation=Product.objects.filter(games='playstation')
    return render(request,'playstation.html',{'playstation':playstation})

def nintendo(request):
    nintendo=Product.objects.filter(games='nintendo')
    return render(request,'nintendo.html',{'nintendo':nintendo})

def about(request):
    return render(request, 'about.html', {'nbar': 'about'})

def profile(request,id):
    data=User.objects.get(id=id)
    print(id)
    return render(request,"profile.html",{'data':data})

def eprofile(request,id):
    data=User.objects.get(id=id)
    print(id)
    return render(request,"eprofile.html",{'data':data})

def eupdate(request,id):
    data=User.objects.get(id=id)
    f_name = request.POST['first_name']
    l_name = request.POST['last_name']
    email = request.POST['email']
    data.first_name=(f_name)
    data.last_name=(l_name)
    data.email=(email)
    data.save()
    return redirect("/")

def contact(request):
    return render(request, 'contact.html', {'nbar': 'contact'})

def cart(request):
    return render(request, 'cart.html')

def recipt(request):
    return render(request, 'recipt.html')


def login(request):
    return render(request, 'login.html')




# cart
@login_required(login_url="/user/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")



def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/cart")



def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/cart")



def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/cart")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")



def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

