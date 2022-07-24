from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from orders.models import Order
from product.forms import ProductForm
from django.contrib.auth.decorators import login_required
from product.views import Product

# Create your views here.
def adminlogin(request):
    if (request.method=="POST"):
        username=request.POST['username']
        
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)

        if user is not None:
            if user.is_superuser == 1:
                login(request,user)
                return redirect('/adminpg/home')
            else:
                messages.error(request,"Username and Password Don't Match, Please Try Again !")
                return redirect('/admin')
        else:
            messages.error(request,"Username and Password Don't Match, Please Try Again !")

    else:
        return render(request, 'admin/adminlogin.html')

def adminhome(request):
    products=Product.objects.all()
    # console = Product.objects.filter(console='console').values().order_by('-id')[0:4]
    # xbox = Product.objects.filter(productCategory='audio').values().order_by('-id')
    # power = Product.objects.filter(productCategory='power').values().order_by('-id')
    # fitness = Product.objects.filter(productCategory='fitness').values().order_by('-id')
    # return render(request, 'admin/adminhome.html' ,{'products': products,'audio': audio,'power': power,'fitness': fitness, 'nbar':'home'})
    return render(request, 'admin/adminhome.html' ,{'products': products})


def logoutadmin(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/admin") 
def addproducts(request):
    return render(request, "admin/addproduct.html")

def add(request):
    data = ProductForm(request.POST, request.FILES)
    print(request.POST)
    data.save()
    return redirect('/adminpg/home')



def edit(request,id):
    data=Product.objects.get(id=id)
    return render(request, "admin/editproduct.html",{'data':data})

def updatepage(request,id):
    data=Product.objects.get(id=id)
    form=ProductForm(request.POST,request.FILES,instance=data)
    form.save()
    return redirect("/adminpg/home")

def delete(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect("home")

@login_required(login_url="/admin") 
def order(request):
    order=Order.objects.all()
    return render(request, "admin/userorder.html",{'order':order})
    
  