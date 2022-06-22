from http import client
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from contact.models import Contact


class TestViews(TestCase):
    
    
    def test_liste_clients(self):
        client=Client()
        response=client.get(reverse('index'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'pages/index.html')