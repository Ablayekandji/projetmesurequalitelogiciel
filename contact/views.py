from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Contact

# Create your views here.

def home(request):
    return render(request,"pages/index.html")

def about(request):
    return render(request,"pages/about.html")

@login_required(login_url="/login/")
def contact_list(request):
    user=request.user
    contacts=Contact.objects.filter(auteur=user)
    print(contacts)
    return render(request,"contacts/contact_list.html",{"contacts":contacts})

@login_required(login_url="/login/")
def contact_details(request,id):
    contact=get_object_or_404(Contact,id=id)
    return render(request,"contacts/contact_detail.html",{"contact":contact})