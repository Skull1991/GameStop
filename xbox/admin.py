from django.contrib import admin

from xbox.models import xbox

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):

   list_display=('id','name','price','quantity','des', 'image')

admin.site.register(xbox,ProductsAdmin)