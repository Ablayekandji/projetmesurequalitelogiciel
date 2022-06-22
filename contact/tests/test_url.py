from django.test import SimpleTestCase
from django.urls import reverse,resolve
from contact.views import home, about,contact_list,contact_details,new_contact,edit_contact,delete_contact


class TestUrls(SimpleTestCase):
    
    
    def test_url_home(self):
        url=reverse('index')
        self.assertEquals(resolve(url).func,home)
    
    def test_url_contact_list(self):
        url=reverse('contacts')
        self.assertEquals(resolve(url).func,contact_list)