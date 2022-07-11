from django.contrib import admin

from nintendo.models import nintendo

# Register your models here.

class nintendoAdmin(admin.ModelAdmin):

    list_display=('id','name','price','quantity','des', 'image')

admin.site.register(nintendo,nintendoAdmin)