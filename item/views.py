

# Create your views here.
from django.shortcuts import redirect, render


from item.models import item
from item.forms import ItemForm
# Create your views here.
def home(request):
    items=item.objects.all()
    return render(request,"item/home.html",{'items':items})

def cart(request):
    return render(request,'item/cart.html')

def create(request):
    return render(request,'item/create.html')

def save(request):

    print(request.POST)
    print(request.FILES)
    data=ItemForm(request.POST,request.FILES)
    data.save()
    return redirect('/item')

def edit(request,id):
    data=item.objects.get(id=id)
    print(id)
    return render(request,"item/edit.html",{'data':data})

def update(request,id):
    data=item.objects.get(id=id)
    form=ItemForm(request.POST,request.FILES,instance=data)
    form.save()
    return redirect("/item")

def delete(request,id):
    data=item.objects.get(id=id)
    data.delete()
    return redirect("/item")