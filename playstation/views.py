

# Create your views here.
from django.shortcuts import redirect, render


from playstation.models import playstation
from playstation.forms import ItemForm
# Create your views here.
def home(request):
    product=playstation.objects.all()
    return render(request,"playstation.html",{'products':product})

def pdetails(request,id):
    data=playstation.objects.get(id=id)
    print(id)
    return render(request,"pdetails.html",{'data':data})
