

# Create your views here.
from django.shortcuts import redirect, render
from orders.models import Order
from django.contrib.auth.models import User

from product.models import Product
from product.forms import ProductForm
# Create your views here.
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

def search_venues(request):
    if request.method== "POST":
        searched = request.POST['searched']
        products= Product.objects.filter(name__icontains=searched)
        return render(request,"search.html",{'products':products,'searched':searched})
    else:
        return render(request,"search.html",{})


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


@login_required(login_url="/user/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/cart")


@login_required(login_url="/user/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/cart")


@login_required(login_url="/user/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/cart")


@login_required(login_url="/user/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/user/login")
def cart_detail(request):
    return render(request, 'cart.html')

@login_required(login_url="/user/login")
def checkout(request):
    if request.method=="POST":
        phonenumber=request.POST.get('phonenumber')
        email=request.POST.get('email')
        address=request.POST.get('address')
        payment=request.POST.get('payment')
        cart=request.session.get('cart')
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(pk=uid)
        
        for i in cart:
            a=(float(cart[i]['price']))
            b=cart[i]['quantity']
            total=a*b
            
            order=Order(
                user=user,
                name=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                image=cart[i]['image'],
                phonenumber=phonenumber,
                email=email,
                address=address,
                payment=payment,
                total=total,
            )
            order.save()
        request.session['cart']={}
        return redirect("/")

       
def order(request):
    uid=request.session.get('_auth_user_id')
    user=User.objects.get(pk=uid)
    order=Order.objects.filter(user=user)

    return render(request, "order.html",{'order':order})

