from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from product.views import home,details,xbox,playstation,nintendo,order,checkout,search_venues
from django.contrib.auth import get_user_model
from product.views import order as order
from app.views import eprofile,contact,about,login,cart

# Create your tests here.
class TestUrls(SimpleTestCase):

    def test_xbox_url(self):
        url = reverse(xbox)
        print(url)
        self.assertEquals(resolve(url).func,xbox)
    def test_eprofile_url(self):
        url = reverse(eprofile)
        print(url)
        self.assertEquals(resolve(url).func,eprofile)
    def test_home_url(self):
        url = reverse(home)
        print(url)
        self.assertEquals(resolve(url).func,home)

    def test_checkout_url(self):
        url = reverse(checkout)
        print(url)
        self.assertEquals(resolve(url).func,checkout)

    
    
    def test_playstation_Render(self):
        url = reverse(playstation)
        print(url)
        self.assertEquals(resolve(url).func,playstation)

User = get_user_model
class TestViews(TestCase):

    def test_nintendo_Render12(self):
        url = reverse(nintendo)
        response= self.assertEquals(resolve(url).func,nintendo)
        self.assertTemplateUsed(response, "nintendo.html")
    
    
    def test_order_Render12(self):
        url = reverse(order)
        response= self.assertEquals(resolve(url).func,order)
        self.assertTemplateUsed(response, "admin/userorder.html")
    

    def test_order_display(self):
        url = reverse(order)
        response= self.assertEquals(resolve(url).func,order)
        self.assertTemplateUsed(response, 'order.html')

      
    def test_search_venues(self):
        url = reverse(search_venues)
        response= self.assertEquals(resolve(url).func,search_venues)
        self.assertTemplateUsed(response, 'search.html')
    
          
    def test_checkout(self):
        url = reverse(checkout)
        response= self.assertEquals(resolve(url).func,checkout)
        self.assertTemplateUsed(response, 'cart.html')
        
           
    def test_contact(self):
        url = reverse(contact)
        response= self.assertEquals(resolve(url).func,contact)
        self.assertTemplateUsed(response, 'contact.html')

          
    def test_cart(self):
        url = reverse(cart)
        response= self.assertEquals(resolve(url).func,cart)
        self.assertTemplateUsed(response, 'cart.html')

           
    def test_login(self):
        url = reverse(login)
        response= self.assertEquals(resolve(url).func,login)
        self.assertTemplateUsed(response, 'login.html')


    def test_about(self):
        url = reverse(about)
        response= self.assertEquals(resolve(url).func,about)
        self.assertTemplateUsed(response, 'about.html')
    