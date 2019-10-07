from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'index.html')
def Aboutus(request):
    return render(request,'about-us.html')
def Contact(request):
    return render(request,'contact.html')
def Portfolio(request):
    return render(request,'gallery.html')