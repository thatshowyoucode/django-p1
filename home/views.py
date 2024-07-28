from django.shortcuts import render, HttpResponse
# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")
def about(request):
    return render(request, 'about.html')
    # return redirect ("https://www.instagram.com/thatshowyoucode.y?igsh=MnV6ajBoM252cnds")

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')