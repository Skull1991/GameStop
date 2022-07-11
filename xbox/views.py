

# Create your views here.
from django.shortcuts import redirect, render


from xbox.models import xbox
from xbox.forms import ItemForm
# Create your views here.
def home(request):
    product=xbox.objects.all()
    return render(request,"xbox.html",{'products':product})

def xdetails(request,id):
    data=xbox.objects.get(id=id)
    print(id)
    return render(request,"xdetails.html",{'data':data})



