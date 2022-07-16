

# Create your views here.
from django.shortcuts import redirect, render


from product.models import Product
from product.forms import ProductForm
# Create your views here.
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

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