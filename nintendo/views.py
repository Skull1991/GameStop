

# Create your views here.
from django.shortcuts import redirect, render


from nintendo.models import nintendo
from nintendo.forms import ItemForm
# Create your views here.
def home(request):
    product=nintendo.objects.all()
    return render(request,"nintendo.html",{'products':product})


def ndetails(request,id):
    data=nintendo.objects.get(id=id)
    print(id)
    return render(request,"ndetails.html",{'data':data})

