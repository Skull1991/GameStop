from django.urls import include, path

from login import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("login",views.login),
]