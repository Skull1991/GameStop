from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'home.html', {'nbar': 'home'})


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

def playstation(request):
    return render(request, 'playstation.html', {'nbar': 'playstation'})

def xbox(request):
    return render(request, 'xbox.html', {'nbar': 'xbox'})

def nintendo(request):
    return render(request, 'product/nintendo.html', {'nbar': 'nintendo'})

def login(request):
    return render(request, 'login.html')




