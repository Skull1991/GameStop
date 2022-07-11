

# Create your views here.
from django.shortcuts import redirect, render


from product.models import Product
from product.forms import ProductForm
# Create your views here.
def xbox(request):
    product=Product.objects.all()
    return render(request,"xbox.html",{'products':product})

