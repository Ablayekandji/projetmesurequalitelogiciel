from unicodedata import name
from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from contact.models import Contact
from django.shortcuts import get_object_or_404


class TestModel(TestCase):
    
    
    def setUp(self):
        user = User.objects.create_user(username="niania", email="niania@gmail.com", password="Passer12345")
        self.contact=Contact.objects.create(
            auteur=user,
            nom="nionio",
            prenom="prenom",
            telephone="777673101",
            email="770000000"
        )
        self.contact.save()
    
    def test_contact(self):
        nouveau=get_object_or_404(Contact,id=1)
        self.assertTrue(nouveau)
    
    