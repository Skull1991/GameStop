from django.contrib import admin

from playstation.models import playstation

# Register your models here.

class playstationAdmin(admin.ModelAdmin):

    list_display=('id','name','price','quantity','des', 'image')

admin.site.register(playstation,playstationAdmin)