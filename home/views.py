from django.shortcuts import render, HttpResponse
# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'index.html' , context)
    # return HttpResponse("this is homepage")
from django.shortcuts import redirect
def about(request):
    return redirect ("https://www.instagram.com/thatshowyoucode.y?igsh=MnV6ajBoM252cnds")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    return HttpResponse("this is my contact")

def hi(request):
    return HttpResponse("helooooo ") 