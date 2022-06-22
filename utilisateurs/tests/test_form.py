from django.test import SimpleTestCase
from utilisateurs import forms

class TestForm(SimpleTestCase):
    
    def test__login_formulaire_valide(self):
        form=forms.LoginForm(data={
            'username':'thuglife',
            'password':'nianiania'
        })
        
        self.assertTrue(form.is_valid())
        
    def test_login_formulaire_vide(self):
        form=forms.LoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)
    
    
    def test__login_formulaire_non_valide(self):
        form=forms.LoginForm(data={
            'username':'thuglife',
            'password':''
        })
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)
    
    
    def test__register_formulaire_valide(self):
        form=forms.SignUpForm(data={
            'username':'thuglife',
            'email':'niania@nionio.com',
            'password1':'nianiania',
            'password2':'nianiania'
        })
        # self.assertTrue(form.is_valid())