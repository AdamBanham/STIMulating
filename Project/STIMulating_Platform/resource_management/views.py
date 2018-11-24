from django.shortcuts import render

# Create your views here.
def home(request):
    #render the home directory back to the browser
    return render(request,'resource_management/home.html')

def about(request):
    #render the about directory back to the browser
    return render(request,'resource_management/about.html')