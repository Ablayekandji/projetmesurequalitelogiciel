from django.urls import path
from .views import home, about,contact_list,contact_details

urlpatterns = [
    path("",home,name="index"),
    path("about/",about,name="about"),
    path("contacts/",contact_list,name="contacts"),
    path("contacts/<int:id>/",contact_details,name="details")

]
