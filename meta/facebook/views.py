from django.shortcuts import render
from facebook.models import Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'home.html')

def contact(request):
    if request.method == "POST":
        first_name=request.POST.get('name')
        last_name=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contacts=Contact(first_name=first_name,last_name=last_name,email=email,phone=phone)
        contacts.save()
        return HttpResponse('registration sucessful')
      
    return render(request,'contact.html')

def signup(request):
    pass

 
