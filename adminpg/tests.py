from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from product.views import order as order
from adminpg.views import addproducts, adminlogin,adminhome,logoutadmin,add,order

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_adminlogin_url(self):
        url = reverse(adminlogin)
        print(url)
        self.assertEquals(resolve(url).func,adminlogin)
    def test_adminhome_url(self):
        url = reverse(adminhome)
        print(url)
        self.assertEquals(resolve(url).func,adminhome)
    def test_order_url(self):
        url = reverse(order)
        print(url)
        self.assertEquals(resolve(url).func,order)

    def test_logoutadmin_url(self):
        url = reverse(logoutadmin)
        print(url)
        self.assertEquals(resolve(url).func,logoutadmin)

    
    
    def test_add_Render(self):
        url = reverse(add)
        print(url)
        self.assertEquals(resolve(url).func,add)

User = get_user_model
class TestViews(TestCase):

    def test_addproducts_Render12(self):
        url = reverse(addproducts)
        response= self.assertEquals(resolve(url).func,addproducts)
        self.assertTemplateUsed(response, "admin/addproduct.html")
    
    
    def test_adminhome_Render12(self):
        url = reverse(adminhome)
        response= self.assertEquals(resolve(url).func,adminhome)
        self.assertTemplateUsed(response, "admin/adminhome.html")