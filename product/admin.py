from django.contrib import admin

from product.models import Product

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):

   list_display=('id','name','price','quantity','des','accessories','category','games', 'image')

admin.site.register(Product,ProductsAdmin)